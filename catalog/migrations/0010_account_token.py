# Generated by Django 5.0.7 on 2024-08-12 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0009_account"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="token",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="token"
            ),
        ),
    ]
