# Generated by Django 5.2.1 on 2025-05-31 12:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CustomerModel",
            fields=[
                ("customer_id", models.IntegerField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(blank=True, max_length=200, null=True)),
                ("last_name", models.CharField(blank=True, max_length=200, null=True)),
                ("age", models.IntegerField(blank=True, null=True)),
                ("phone_number", models.BigIntegerField(blank=True, null=True)),
                ("monthly_salary", models.IntegerField(blank=True, null=True)),
                ("approved_limit", models.IntegerField(blank=True, null=True)),
                ("current_debt", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="LoanModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("loan_id", models.IntegerField()),
                (
                    "loan_amount",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("tenure", models.IntegerField(blank=True, null=True)),
                (
                    "interest_rate",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "monthly_repayment",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("emis_paid_on_time", models.IntegerField(blank=True, null=True)),
                ("start_date", models.DateField(blank=True, null=True)),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "customer_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.customermodel",
                    ),
                ),
            ],
        ),
    ]
