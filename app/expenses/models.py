from django.db import models


class CATEGORY_TYPE(models.TextChoices):
    expense = "expense", "Expense"
    income = "income", "Income"
    Loan = "loan", "Loan"


class Category(models.Model):
    name = models.CharField(unique=True, blank=False, null=False, max_length=50)
    type = models.CharField(choices=CATEGORY_TYPE.choices, max_length=50)

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


class ACCOUNT_TYPE(models.TextChoices):
    cash = "cash", "Cash"
    credit_card = "credit_card", "Credit Card"


class Account(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30, choices=ACCOUNT_TYPE.choices)
