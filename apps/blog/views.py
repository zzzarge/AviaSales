from django.shortcuts import render, redirect, get_object_or_404



from .models import Country, City, Ticket

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

def city_details(request, pk):
    city = get_object_or_404(City, pk=pk)
    cities = City.objects.all()
    tickets = city.ticket_purchases.all()
   
    context = {
        "city": city,
        "cities": cities,
        "tickets": tickets,
    }

    return render(request, "city_details.html", context)



def pricing_view(request):
    tickets = Ticket.objects.all()

    context = {
        "tickets": tickets
    }

    return render(request, "price.html", context)


# def checce(request, choice_id, city_id ):
#     city = get_object_or_404(City, pk = city_id)

#     form = ChoiceForm()
#     if form.is_valid():
#         if form.low == True:
#             city.price = 500

#         elif form.bissines == True:
#             city.price = 50000
        
#         else:
#             pass
