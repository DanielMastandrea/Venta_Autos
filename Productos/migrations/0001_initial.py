# Generated by Django 4.1 on 2022-08-06 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=40)),
                ('model', models.CharField(max_length=40)),
                ('year', models.IntegerField()),
                ('price', models.FloatField()),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('creation_date', models.DateField(auto_now_add=True, null=True)),
                ('stock', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Auto',
                'verbose_name_plural': 'Autos',
            },
        ),
    ]
