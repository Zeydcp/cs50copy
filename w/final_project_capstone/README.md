# Restaurant Review App

This is a web application that allows users to browse restaurants, submit reviews, and interact with other users’ reviews through ratings and likes. Each restaurant has a dedicated page displaying its information, average user rating, image, and a list of user reviews. Logged-in users can write, edit, or delete their reviews, as well as like or unlike reviews submitted by others.

---

## 🚀 How to Run the Application

### Install dependencies

pip install -r requirements.txt

### Apply Migrations

python manage.py migrate

### Run the Development Server

python manage.py runserver

File Overview
Backend (Django)

    manage.py: Django’s command-line utility.

    restaurants_near_me/: Main Django app.

        models.py: Contains the models for Restaurant, Review, and review likes.

        views.py: Contains the logic for rendering restaurant pages and handling review CRUD operations and likes and deletes.

        urls.py: URL routes for views.

        templates/: HTML templates for rendering pages.

        static/restaurants_near_me/: JavaScript and CSS files for interactivity and styling.

Frontend

    templates/index.html: Displays restaurant info and review form.

    reviews.js: JavaScript file for review editing, deleting, star rendering, and confirmation dialogs.

    restaurant.js: JavaScript file used to render the homepage to request location and render the restaurants

    style.css: Optional styling overrides for stars, spacing, and form UI.

Distinctiveness and Complexity
Distinctiveness:

This project goes beyond a basic CRUD app by integrating dynamic JavaScript behaviors with Django-rendered content. It introduces user interactions such as:

    Live editing and deleting of reviews without refreshing the page.

    Interactive star rating components supporting a 0–4 scale.

    A heart (❤️) system for liking reviews, which modifies the weighting of the rating on the restaurant average rating.

    Custom radio buttons displayed as stars with no star meaning "0".

This interactivity makes it distinct from simple forms-based apps and showcases deeper integration between frontend and backend.
Complexity:

    Dynamic Star Rating System: Ratings are handled both visually with JavaScript and validated server-side via Django forms.

    Review Ownership and Access Control: Users can only edit/delete their own reviews, requiring backend logic tied to user sessions.

    Form Prefilling and DOM Synchronization: On edit, the form fields reflect current rating and text, dynamically toggled without reloading.

    Async Behavior: Deletes and edits are handled using fetch with JavaScript, along with confirmation dialogs, simulating modern SPA features.

    State Management: The frontend manages state consistency between static and editable forms, a non-trivial challenge in multi-review environments.

Together, these demonstrate both frontend fluency and backend robustness, especially in aligning user experience with secure backend logic.
Additional Information

    The app assumes users are authenticated. For full functionality, log in before interacting with reviews.

    Rating scale is set to 0–4 star ⭐️
