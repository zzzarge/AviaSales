from django import forms
from .models import User, Comment


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "citizenship",
            "document_id",
            "gender",
            "country_code",
            "phone_number",
        ]


class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)