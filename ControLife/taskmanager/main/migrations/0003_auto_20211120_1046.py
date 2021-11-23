# Generated by Django 3.2.9 on 2021-11-20 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211114_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purpose',
            name='fact',
        ),
        migrations.AlterField(
            model_name='timetable',
            name='name',
            field=models.CharField(choices=[('Fr', 'Friday'), ('We', 'Wednesday'), ('Su', 'Sunday'), ('Th', 'Thursday'), ('Tu', 'Tuesday'), ('Mo', 'Monday'), ('Sa', 'Saturday')], max_length=2, verbose_name='Day'),
        ),
    ]
