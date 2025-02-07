# Generated by Django 5.0.3 on 2024-04-04 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competitions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('full_text', models.TextField(verbose_name='Описание испытаний предстоящих на соревнованиях')),
                ('places', models.IntegerField(verbose_name='Количество мест для участия')),
                ('date', models.DateTimeField(verbose_name='Дата проведения')),
                ('relevance', models.BooleanField(verbose_name='Актуальность')),
            ],
            options={
                'verbose_name': 'Соревнование',
                'verbose_name_plural': 'Соревнования',
            },
        ),
    ]
