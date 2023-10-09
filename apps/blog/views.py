from django.shortcuts import render, redirect, get_object_or_404



from .models import Country

def base_view(request):
    countries = Country.objects.all()[:6]

    context = {
        "countries": countries
    }
    
    return render(request, "index.html", context)


def country_details(request, pk):
    country = get_object_or_404(Country, pk=pk)
   
    context = {
        "country": country,
    }

    return render(request, "country_details.html", context)