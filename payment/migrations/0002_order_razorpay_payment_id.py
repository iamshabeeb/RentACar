# Generated by Django 4.0.5 on 2022-10-06 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='razorpay_payment_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
