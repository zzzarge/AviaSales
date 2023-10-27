from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings



from .models import Country, City, Ticket, UserTicket, Comment
from django.contrib import messages
from .forms import UserUpdateForm, CommentCreationForm
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
    comments = city.comments.all()
   
    context = {
        "city": city,
        "cities": cities,
        "tickets": tickets,
        "comments": comments,
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

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            ticket = get_object_or_404(Ticket, pk=pk)
            UserTicket.objects.create(
                ticket=ticket,
                user=request.user
            )

            subject = 'Покупка билета'
            message = f'Здравствуйте {request.user.full_name}! Вас приветствует компания AviaSales. Вы успешно приобрели билет {ticket.city}\{ticket.departure} {ticket.category} ${ticket.payment}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [request.POST.get('email')]

            send_mail(subject, message, from_email, recipient_list)

            messages.success(request, 'Билет успешно куплен!')
            return redirect('base_view')

    else:
        form = UserUpdateForm()

    return render(request, 'buy_tickets.html', {'form': form, 'countries': countries})



@login_required
def write_comments(request, pk):
    city = City.objects.get(pk=pk)
    if request.method =="POST":
        form=CommentCreationForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner=request.user
            comment.city = city
            comment.save()
    return redirect("city_details", pk=city.pk)



@login_required
def delete_comment(request, pk):
    comment= Comment.objects.get(pk=pk)
    
    if comment not in request.user.comments.all():
        return redirect("city_details", pk=comment.city.pk)
    
    comment.delete()
    return redirect(request.META.get('HTTP_REFERER'))



# def london_city(requset):
#     return redirect ('london_city')


def twitter(request):
    twitter_url = 'https://twitter.com'

    return redirect(twitter_url)


def facebook(request):
    facebook_url = 'https://www.facebook.com'

    return redirect(facebook_url)


def linkedin(request):
    linkedin_url = 'https://www.linkedin.com'

    return redirect(linkedin_url)


def dribbble(request):
    dribbble_url = 'https://dribbble.com'

    return redirect(dribbble_url)


def dubai_hotel(request):
    dubai_hotel_url = 'https://www.booking.com/city/ae/dubai.ru.html?aid=319915;gad_source=1;gclid=CjwKCAjwv-2pBhB-EiwAtsQZFGQbQeetSQBfCzbXdmVRzH0IpMJk_RFhjQ9dDR3lDpQaGnuAkXZ9BhoCwOwQAvD_BwE;ws=;label=dubai-53SwLmJnlUKslKxEnvKBiAS408282807088%3Apl%3Ata%3Ap1920%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-146342137270%3Akwd-76067340%3Alp1009827%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YdQLqCSGZAFDHKNAytkZCCU'

    return redirect(dubai_hotel_url)


def italy_hotel(request):
    italy_hotel_url = 'https://www.booking.com/country/it.ru.html?aid=319915;label=it-LD5zJ95YjAMGxndFJYtyagS390408492429:pl:ta:p1:p2:ac:ap:neg:fi:tiaud-146342137270:kwd-27993753:lp1009827:li:dec:dm:ppccp=UmFuZG9tSVYkc2RlIyh9YdQLqCSGZAFDHKNAytkZCCU;ws=&gad_source=1&gclid=CjwKCAjwv-2pBhB-EiwAtsQZFOpiBJEB83oNKiewPL8QWG2THq-CShwcCsOVwCFknQxBIBt4z5RACRoCfFcQAvD_BwE'

    return redirect(italy_hotel_url)


def velikobritania_hotel(request):
    velikobritania_hotel_url = 'https://www.booking.com/country/gb.ru.html?aid=319915;label=gb-bpMfepe7jTKkQlcFTmHzygS390518231406:pl:ta:p1:p2260.000:ac:ap:neg:fi:tiaud-297601666515:kwd-26351628348:lp1009827:li:dec:dm:ppccp=UmFuZG9tSVYkc2RlIyh9YdQLqCSGZAFDHKNAytkZCCU;ws=&gad_source=1&gclid=CjwKCAjwv-2pBhB-EiwAtsQZFE0dTBxWDD24a4jor-FRED52niqY-xgXuEIQGI1h9GAShmdHlef97xoCO8YQAvD_BwE'

    return redirect(velikobritania_hotel_url)


def turkey_hotel(request):
    turkey_hotel_url = 'https://www.booking.com/country/tr.html?aid=303948;label=tr-Wrqv5JBd0kQcLX5FyoNplgS182991160456:pl:ta:p1:p2:ac:ap:neg:fi:tiaud-297601666515:kwd-30578743:lp1009827:li:dec:dm:ppccp=UmFuZG9tSVYkc2RlIyh9Yf5EcukO1MOGLSSAuId8ToA;ws=&gad_source=1&gclid=CjwKCAjwv-2pBhB-EiwAtsQZFOiq7tJLPOG2JzR4LQUyHWhouLk7FzfyDGrhhFJgqQCgy1Ot3NJAJBoCZb0QAvD_BwE'

    return redirect(turkey_hotel_url)


def seoul_hotel(request):
    seoul_hotel_url = 'https://www.booking.com/city/kr/seoul.ru.html?aid=319915;label=seoul-l4KVLHvQoKnbdjsSyUA_EwS390216934005:pl:ta:p1:p2:ac:ap:neg:fi:tiaud-146342137270:kwd-307287843974:lp1009827:li:dec:dm:ppccp=UmFuZG9tSVYkc2RlIyh9YdQLqCSGZAFDHKNAytkZCCU;ws=&gad_source=1&gclid=CjwKCAjwv-2pBhB-EiwAtsQZFDlmP0Qtu25hau3cKfYnsF3Vo6PleW6DbYy4xDxmaJdECTEiG-L1VRoCA9cQAvD_BwE'

    return redirect(seoul_hotel_url)


def velikobritania_country(request):
    velikobritania_country_url = 'http://127.0.0.1:8000/country/details/1'

    return redirect(velikobritania_country_url)


def dubai_city(request):
    dubai_city_url = 'http://127.0.0.1:8000/city/details/20'

    return redirect(dubai_city_url)


def italy_country(request):
    italy_country_url = 'http://127.0.0.1:8000/country/details/5'

    return redirect(italy_country_url)


def seoul_city(request):
    seoul_city_url = 'http://127.0.0.1:8000/city/details/3'

    return redirect(seoul_city_url)


def turkey_country(request):
    turkey_country_url = 'http://127.0.0.1:8000/country/details/2'

    return redirect(turkey_country_url)