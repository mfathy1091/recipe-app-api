from django.db import models


class CATEGORY_TYPE(models.TextChoices):
    expense = "expense", "Expense"
    salary = "income", "Income"
    bonus = "loan", "Loan"


class Category(models.Model):
    name = models.CharField(unique=True, blank=False, null=False, max_length=50)
    type = models.CharField(choices=CATEGORY_TYPE.choices, max_length=50)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(blank=False, null=False)
    notes = models.CharField(max_length=255, blank=True, null=False)
