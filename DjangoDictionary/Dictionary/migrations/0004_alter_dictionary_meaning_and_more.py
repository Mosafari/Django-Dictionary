# Generated by Django 4.1.7 on 2023-02-28 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dictionary', '0003_dictionary_src_alter_dictionary_targetlang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionary',
            name='meaning',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='dictionary',
            name='pronunciation',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='dictionary',
            name='src',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='dictionary',
            name='targetlang',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
