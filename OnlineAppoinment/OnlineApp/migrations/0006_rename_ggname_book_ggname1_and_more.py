# Generated by Django 4.0.1 on 2022-01-28 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineApp', '0005_book_alumnibook_stats1_studentbook_ggname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Ggname',
            new_name='Ggname1',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Scourse',
            new_name='Scourse1',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Sdate',
            new_name='Sdate1',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Sdep',
            new_name='Sdep1',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Slast',
            new_name='Slast1',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Smail',
            new_name='Smail1',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Sname',
            new_name='Sname1',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Spurp',
            new_name='Spurp1',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Ssid',
            new_name='Ssid1',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Syear',
            new_name='Syear1',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='status',
            new_name='status1',
        ),
    ]
