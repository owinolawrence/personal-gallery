from .models import Category,Image
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
        searched_category = Category.search_by_category(search_term)
        search_by_category=Image.search_by_category(searched_category)

        if searched_category:

            message = f"{search_term}"

            return render(request, 'all-photos/search.html',{"message":message,"category": searched_category})

    else:
        message = "You haven't searched for any category"
        return render(request, 'all-photos/search.html',{"message":message})

def photo(request):
    photo = Photo.get_all()
    return render(request, 'all-photos/images.html', {"image":image })

def detail(request, image_id):
    image = Image.objects.get(id = image_id)
    return render(request, 'all-photos/details.html', {"image":image })

def location(request, country):
    location = Location.objects.get(id =country)
    return render(request, 'all-photos/location.html', {"image":image })

def admin_dashboard(request):
    admin = Admin

def category(request,category_id):
    try:
        category = category.objects.get(id = category_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/category.html", {"category":category})










    
