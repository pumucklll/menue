# Generated by Django 5.0.2 on 2024-02-27 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menue', '0002_alter_book_verkaufspreis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Verkaufspreis',
            field=models.FloatField(),
        ),
    ]
