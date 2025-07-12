document.addEventListener('DOMContentLoaded', function() {

    const reviewList = document.getElementById('review-list');

    reviewList.addEventListener('click', function(e) {
        // Check if the clicked element is an edit button
        if (e.target.classList.contains('edit-review-btn')) {

            // Hide all static reviews and show their corresponding edit forms
            const visibleEditable = reviewList.querySelector('.editable-review:not(.d-none)');
            if (visibleEditable) {
                let staticReview = visibleEditable.previousElementSibling;
                staticReview.classList.remove('d-none');
                visibleEditable.classList.add('d-none');
            };

            staticReview = e.target.closest('.static-review');
            staticReview.classList.add('d-none');
            const edit = staticReview.nextElementSibling;
            edit.classList.remove('d-none');

            const textArea = edit.querySelector('textarea');
            textArea.focus();
        } else if (e.target.classList.contains('delete-review-btn')) {
            const isConfirmed = confirm('Are you sure you want to delete this?');
            if (!isConfirmed) return;

            const button = e.target;
            const reviewID = button.dataset.reviewid;

            fetch(`delete/`, {
                    method: 'POST',
                    body: JSON.stringify({
                        id: reviewID
                    })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        const restaurant = data.restaurant;
                        const p = document.querySelector(`.span-${restaurant.id}`).parentNode;
                        document.querySelectorAll(`.span-${restaurant.id}`).forEach(span => span.remove());

                        p.innerHTML += getStarHTML(restaurant.rating, restaurant.id);

                        button.closest(`.card.mb-2`).remove();
                    }
                })


        } else if (e.target.classList.contains('like')) {
            const button = e.target;
            const reviewID = button.dataset.reviewid;

            fetch(`like/`, {
                    method: 'POST',
                    body: JSON.stringify({
                        id: reviewID
                    })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        // Toggle heart class based on like status
                        if (data.liked) {
                            button.classList.remove('heart');
                        } else {
                            button.classList.add('heart');
                        }

                        const review = data.review;

                        // Update like count
                        const countCell = button.closest('tr').querySelector('td.text-secondary');
                        countCell.textContent = review.count;

                        const p = document.querySelector(`.span-${review.restaurant_id}`).parentNode;
                        document.querySelectorAll(`.span-${review.restaurant_id}`).forEach(span => span.remove());

                        p.innerHTML += getStarHTML(review.restaurant_rating, review.restaurant_id);
                    }
                })
        }
    });

    const cancelButtons = document.querySelectorAll('.cancel-review-btn');
    cancelButtons.forEach(function(btn) {
        btn.onclick = () => {
            const editable = btn.closest('.editable-review');
            editable.classList.add('d-none');
            editable.previousElementSibling.classList.remove('d-none');
        };
    });

    const editForms = document.querySelectorAll(`.edit-form`);

    editForms.forEach(Energize);

    const reviewForm = document.getElementById('review-form');
    reviewForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData(reviewForm);

        fetch(window.location.pathname, {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Add the new review to the top of the list
                    const reviewList = document.getElementById('review-list');
                    const review = data.review;
                    const rest = data.rest;

                    const div = document.createElement('div');
                    div.classList.add('card', 'mb-2');

                    // Edit button (if the review belongs to current user)
                    const editButton = document.createElement('button');
                    editButton.className = 'btn btn-sm btn-outline-primary edit-review-btn';
                    editButton.setAttribute('data-reviewid', review.id);
                    editButton.type = "button";
                    editButton.textContent = 'Edit';

                    // Edit button (if the review belongs to current user)
                    const deleteButton = document.createElement('button');
                    deleteButton.className = 'btn btn-sm btn-danger delete-review-btn';
                    deleteButton.setAttribute('data-reviewid', review.id);
                    deleteButton.type = "button";
                    deleteButton.textContent = 'Delete';

                    const likeButton = `
                    <table>
                        <tr>
                            <td>
                                <button class="btn p-0 mb-1 heart" type="button">❤️</button>
                            </td>
                            <td class="text-secondary">0</td>
                        </tr>
                    </table>
                `;

                    div.innerHTML = `
                    <div class="card-body">
                        <div class="static-review">
                            <h5 class="card-title mb-0">
                                ${getStarHTML(review.rating, review.id)}
                            </h5>
                            <p class="card-text" id="${review.id}">${review.review}</p>
                        </div>
                        ${rest.form}
                        ${likeButton}
                        <small class="text-muted">By ${rest.user}</small>
                    </div>
                `;

                    const p = document.querySelector(`.span-${review.restaurant_id}`).parentNode;
                    document.querySelectorAll(`.span-${review.restaurant_id}`).forEach(span => span.remove());

                    p.innerHTML += getStarHTML(review.restaurant_rating, review.restaurant_id);

                    const whitespaceNode = document.createTextNode(' ');

                    // Insert the button after creating the HTML
                    div.querySelector('.card-title').append(editButton);
                    editButton.after(whitespaceNode);
                    div.querySelector('.card-title').append(deleteButton);

                    const cancel = div.querySelector('.cancel-review-btn');
                    cancel.onclick = () => {
                        const editable = cancel.closest('.editable-review');
                        editable.classList.add('d-none');
                        editable.previousElementSibling.classList.remove('d-none');
                    };

                    reviewList.prepend(div);
                    Energize(reviewList.querySelector('.edit-form'));
                    reviewForm.reset();
                } else {
                    alert("There was an error saving your review.");
                }
            });
    });
});


function Energize(form) {
    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData(form);

        const reviewID = form.dataset.reviewid;
        const selectedReview = formData.get(`${reviewID}-review`);

        const selectedRating = formData.get(`${reviewID}-rating`) ?? '0'; // Get selected rating value
        const originalRating = form.dataset.rating;

        const bodyDiv = document.querySelector(`#${CSS.escape(reviewID)}`);
        const originalReview = bodyDiv.innerHTML; // Get original value from data attribute

        if (selectedReview === originalReview && selectedRating === originalRating) {
            console.log('Rating unchanged. No request sent.');
            const editable = form.closest('.editable-review');
            editable.classList.add('d-none');
            editable.previousElementSibling.classList.remove('d-none');
            return;
        }

        formData.append('_method', 'PUT');
        formData.append('id', reviewID);

        fetch(window.location.pathname, {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const review = data.review;

                    form.dataset.rating = review.rating;

                    // Review rating
                    const card = document.querySelector(`.span-${review.id}`).parentNode;
                    document.querySelectorAll(`.span-${review.id}`).forEach(span => span.remove());

                    card.innerHTML = getStarHTML(review.rating, review.id) + card.innerHTML;

                    // Average rating
                    const p = document.querySelector(`.span-${review.restaurant_id}`).closest("p");
                    document.querySelectorAll(`.span-${review.restaurant_id}`).forEach(span => span.remove());

                    p.innerHTML += getStarHTML(review.restaurant_rating, review.restaurant_id);

                    bodyDiv.innerHTML = review.review;

                    const editable = form.closest('.editable-review');
                    editable.classList.add('d-none');
                    const staticReview = editable.previousElementSibling;
                    staticReview.classList.remove('d-none');

                    if (!staticReview.querySelector(`.espan-${review.id}`)) {

                        const edited = document.createElement('span');
                        edited.className = `text-secondary espan-${review.id}`;
                        edited.textContent = 'Edited';
                        staticReview.insertBefore(edited, staticReview.querySelector('.card-text'));

                    };
                }
            })
    });
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



function likeReview(button, reviewID) {
    const number = button.parentNode.nextElementSibling;

    const url = window.location.pathname;

    fetch(url, {
            method: 'POST',
            body: JSON.stringify({
                id: reviewID
            })
        })
        .then(response => response.json())
        .then(response => {
            if (response.count != null) {
                const likeCount = response.count;
                if (response.like) {
                    button.classList.remove('heart');
                } else {
                    button.classList.add('heart');
                }
                number.innerHTML = likeCount;
            }
        })
};
