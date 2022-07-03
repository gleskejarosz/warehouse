from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
# from django.views.generic import DetailView
from items.models import Item, input_to_stock, withdraw, total_scrap, scrap, return_to_stock

from transactions.models import TransactionType, TransactionArchive
from transactions.forms import ItemTransactionFilter, AmountTransactionForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


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


class ItemTransactionView(View):
    def get(self, request):
        return render(
            request,
            template_name="transactions/transactions.html",
            context={"transactions": TransactionType.objects.all()}
        )


# class ItemTransactionDetail(DetailView):
#     model = Item
#     template_name = 'transactions/detail_item_trans.html'


class ItemTransactionDetail(View):
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


def search_item(request, trans: str):
    items_list = Item.objects.all().order_by('-registration_date')
    items_filter = ItemTransactionFilter(request.GET, queryset=items_list)
    return render(
        request,
        template_name='transactions/filter_list.html',
        context={
            'filter': items_filter,
            'trans': trans
        }
    )


def item_transaction_detail(request, pk, trans):
    form = AmountTransactionForm(request.POST or None)
    item = get_object_or_404(Item, pk=pk)
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
            'transaction': transaction,
            'form': form
        }
    )


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
    return render(
        request,
        template_name='transactions/confirmation.html',
        context={
            'item': item,
            'trans': trans,
            'amount': amount
        }
    )


def archive_transaction(item, transaction, quantity, after):
    TransactionArchive.objects.create(
        transaction=transaction,
        item=item,
        quantity=quantity,
        quantity_after=after
    )


def transaction_on_item(request, pk, trans, amount):
    item = get_object_or_404(Item, pk=pk)
    trans = get_object_or_404(TransactionType, name=trans)
    q_before = get_object_or_404(Item, pk=pk).quantity

    if trans.name == 'Input':
        input_to_stock(item, amount=int(amount))
        item.save()

    if trans.name == 'Withdraw':
        withdraw(item, amount=int(amount))
        item.save()

    if trans.name == 'Total Scrap':
        total_scrap(item)
        item.save()

    if trans.name == 'Scrap':
        scrap(item, amount=int(amount))
        item.save()

    if trans.name == 'Return to stock':
        return_to_stock(item, amount=int(amount))
        item.save()

    q_after = get_object_or_404(Item, pk=pk).quantity

    if q_after != q_before:
        archive_transaction(item=item, transaction=trans, quantity=amount, after=q_after)
        return HttpResponseRedirect(reverse("transaction_app:transaction", args={trans.name}))

    return HttpResponseRedirect(reverse("transaction_app:transaction_error", args={trans.name, pk, amount}))





