# Generated by Django 4.0.10 on 2024-06-07 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_transaction_date_transaction_notes_transaction_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('cash', 'Cash'), ('credit_card', 'Credit Card')], max_length=30)),
            ],
        ),
    ]