# Generated by Django 4.0.1 on 2022-01-28 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineApp', '0006_rename_ggname_book_ggname1_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AddField(
            model_name='studentbook',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]