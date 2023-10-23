from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required



from .models import Country, City, Ticket, UserTicket
from django.contrib import messages
from .forms import UserUpdateForm
import requests


def base_view(request):
    countries = Country.objects.all()[:6]
    cities = City.objects.all()

    context = {
        "countries": countries,
        "cities": cities,
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
    cities = City.objects.all().order_by("title")
    tickets = city.ticket_purchases.all()
   
    context = {
        "city": city,
        "cities": cities,
        "tickets": tickets,
    }

    return render(request, "city_details.html", context)


def search_tickets(request):

    print(request.GET, "\n\n\n\n")

    departure_pk = request.GET.get("departure")
    departure = City.objects.get(pk=departure_pk)

    category = request.GET.get("category")

    city_pk = request.GET.get("city")
    city = City.objects.get(pk=city_pk)

    date = request.GET.get("date").split("/")
    date = f"{date[2]}-{date[0]}-{date[1]}"

    tickets = Ticket.objects.filter(departure=departure, date=date, city=city).order_by("category")

    context = {
        "tickets": tickets,
        "city": city
    }

    return render(request, "tickets_list.html", context)
   



def pricing_view(request):
    tickets = Ticket.objects.all()

    context = {
        "tickets": tickets
    }

    return render(request, "price.html", context)

@login_required
def buy_ticket(request, pk):
    url = "https://restcountries.com/v3.1/all"

    response = requests.get(url=url)

    countries = [country['name']['official'] for country in response.json()]

    print(request.POST, "\n\n\n")
    form = UserUpdateForm()

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            ticket = get_object_or_404(Ticket, pk=pk)
            UserTicket.objects.create(
                ticket = ticket,
                user=request.user
            )

            messages.success(request, 'Билет успешно куплен!')
            return redirect('base_view')  
        
   
    
    return render(request, 'buy_tickets.html', {'form': form, "form": form, 'countries': countries})