# Generated by Django 5.1.6 on 2025-03-11 02:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('upload_image', models.ImageField(blank=True, null=True, upload_to='promotions/images/')),
                ('upload_video', models.FileField(blank=True, null=True, upload_to='promotions/videos/')),
                ('enable', models.BooleanField(default=True)),
                ('sort_order', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
