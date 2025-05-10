from django.db import models

class Bd(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    novelty = models.ForeignKey('Novelty', null=True, on_delete=models.PROTECT, verbose_name='Степень новизны', default='Не указано')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']


class Novelty(models.Model):
    name = models.CharField(max_length=15, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Степени новизны'
        verbose_name = 'Степень новизны'
        ordering = ['name']
