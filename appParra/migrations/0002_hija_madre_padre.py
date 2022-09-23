# Generated by Django 4.1 on 2022-09-21 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appParra', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hija',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('edad', models.IntegerField()),
                ('fechaDeNacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Madre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('edad', models.IntegerField()),
                ('fechaDeNacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Padre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('edad', models.IntegerField()),
                ('fechaDeNacimiento', models.DateField()),
            ],
        ),
    ]
