from django.urls import path


from .views import (
    register_view,
    login_view,
    logout_view,
    update_profile_view

)

app_name = "account"

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("profile/update/", update_profile_view, name="update"),
]
