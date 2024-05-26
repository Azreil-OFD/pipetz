from django.db import models


class Competitions(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Описание испытаний предстоящих на соревнованиях')
    places = models.IntegerField('Количество мест для участия')
    date = models.DateTimeField('Дата проведения')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Соревнование'
        verbose_name_plural = 'Соревнования'
