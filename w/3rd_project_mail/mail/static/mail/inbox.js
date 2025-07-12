document.addEventListener('DOMContentLoaded', function() {

    // Use buttons to toggle between views
    document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
    document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
    document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
    document.querySelector('#compose').addEventListener('click', () => compose_email(''));

    // By default, load the inbox
    load_mailbox('inbox');
});

function compose_email(email) {

    // Show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';
    document.querySelector('#email').style.display = 'none';

    // Get receiver
    const heading = document.querySelector("h2").innerHTML;

    // Clear out composition fields
    document.querySelector('#compose-recipients').value = email ? (heading === email.sender) ? email.recipients[0] : email.sender : '';
    document.querySelector('#compose-subject').value = email ? email.subject.includes("Re: ") ? email.subject : `Re: ${email.subject}` : '';
    document.querySelector('#compose-body').value = email ? `\n\nOn ${email.timestamp} ${email.sender} wrote:\n${email.body}` : '';

    document.querySelector('#compose-recipients').disabled = email ? true : false;
    document.querySelector('#compose-subject').disabled = email ? true : false;

    document.querySelector('#compose-form').onsubmit = function(e) {
        e.preventDefault();

        _recipients = document.querySelector('#compose-recipients').value;
        _subject = document.querySelector('#compose-subject').value;
        _body = document.querySelector('#compose-body').value;

        fetch('/emails', {
                method: 'POST',
                body: JSON.stringify({
                    recipients: _recipients,
                    subject: _subject,
                    body: _body
                })
            })
            .then(response => response.json())
            .then(result => {
                // Print result
                load_mailbox('sent');
            })
    };
};


function load_mailbox(mailbox) {

    // Show the mailbox and hide other views
    document.querySelector('#emails-view').style.display = 'block';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#email').style.display = 'none';

    // Show the mailbox name
    document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

    const container = document.createElement('div');
    container.id = 'containerID';
    container.classList.add("container", "vh-100");

    document.querySelector('#emails-view').append(container);


    fetch(`/emails/${mailbox}`)
        .then(response => response.json())
        .then(emails => {
            // Print emails
            emails.forEach(add_email);

            // ... do something else with emails ...
        })

};


// Add a new post with given contents to DOM
function add_email(contents) {

    const emailbutton = document.createElement('button');
    emailbutton.style.backgroundColor = "transparent";
    emailbutton.classList.add("btn-block", "border-0", "p-0", "m-0");

    emailbutton.addEventListener('click', () => load_email(contents.id));

    // Create new email display
    const [email, _sender, _subject, _timestamp] = Array(4).fill(null).map(() => document.createElement('div'));

    email.classList.add("row", "custom-hover-border", "rounded", "text-break");

    email.style.backgroundColor = (contents.read) ? "white" : "lightgrey";

    // Define elements and their content
    _sender.classList.add("col", "my-auto", "text-left");
    _sender.innerHTML = contents.sender.bold();

    _subject.classList.add("col", "my-auto", "text-left");
    _subject.innerHTML = contents.subject;

    _timestamp.classList.add("col", "my-auto", "text-right");
    _timestamp.innerHTML = contents.timestamp;
    _timestamp.style.color = "grey";

    email.append(_sender, _subject, _timestamp);
    emailbutton.append(email);

    // Add post to DOM
    document.querySelector('#containerID').append(emailbutton);
};


function load_email(id) {
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';

    fetch(`/emails/${id}`)
        .then(response => response.json())
        .then(email => {
            // Get receiver
            const heading = document.querySelector("h2").innerHTML;
            const archivebutton = document.querySelector('#archive');

            document.querySelector('#from').innerHTML = `<b>From: </b>${email.sender}`;
            document.querySelector('#to').innerHTML = `<b>To: </b>${email.recipients}`;
            document.querySelector('#subject').innerHTML = `<b>Subject: </b>${email.subject}`;
            document.querySelector('#timestamp').innerHTML = `<b>Timestamp: </b>${email.timestamp}`;

            document.querySelector('#reply').onclick = () => compose_email(email);

            archivebutton.style.display = (heading === email.recipients[0]) ? "block" : "none";
            archivebutton.innerHTML = email.archived ? "Unarchive" : "Archive";
            archivebutton.onclick = () => fetch(`/emails/${id}`, {
                    method: 'PUT',
                    body: JSON.stringify({
                        archived: !email.archived
                    })
                })
                .then(() => load_mailbox('inbox'))

            document.querySelector('#body').innerHTML = email.body.replaceAll('\n', '<br>');

            if (!email.read) {
                fetch(`/emails/${id}`, {
                    method: 'PUT',
                    body: JSON.stringify({
                        read: true
                    })
                })
            };


            document.querySelector('#email').style.display = 'block';

        })

};
