# Generated by Django 4.2 on 2023-04-08 13:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0003_order_created_at_alter_order_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="transaction_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
