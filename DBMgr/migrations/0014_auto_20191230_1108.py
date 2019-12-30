# Generated by Django 2.2.6 on 2019-12-30 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DBMgr', '0013_auto_20191230_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritecompany',
            name='favorite',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='company_related', to='DBMgr.Company'),
        ),
        migrations.AlterField(
            model_name='favoritestore',
            name='favorite',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='store_related', to='DBMgr.ConvenienceStore'),
        ),
    ]
