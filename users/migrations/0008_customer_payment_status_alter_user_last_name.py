# Generated by Django 4.1.7 on 2023-02-18 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='payment_status',
            field=models.BooleanField(default=False, verbose_name='Статус оплаты'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, default=False, max_length=150, verbose_name='last name'),
            preserve_default=False,
        ),
    ]
