from const import TRANSACTION_TYPES
from models import TransactionType


def transactions_initialize():
    for transaction in TRANSACTION_TYPES:
        TransactionType.objects.create(name=transaction[0], description=transaction[2])


if __name__ == '__main__':
    transactions_initialize()
