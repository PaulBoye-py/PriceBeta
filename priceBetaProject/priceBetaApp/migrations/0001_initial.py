# Generated by Django 3.2.14 on 2022-07-24 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('rating', models.IntegerField()),
                ('Created_date', models.DateTimeField()),
            ],
        ),
    ]
