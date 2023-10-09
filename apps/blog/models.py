from django.db import models
from ..account.models import User

class Country(models.Model):
    title = models.CharField("Страна", max_length=100)
    image = models.ImageField("Картинка", upload_to="country/")
    content = models.TextField("Контент", null=True, blank=True)

    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


    @property
    def short_content(self):
        return f"{self.content[:20]}..."
    

class City(models.Model):
    county = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="cities", verbose_name="Страна")
    title = models.CharField("Город", max_length=100)
    content = models.TextField("Контент", null=True, blank=True)
    price = models.DecimalField("Цена", max_digits=6, decimal_places=2)
    is_available = models.BooleanField("Активно", default=True)
    lat = models.FloatField("Широта", null=True, blank=True)
    lot = models.FloatField("Долгота", null=True, blank=True)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.title


class CityImages(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="images", verbose_name="Город")
    image = models.ImageField("Картинка", upload_to="cities/", null=False)

    class Meta:
        verbose_name = "Картинка города"
        verbose_name_plural = "Картинки города"

    def __str__(self):
        return self.city.title
    

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", verbose_name="Комментарии")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="comments", verbose_name="Публикация")
    text = models.TextField(verbose_name="Текст комментария")
    created = models.DateTimeField(verbose_name="Дата публикации", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, verbose_name="Ответ комментарию", related_name="answers", null=True, blank=True)

    def __str__(self):
        return f"{self.owner.username} {self.text[:20]}"
    
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
