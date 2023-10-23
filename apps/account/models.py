from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    MALE = "мужской"
    FAMALE = "женский"
    OTHER = "другое"

     
    GENDER_CHOICES = [
        (MALE, 'Мужской'),
        (FAMALE, 'Женский'),
        (OTHER, 'Другое')
    ]

    email = models.EmailField("Email", unique=True, null=False)
    image = models.ImageField("Аватар", upload_to="account/", default="account/default_avatar.png", blank=True)
    date_of_birth = models.DateField("Дата рождения", null=True, blank=True)
    about = models.TextField("О себе", blank=True)
    citizenship = models.CharField(max_length=100, null=True, blank=True)
    document_id = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    country_code = models.CharField(max_length=5, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)



    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
    
    @property
    def full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()
    


class Country(models.Model):
    name = models.CharField("Name", max_length=100)
    flag = models.ImageField("Флаг", upload_to="flags/")

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    def __str__(self):
        return self.name
    


