# Generated by Django 4.1.7 on 2023-02-28 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dictionary', '0004_alter_dictionary_meaning_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionary',
            name='word',
            field=models.CharField(max_length=255),
        ),
    ]