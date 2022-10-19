# Generated by Django 4.0.5 on 2022-10-05 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
        ('guide', '0001_initial'),
        ('variations', '0002_alter_variation_driver_items_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='driver_items',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='driver.drivers'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='guide_items',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='guide.guide'),
        ),
    ]