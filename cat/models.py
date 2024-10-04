from django.db import models
from cat_exhibition import settings


class Breed(models.Model):
    breed = models.CharField(max_length=255, verbose_name='Порода')

    def __str__(self):
        return f'{self.breed}'

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'


class Cat(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    color = models.CharField(max_length=255, verbose_name='Цвет')
    age_months = models.IntegerField(verbose_name='Возраст (полных месяцев')
    description = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', related_name='owner')
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name='Порода')
    ratings_count = models.IntegerField(verbose_name='Количество оценок', default=0)
    ratings_score = models.IntegerField(verbose_name='Рейтинг', default=0)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Котенок'
        verbose_name_plural = 'Котята'

    @property
    def average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return sum(int(rating.score) for rating in ratings) / ratings.count()


class Rating(models.Model):
    SCORES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, verbose_name='Котенок', related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец')
    score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Оценка')

    def __str__(self):
        return f'{self.cat.name} - {self.score}'

    class Meta:
        unique_together = ('cat', 'user')




