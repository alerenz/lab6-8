# Generated by Django 4.2 on 2023-05-15 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_bank_otchevsto_remove_clients_otchevsto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sotrudnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('data_birth', models.DateField(verbose_name='Дата рождения')),
                ('stazh', models.IntegerField(verbose_name='Стаж')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]