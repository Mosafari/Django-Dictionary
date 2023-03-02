# Generated by Django 4.1.7 on 2023-02-28 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dictionary', '0002_dictionary_pronunciation'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictionary',
            name='src',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dictionary',
            name='targetlang',
            field=models.CharField(max_length=255),
        ),
    ]
