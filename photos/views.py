from .models import Category
from django.shortcuts import render , redirect
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def index(request):
    return render (request ,'index.html')

def photos_today(request):
    date = dt.date.today()
     # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    return render (request, 'all-photos/today-photos.html' , {'date': date})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day


def past_days_photos(request,past_date):
    try:
    # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photos_of_day)

    return render(request, 'all-photos/past-photos.html', {"date": date})
def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Category.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"category": searched_categories})

    else:
        message = "You haven't searched for any category"
        return render(request, 'all-photos/search.html',{"message":message})
