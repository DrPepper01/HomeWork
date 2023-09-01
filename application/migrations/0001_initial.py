# Generated by Django 4.2.4 on 2023-08-24 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('info', models.CharField(max_length=200)),
                ('price', models.IntegerField(blank=True)),
            ],
        ),
    ]
