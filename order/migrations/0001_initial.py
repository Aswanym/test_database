# Generated by Django 4.0.2 on 2022-07-22 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('content', models.CharField(max_length=100, null=True)),
                ('app_name', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': '"order"."order"',
            },
        ),
        migrations.CreateModel(
            name='SecondOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('second_title', models.CharField(max_length=100, null=True)),
                ('second_content', models.CharField(max_length=100, null=True)),
                ('second_app_name', models.CharField(max_length=100, null=True)),
                ('fist_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
            options={
                'db_table': '"order"."second_order"',
            },
        ),
    ]
