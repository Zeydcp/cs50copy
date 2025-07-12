from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseForbidden, HttpResponseBadRequest, QueryDict
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from json import loads
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
from requests import get
from django.template.loader import render_to_string

from .models import User, Restaurant, Review, NewReviewForm, Like

# Create your views here.


def index(request):

    # Authenticated users view their inbox
    if request.user.is_authenticated:
        return render(request, "restaurants_near_me/index.html")

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))


@csrf_exempt
@login_required
def like(request):
    if request.method == "POST":
        data = loads(request.body)
        id = data.get('id')
        review = get_object_or_404(Review, id=id)
        if review.user == request.user:
            return JsonResponse({
                'success': False
            })
        elif review.id in request.user.reviews_liked:
            Like.objects.get(liker=request.user, review=review).delete()
            liked = False
        else:
            Like.objects.create(liker=request.user, review=review)
            liked = True

        print(review.serialize())

        return JsonResponse({
            'success': True,
            'liked': liked,
            'review': review.serialize()
        })

    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=405)


@csrf_exempt
@login_required
def delete(request):
    if request.method == "POST":
        data = loads(request.body)
        id = data.get('id')

        review = get_object_or_404(Review, id=id)
        if review.user == request.user:
            restaurant = review.place
            review.delete()

            return JsonResponse({
                'success': True,
                'restaurant': restaurant.serialize()
            })

    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=405)


@csrf_exempt
@login_required
def page(request):

    data = loads(request.body)
    lat = data.get('latitude')
    lng = data.get('longitude')

    if not lat or not lng:
        return JsonResponse({'error': 'Missing coordinates'}, status=400)

    # Get 10 closest restaurants
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{lat},{lng}",
        "rankby": "distance",
        "type": "restaurant",
        "key": settings.API_KEY
    }

    response = get(url, params=params)
    results = response.json().get("results")[:5]

    restaurants: list[Restaurant] = []
    for item in results:
        name = item.get('name')
        place_id = item.get('place_id')

        photo_url = None

        if item.get('photos'):
            photo_reference = item['photos'][0].get('photo_reference')
            photo_url = (
                f"https://maps.googleapis.com/maps/api/place/photo"
                f"?maxwidth=400"
                f"&photo_reference={photo_reference}"
                f"&key={settings.API_KEY}"
            )

        defaults = {}

        if photo_url:
            defaults['photo_url'] = photo_url

        restaurant, _ = Restaurant.objects.get_or_create(
            place_id=place_id,
            name=name,
            defaults=defaults
        )
        restaurants.append(restaurant)

    return JsonResponse([restaurant.serialize() for restaurant in restaurants], safe=False)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "restaurants_near_me/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "restaurants_near_me/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "restaurants_near_me/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
        except IntegrityError:
            return render(request, "restaurants_near_me/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "restaurants_near_me/register.html")


@csrf_exempt
@login_required
def restaurant(request, id):
    restaurant: Restaurant = get_object_or_404(Restaurant, place_id=id)

    reviews = restaurant.reviews.all().order_by('-id')
    review_forms = [NewReviewForm(instance=review, prefix=str(review.id)) for review in reviews]
    review_data = list(zip(reviews, review_forms))

    if request.POST.get('_method') == 'PUT':
        review_id = request.POST.get('id')
        review = get_object_or_404(Review, id=review_id, user=request.user.id)

        form = NewReviewForm(request.POST, instance=review, prefix=str(review_id))

        if form.is_valid():
            review = form.save(commit=False)
            review.edited = True
            review.save()

            return JsonResponse({
                'success': True,
                'review': review.serialize()
            })
        else:
            print(form.errors)
            return JsonResponse({'success': False})

    elif request.method == 'POST':
        form = NewReviewForm(request.POST)

        if form.is_valid():
            review: Review = form.save(commit=False)
            review.user = request.user
            review.place = restaurant
            review.save()

            # Render just the form HTML as a string
            form_html = render_to_string('restaurants_near_me/review_form.html', {
                'review': review,
                'review_form': NewReviewForm(instance=review, prefix=review.id)
            }, request=request)

            return JsonResponse({
                'success': True,
                'review': review.serialize(),
                'rest': {
                    'user': request.user.username,
                    'form': form_html
                }
            })
        else:
            return JsonResponse({'success': False})

    return render(request, 'restaurants_near_me/restaurant.html', {
        'restaurant': restaurant.serialize(),
        'review_data': review_data,
        'first_form': NewReviewForm
    })
