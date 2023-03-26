from django.db import models


class Articles(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=250)
    text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
