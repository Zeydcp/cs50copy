document.addEventListener('DOMContentLoaded', function() {
    // Select all buttons
    document.querySelectorAll('button').forEach(button => {
        button.onclick = () =>
            button.classList.contains('btn-link') ?
            editPost(button, button.dataset.post) :
            likePost(button, button.dataset.post);
    });
});


function editPost(button, postID) {
    const bodyDiv = document.querySelector(`#${CSS.escape(postID)}`);
    const body = bodyDiv.innerHTML;

    const formGroup = document.createElement('div');
    formGroup.classList.add('form-group');
    formGroup.id = 'formPost';

    const textArea = document.createElement('textarea');
    textArea.classList.add('form-control');
    textArea.value = body;
    textArea.id = 'currentPost';
    textArea.rows = 1;

    formGroup.append(textArea);
    bodyDiv.parentNode.replaceChild(formGroup, bodyDiv);
    textArea.focus();
    button.style.display = 'none';

    const formGroup2 = document.createElement('div');
    formGroup2.classList.add('form-group');

    const input = document.createElement('button');
    input.classList.add('btn', 'btn-primary');
    input.type = 'submit';
    input.innerHTML = 'Save';
    input.onclick = () => saveEdit(button, formGroup, formGroup2, postID, textArea);
    formGroup2.append(input);
    formGroup.parentNode.insertBefore(formGroup2, formGroup.nextSibling);
};


function saveEdit(button, formGroup, formGroup2, postID, textArea) {
    const body = textArea.value;

    var url = window.location.pathname;

    fetch(url, {
            method: 'PUT',
            body: JSON.stringify({
                id: postID,
                body: body
            })
        })
        .then(response => response.json())
        .then(date => {
            button.style.display = 'block';

            const bodyDiv = document.createElement('div');
            bodyDiv.id = postID;
            bodyDiv.innerHTML = body;
            formGroup.parentNode.replaceChild(bodyDiv, formGroup);

            time = formGroup2.nextElementSibling;

            const dateObj = new Date(date.timestamp);

            // Get month abbreviation and add a period
            const monthAbbr = dateObj.toLocaleString("en-US", {
                month: "short"
            }) + "."; // "Feb."

            // Format the rest of the date
            const formattedDate = `${monthAbbr} ${dateObj.getDate()}, ${dateObj.getFullYear()}`;

            // Format time
            const formattedTime = dateObj.toLocaleTimeString("en-US", {
                hour: "numeric",
                minute: "2-digit",
                hour12: true
            }).replace("AM", "a.m.").replace("PM", "p.m.");

            // Combine date and time
            const finalFormat = `${formattedDate}, ${formattedTime}`;

            time.innerHTML = finalFormat;
            formGroup2.remove();
        })
};


function likePost(button, postID) {
    const number = button.parentNode.nextElementSibling;

    const url = window.location.pathname;

    fetch(url, {
            method: 'POST',
            body: JSON.stringify({
                id: postID
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
