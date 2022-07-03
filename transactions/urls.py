from django.urls import path
from transactions import views


app_name = "transaction_app"

urlpatterns = [
    path('transaction_list/', views.ItemTransactionView.as_view(), name="transaction-list"),
    path('transaction/<str:trans>/', views.search_item, name="transaction"),
    path('transaction/<str:trans>/item/<pk>', views.item_transaction_detail, name="transaction-item"),
    path('transaction/confirmation/<str:trans>/item/<pk>/<amount>/', views.confirmation_on_item, name="confirmation"),
    path('transaction/<str:trans>/item/<pk>/<amount>/', views.transaction_on_item, name="trans_on_item"),
    path('transaction/tranaction_error/<str:trans>/<pk>/<amount>', views.transaction_error, name="transaction_error")




    # path('transactions/item_search_for_transaction/', views.transaction_item_search),

    ]

