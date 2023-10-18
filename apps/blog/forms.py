from django import forms
from .models import UserTicket

from django.core.exceptions import ValidationError

import datetime

class UserTicketCreationForm(forms.Form):

    class Meta:
        model=UserTicket
        fields = (
            "departure",
            "ticket",
            "date",
        )

    def clean_date(self):
        date = self.cleaned_data.get("date")

        if date <= datetime.date.today():
            raise ValidationError("Выберите будущую дату!")

        return date

