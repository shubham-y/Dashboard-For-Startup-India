# Generated by Django 2.1.1 on 2019-02-19 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dipp', '0005_statusreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusreport',
            name='month',
            field=models.CharField(max_length=40),
        ),
    ]