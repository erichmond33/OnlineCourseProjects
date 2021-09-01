document.addEventListener('DOMContentLoaded', function() {
    // Removing the button to make a post seeing as this is the post page
    document.querySelector("#advice").remove()
    document.querySelector("#new_post").remove()

    //Making a post
    document.querySelector('#post_form').onsubmit = function() {

        console.log(document.querySelector('#compose-body').value);

        fetch('/send', {
        method: 'POST',
        body: JSON.stringify({
            post: document.querySelector('#compose-body').value
        })
        })
        .then(response => response.json())
        .then(result => {
            // Print result
            console.log(result);
        }).then(document.querySelector("#all_posts").click());

        return false;
    }
});