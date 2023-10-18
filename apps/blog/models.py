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
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="cities", verbose_name="Страна")
    title = models.CharField("Город", max_length=100)
    content = models.TextField("Контент", null=True, blank=True)
    is_available = models.BooleanField("Активно", default=True)
    lat = models.FloatField("Широта", null=True, blank=True)
    lot = models.FloatField("Долгота", null=True, blank=True)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.title
    

class Ticket(models.Model):
    BUDGET = "budget"
    STANDART = "standart"
    BUISNES = "buisnes"

    TIKET_CHOISES = (
        (BUDGET, "Budget"),
        (STANDART, "Standart"),
        (BUISNES, "Buisnes")
    )


    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='ticket_purchases')
    category = models.CharField(max_length=15, choices=TIKET_CHOISES, default=STANDART)
    payment = models.DecimalField(max_digits=10, decimal_places=2,  null=True, blank=True)
    date = models.DateField(null=True)
    departure = models.ForeignKey(City, max_length=50, on_delete=models.CASCADE, related_name='tickets')

    def __str__(self):
        return f"Ticket Purchase for {self.city.title}"


class UserTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tickets")
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="purchased")

    def __str__(self) -> str:
        return f"{self.user.username} - {self.ticket.city.title}"
    

class CityImages(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="images", verbose_name="Город")
    image = models.ImageField("Картинка", upload_to="cities/", null=False)

    class Meta:
        verbose_name = "Картинка города"
        verbose_name_plural = "Картинки города"

    def __str__(self):
        return self.city.title
    

class PopularPlaces(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="places", verbose_name="Город")
    image = models.ImageField("Картинка", upload_to="populars/", null=False)
    title = models.CharField("Известное", max_length=100)
    content = models.TextField("Контент", null=True, blank=True)
    lat = models.FloatField("Широта", null=True, blank=True)
    lot = models.FloatField("Долгота", null=True, blank=True)

    class Meta:
        verbose_name = "известное"
        verbose_name_plural = "известные"
    
    def __str__(self):
        return self.city.title
    

class LocalPlaces(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="locals", verbose_name="Город")
    image = models.ImageField("Картинка", upload_to="cities/", null=False)
    title = models.CharField("Известное", max_length=100)
    content = models.TextField("Контент", null=True, blank=True)
    lat = models.FloatField("Широта", null=True, blank=True)
    lot = models.FloatField("Долгота", null=True, blank=True)

    class Meta:
        verbose_name = "локальное"
        verbose_name_plural = "локальные"
    
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
