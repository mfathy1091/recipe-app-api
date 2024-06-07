# Generated by Django 4.0.10 on 2024-06-07 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0006_account_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('date', models.DateField(blank=True, null=True)),
                ('from_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transfers_out', to='expenses.account')),
                ('to_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transfers_in', to='expenses.account')),
            ],
        ),
    ]
