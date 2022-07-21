# Generated by Django 4.0.2 on 2022-07-21 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_newstore'),
    ]

    operations = [
        migrations.CreateModel(
            name='OldStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=100, null=True)),
                ('store_title', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': '"product"."old_store"',
            },
        ),
    ]