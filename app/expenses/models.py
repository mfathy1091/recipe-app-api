from django.db import models, transaction


class CATEGORY_TYPE(models.TextChoices):
    expense = "expense", "Expense"
    income = "income", "Income"
    Loan = "loan", "Loan"


class Category(models.Model):
    name = models.CharField(unique=True, blank=False, null=False, max_length=50)
    type = models.CharField(choices=CATEGORY_TYPE.choices, max_length=50)

    def __str__(self):
        return self.name


class ACCOUNT_TYPE(models.TextChoices):
    cash = "cash", "Cash"
    credit_card = "credit_card", "Credit Card"


class Account(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30, choices=ACCOUNT_TYPE.choices)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name


class TRANSACTION_TYPE(models.TextChoices):
    debit = "debit", "Debit"
    credit = "credit", "Credit"


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.CharField(max_length=30, choices=TRANSACTION_TYPE.choices, null=True, blank=True)
    date = models.DateField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        with transaction.atomic():
            if self.id is None:
                if self.type == TRANSACTION_TYPE.debit:
                    self.account.balance -= self.amount
                else:
                    self.account.balance += self.amount
            else:
                old_transaction = Transaction.objects.get(id=self.id)
                old_transaction_amount = old_transaction.amount
                if old_transaction_amount != self.amount:
                    diff = old_transaction_amount - self.amount
                    self.account.balance += diff
            self.account.save()
            super(Transaction, self).save(*args, **kwargs)


class Transfer(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateField(blank=True, null=True)
    from_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=False, related_name="transfers_out")
    to_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=False, related_name="transfers_in")

    def save(self, *args, **kwargs):
        with transaction.atomic():
            if self.id is None:
                self.from_account.balance -= self.amount
                self.to_account.balance += self.amount
            else:
                old_transfer_amount = Transfer.objects.get(id=self.id).amount
                if old_transfer_amount != self.amount:
                    diff = old_transfer_amount - self.amount
                    self.from_account.balance += diff
                    self.to_account.balance -= diff
            self.from_account.save()
            self.to_account.save()
            super(Transfer, self).save(*args, **kwargs)
