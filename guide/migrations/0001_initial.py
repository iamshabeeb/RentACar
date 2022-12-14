# Generated by Django 4.0.5 on 2022-10-01 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('phone', models.BigIntegerField()),
                ('place', models.CharField(max_length=50)),
                ('pin', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('experience', models.CharField(max_length=50)),
                ('aadhar_no', models.BigIntegerField()),
                ('price', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
