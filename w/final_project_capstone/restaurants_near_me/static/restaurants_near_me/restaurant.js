document.addEventListener('DOMContentLoaded', function() {
    navigator.geolocation.getCurrentPosition(function(position) {
        const lat = position.coords.latitude;
        const lng = position.coords.longitude;
        // Send lat/lng to your Django view via AJAX or a form

        fetch(`/near_me`, {
                method: 'POST',
                body: JSON.stringify({
                    latitude: lat,
                    longitude: lng
                })
            })
            .then(response => response.json())
            .then(restaurants => {
                restaurants.forEach(add_restaurant);
            })
    })
});

function add_restaurant(restaurant) {

    const anchor = document.createElement('a');
    anchor.href = `/${restaurant.id}`;
    anchor.classList.add("text-decoration-none", "text-reset");

    const div = document.createElement('div');
    div.classList.add("row", "custom-hover-border", "rounded", "text-break", "mb-3", "text-break", "h-25");
    const div1 = document.createElement('div');
    div1.classList.add("col-2", "text-center");
    div1.id = 'index_div';

    if (restaurant.image !== null) {
        const img = document.createElement('img');
        img.src = restaurant.image;
        img.alt = restaurant.name;
        div1.appendChild(img)
    }

    const div2 = document.createElement('div');
    div2.classList.add("col-4", "my-auto");

    const title = document.createElement('h4');
    title.innerHTML = restaurant.name;
    div2.appendChild(title);

    const div3 = document.createElement('div');
    div3.classList.add("col-3", "my-auto");

    const div4 = document.createElement('div');
    div4.classList.add("col-3", "my-auto");

    const rating = document.createElement('p');

    rating.innerHTML = getStarHTML(restaurant.rating, restaurant.id);

    div4.appendChild(rating);

    div.append(div1, div2, div3, div4);
    anchor.appendChild(div);

    const container = document.querySelector('.container');
    container.appendChild(anchor);
}

function getStarHTML(rating, id) {
    let stars = '';
    for (let i = 1; i <= 4; i++) {
        if (i <= rating) {
            stars += `<span class="span-${id}">⭐</span>`; // filled star
        } else {
            stars += `<span class="span-${id} unpicked">⭐</span>`; // empty star
        }
    }
    return stars;
}
