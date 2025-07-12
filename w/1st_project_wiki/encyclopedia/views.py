from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.forms import Form, CharField, Textarea, ValidationError
from django.template import Template, Context
from random import choice

from . import util

from re import sub


class NewPageForm(Form):
    title = CharField(label="Page Title")
    content = CharField(widget=Textarea, label="")

    disallowed_items = util.list_entries()

    def clean_title(self):
        data = self.cleaned_data['title']
        if get_match(data) is not None:
            raise ValidationError("Page already exists")
        return data


class EditForm(Form):
    content = CharField(widget=Textarea, label="")

    def __init__(self, *args, initial_value=None, **kwargs):
        # Call the parent class's __init__ method
        super().__init__(*args, **kwargs)

        # Set the initial value based on the provided parameter
        if initial_value is not None:
            self.fields['content'].initial = initial_value


# Converts markdown to html
def converter(md):
    # Fix headings
    md = sub(r'## (.+)', r'<h2>\1</h2>', md)
    md = sub(r'# (.+)', r'<h1>\1</h1>', md)

    # Fix bold text
    md = sub(r'\*\*([^\*]+)\*\*', r'<strong>\1</strong>', md)

    # Fix unordered lists
    md = sub(r'\n((?:\* .+\n)*\* .+)', r'\n<ul>\1</ul>\n', md)
    md = sub(r'\* (.+)', r'<li>\1</li>', md)

    # Fix links
    md = sub(r'\[([^\[]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', md)

    # Fix paragraphs
    md = sub(r'\n{2,}(.+)', r'<p>\1</p>', md)

    return md


def template_renderer(md, name):
    context = {
        'md': md,
        'name': name
    }

    template = """
                {% extends 'encyclopedia/layout.html' %}
                {% block title %}
                    {{ name }}
                {% endblock %}
                {% block body %}
                    {{ md|safe }}
                <p class='pt-4'>
                    <a class='btn btn-primary' href="{% url 'edit_page' name=name %}" role='button'>Edit Page</a>
                <p>
                {% endblock %}
                """

    # Necessary to be able to extend layout.html
    template = Template(template)
    md = template.render(Context(context))

    return md


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


# Helper function
def get_match(result):
    return next((ent for ent in util.list_entries() if ent.lower() == result.lower()), None)


def entry(request, name: str):

    # Get content from page that you wanna edit
    content = util.get_entry(name)

    # Invalid url entry
    if content is None:
        return HttpResponseNotFound("Requested page was not found")

    # Convert markdown to html
    html = converter(content)

    # Add layout.html and edit button
    html = template_renderer(html, name)
    return HttpResponse(html)


def search(request):
    # Find search result
    result: str = request.GET.get('q')

    # Case insensitive matching if the whole result is present
    full_result = get_match(result)

    # Take to wiki page if full name entered
    if full_result in util.list_entries():
        return HttpResponseRedirect(reverse("wiki_entry", args=[full_result]))
    # Return list of suggestions with similar name
    else:
        return render(request, "encyclopedia/search.html", {
            "entries": [ent for ent in util.list_entries() if result.lower() in ent.lower()]
        })


def create(request):
    # Extract values from form
    if request.method == "POST":
        form = NewPageForm(request.POST)

        # Make sure data is valid
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            # Save value and take to the page just created
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("wiki_entry", args=[title]))

        # Return page with error message
        else:
            return render(request, "encyclopedia/create.html", {
                "form": form
            })

    # When page is reached through GET
    return render(request, "encyclopedia/create.html", {
        "form": NewPageForm()
    })


def edit(request, name):

    # Get content from page that you wanna edit
    content = util.get_entry(name)

    # Invalid entry to edit
    if content is None:
        return HttpResponseNotFound("Requested page was not found")

    # When save page is clicked
    if request.method == "POST":

        # Retrieve content entered
        form = EditForm(request.POST)

        # Save valid content
        if form.is_valid():
            content = form.cleaned_data["content"]

            util.save_entry(name, content)
            return HttpResponseRedirect(reverse("wiki_entry", args=[name]))

    # Page arrived at through GET
    return render(request, "encyclopedia/edit.html", {
        "title": name,
        "form": EditForm(initial_value=content)
    })


def random_entry(request):
    # Pull random value from list of entries
    name = choice(util.list_entries())

    # Redirect to the page with the name it pulled out
    return HttpResponseRedirect(reverse("wiki_entry", args=[name]))
