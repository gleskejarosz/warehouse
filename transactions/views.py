from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView

from items.models import Item, input_to_stock, withdraw, total_scrap, scrap, return_to_stock

from transactions.models import TransactionType, TransactionArchive
from transactions.forms import ItemTransactionFilter, AmountTransactionFormInt, AmountTransactionForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from transactions.__const__ import TRANSACTION_TYPES


@login_required
def transactions(request):
    return render(
        request,
        template_name="transactions/transactions.html",
        context={"transactions": TransactionType.objects.all()}
    )


def transaction_input(request):
    return render(
        request,
        template_name="transactions/detail_item_trans.html",
        context={
            "transaction": TransactionType.objects.all(),
            "items": Item.objects.all()
        }
    )


class ItemTransactionView(LoginRequiredMixin, View):
    def get(self, request):
        return render(
            request,
            template_name="transactions/transactions.html",
            context={"transactions": TransactionType.objects.all()}
        )


class ItemTransactionDetail(LoginRequiredMixin, View):
    def get(self, request, pk, trans):
        item = get_object_or_404(Item, pk=pk)
        transaction = get_object_or_404(TransactionType, name=trans)
        return render(
            request,
            template_name='transactions/detail_item_trans.html',
            context={
                'item': item,
                'transaction': transaction,
                'form': AmountTransactionForm()}
        )

@login_required()
def search_item(request, trans: str):
    if trans in ['Withdraw', 'Scrap', 'Total Scrap']:
        items_list = Item.objects.filter(quantity__gt=0).order_by('-registration_date')
    else:
        items_list = Item.objects.all().order_by('-registration_date')

    items_filter = ItemTransactionFilter(request.GET, queryset=items_list)
    transaction = get_object_or_404(TransactionType, name=trans)
    return render(
        request,
        template_name='transactions/filter_list.html',
        context={
            'filter': items_filter,
            'trans': transaction
        }
    )

@login_required()
def item_transaction_detail(request, trans, pk):
    item = get_object_or_404(Item, pk=pk)

    if item.unit.integer:
        form = AmountTransactionFormInt(request.POST or None)
    else:
        form = AmountTransactionForm(request.POST or None)

    transaction = get_object_or_404(TransactionType, name=trans)
    amount = form["amount"].value()

    if form.is_valid():
        return render(
            request,
            template_name='transactions/confirmation.html',
            context={
                'item': item,
                'trans': transaction,
                'amount': amount
            }
        )

    return render(
        request,
        template_name='transactions/detail_item_trans.html',
        context={
            'item': item,
            'trans': transaction,
            'form': form
        }
    )


@login_required()
def confirmation_on_item(request, pk, trans, amount):
    item = get_object_or_404(Item, pk=pk)
    trans = get_object_or_404(TransactionType, name=trans)
    return render(
        request,
        template_name='transactions/confirmation.html',
        context={
            'item': item,
            'trans': trans,
            'amount': amount
        }
    )


def transaction_error(request, pk, trans, amount):
    item = get_object_or_404(Item, pk=pk)

    message = "Action forbidden."

    if trans.name == "Withdraw":
        message = "Probably you want to withdraw more than stock has."

    return render(
        request,
        template_name='transactions/error.html',
        context={
            'item': item,
            'trans': trans,
            'amount': amount,
            'message': message
        }
    )


@login_required()
def archive_transaction(request, item, transaction, quantity, after):
    TransactionArchive.objects.create(
        transaction=transaction.name,
        item=item,
        quantity=quantity,
        quantity_after=after,
        who=request.user.username,
    )


@login_required()
def transaction_on_item(request, pk, trans, amount):
    item = get_object_or_404(Item, pk=pk)
    trans = get_object_or_404(TransactionType, name=trans)
    q_before = get_object_or_404(Item, pk=pk).quantity

    if trans.name == 'Input':
        input_to_stock(item, amount=float(amount))
        item.save()

    if trans.name == 'Withdraw':
        withdraw(item, amount=float(amount))
        item.save()

    if trans.name == 'Total Scrap':
        total_scrap(item)
        item.save()

    if trans.name == 'Scrap':
        scrap(item, amount=float(amount))
        item.save()

    if trans.name == 'Return to stock':
        return_to_stock(item, amount=float(amount))
        item.save()

    q_after = get_object_or_404(Item, pk=pk).quantity

    if q_after != q_before:
        archive_transaction(request=request, item=item, transaction=trans, quantity=amount, after=q_after)
        return HttpResponseRedirect(reverse("transaction_app:transaction", kwargs={"trans": trans.name}))

    return transaction_error(request, pk, trans, amount)


def transactions_initialize(request):
    for transaction in TRANSACTION_TYPES:
        TransactionType.objects.create(name=transaction[0], description=transaction[1])
    return HttpResponseRedirect(reverse("transaction_app:transaction-list"))


class TransactionArchiveView(ListView):
    template_name = "transactions/archive_list_view.html"
    model = TransactionArchive
    paginate_by = 10
