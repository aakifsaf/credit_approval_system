# Generated by Django 5.2.1 on 2025-06-07 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_loanmodel_id_alter_loanmodel_loan_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermodel',
            name='customer_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
