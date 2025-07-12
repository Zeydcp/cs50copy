from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.forms import ModelForm, NumberInput, Textarea, Select, TextInput, FileInput

from .models import User, Listing


class NewListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'image', 'price', 'category']

        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Title'
            }),
            'description': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'Description',
            }),
            'image': FileInput(attrs={
                'required': False,
                'class': 'form-control',
                'type': "file"
            }),
            'price': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Price'
            }),
            'category': Select(attrs={
                'class': 'form-control'
            })
        }


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def create_listing(request):
    if request.method == "POST":

        form = NewListingForm(request.POST)
        # Make sure data is valid
        if form.is_valid():
            title = request.POST["title"]
            description = request.POST["description"]
            image = request.FILES.get("image")
            price = request.POST["price"]
            category = request.POST.get("category")

            listing = Listing(title=title, description=description, image=image, price=price, seller=request.user, category=category)
            listing.save()

            return HttpResponseRedirect(reverse("index"))

        else:
            return render(request, "auctions/create_listing.html", {
                "form": form
            })
    else:
        return render(request, "auctions/create_listing.html", {
            "form": NewListingForm()
        })


def listing(request, id):
    listing_obj = Listing.objects.all().filter(id=id).first()
    if listing_obj.active:
        if request.method == "POST":
            if float(request.POST["bid"]) > listing_obj.price:
                listing_obj.price = float(request.POST["bid"])
                listing_obj.save()
                
        return render(request, "auctions/listing.html", {
            "listing": listing_obj
        })

    return render(request, "auctions/error.html")
