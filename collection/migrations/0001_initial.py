# Generated by Django 2.2.6 on 2020-01-02 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('open_data', '0004_auto_20200102_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='favoritestore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('favorite', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='store_related', to='open_data.ConvenienceStore')),
                ('favorite_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='favoriteshow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('favorite', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='show_related', to='open_data.show')),
                ('favorite_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='favoritecompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('favorite', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='company_related', to='open_data.Company')),
                ('favorite_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
