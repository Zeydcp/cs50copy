const data = document.currentScript.dataset;
let followers = parseInt(data.followers, 10);

document.addEventListener('DOMContentLoaded', function() {

    const authenticated = (data.authenticated === 'True') ? true : false;
    const currentUser = data.currentUser;
    const pageUser = data.pageUser;
    const following = (data.following === 'True') ? true : false;


    if (authenticated && currentUser != pageUser) {
        const div = document.createElement('div');
        div.classList.add('col');

        const button = document.createElement('button');
        button.type = 'button';
        button.id = 'follow';
        button.classList.add('btn', 'btn-primary');

        button.innerHTML = following ? "Unfollow" : "Follow";
        button.onclick = () => toggle(pageUser);

        div.append(button);
        document.querySelector('#page_row').append(div);
    }

});


function toggle(pageUser) {
    const button = document.querySelector('#follow');

    fetch(`/profile/${pageUser}`, {
            method: 'POST',
            body: JSON.stringify({
                type: "follow"
            })
        })
        .then(response => response.json())
        .then(response => {
            const followers = response.count;
            button.innerHTML = (response.follow) ? "Unfollow" : "Follow";
            document.querySelector('#followers').innerHTML = `${followers} followers`;
        })

};
