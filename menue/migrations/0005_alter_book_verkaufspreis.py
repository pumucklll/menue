# Generated by Django 5.0.2 on 2024-02-27 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menue', '0004_alter_book_verkaufspreis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Verkaufspreis',
            field=models.CharField(max_length=100),
        ),
    ]
