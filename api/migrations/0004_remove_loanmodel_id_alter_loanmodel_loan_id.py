# Generated by Django 5.2.1 on 2025-06-05 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_loanmodel_loan_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="loanmodel",
            name="id",
        ),
        migrations.AlterField(
            model_name="loanmodel",
            name="loan_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
