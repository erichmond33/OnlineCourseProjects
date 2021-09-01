document.addEventListener('DOMContentLoaded', function() {
    // Advice animation
    if (document.URL)
    document.querySelector("#advice").addEventListener('animationend', () => {
        document.querySelector("#advice").remove()
    });
    
    load_feed()
});

function load_feed() {


    //Fetching the mofuckin feed
    fetch('/feed')
  .then(response => response.json())
  .then(feed => {
      // Print emails
      console.log(feed);

      //The parent to all of this
      var all_posts = document.createElement("div");
      all_posts.setAttribute("id", "all_posts")
      document.querySelector(".container").appendChild(all_posts);

      var profile = document.createElement("div");
      profile.setAttribute("id", "profile");
      document.querySelector(".container").appendChild(profile);

      // ... do something else with emails ...
      for (post in feed) {

        //Creating the feed elements
        var wrapper = document.createElement("div");
        wrapper.setAttribute("id", "wrapper");

        var user = document.createElement("div");
        user.setAttribute("id", "user");
        
        var userlink = document.createElement("button");
        userlink.setAttribute("id", "userlink");
        userlink.setAttribute("type", "button" );
        userlink.setAttribute("value", `${feed[post].user_id}`)
        userlink.setAttribute("class", "btn btn-danger btn-sm");
        user.appendChild(userlink);
        userlink.innerHTML = feed[post].user_name;

        var body = document.createElement("div");
        body.setAttribute("id", "body");
        body.appendChild(document.createElement("p"));
        body.children[0].setAttribute("id", "body_content");
        body.children[0].innerHTML = feed[post].body;
        body.appendChild(document.createElement("p"));
        body.children[1].setAttribute("id", "timestamp");
        body.children[1].innerHTML = feed[post].timestamp
        body.appendChild(document.createElement("p"));
        body.children[2].innerHTML = feed[post].id;
        body.children[2].style.display = "none";

        var likes = document.createElement("div");
        likes.setAttribute("id", "likes");
        likes.appendChild(document.createElement("div"));
        likes.children[0].setAttribute("id", "likes_icon");
        likes.children[0].innerHTML = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"20\" height=\"20\" fill=\"currentColor\" class=\"bi bi-heart-fill\" viewBox=\"0 0 16 16\"><path fill-rule=\"evenodd\" d=\"M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z\"/></svg>";
        likes.appendChild(document.createElement("button"));
        likes.children[1].setAttribute("id", "edit");
        likes.children[1].setAttribute("class", "btn btn-danger btn-sm, edit");
        likes.children[1].innerHTML = "Edit";
        if (document.querySelector("#java_username").innerHTML != userlink.innerHTML) {
            likes.children[1].style.visibility = "hidden";
        }
        likes.appendChild(document.createElement("div"));
        likes.children[2].innerHTML = feed[post].likes;
        likes.children[2].setAttribute("id", "num_likes");



        wrapper.appendChild(user);
        wrapper.appendChild(body);
        wrapper.appendChild(likes);
        all_posts.appendChild(wrapper);
        all_posts.appendChild(document.createElement("hr"));   
        
        

        //Like a post
        likes.addEventListener("click", function() {

            var tar = event.target.parentNode;

            //ensuring we always click onto the same target
            if (tar.tagName != "DIV") {
                tar = tar.parentNode.parentNode
            }

            id = tar.parentNode.children[1].children[2].innerHTML;


            fetch(`/like/${id}`, {
            method: 'PUT',})
            .then(response => response.json())
            .then(response => {

                tar.children[2].innerHTML = response.likes;
            


            })    
            
            

        })



        //EDIT A POST
        likes.children[1].addEventListener("click", function() {

            var tar = event.target.parentNode.parentNode.children[1];
            var id = tar.children[2].innerHTML;
            //Holy shit how does this work
            console.log(tar);
            console.log(`ID: ${id}`);

            //Clear/prepare the body
            tar.innerHTML = "";
            tar.setAttribute("class", "container");

            //Create the edit elements
            form = document.createElement("form");
            form.setAttribute("id", "edit_form");
            tar.appendChild(form);
            form.appendChild(document.createElement("textarea"));
            form.appendChild(document.createElement("div"));
            form.children[0].setAttribute("id", "edit_text");
            form.children[0].setAttribute("class", "form-control");
            form.children[0].setAttribute("rows", "5");
            form.children[1].appendChild(document.createElement("a"));
            form.children[1].setAttribute("id", "link_div");
            form.children[1].children[0].setAttribute("href", "#");
            form.children[1].children[0].setAttribute('id', 'edit_submit');
            form.children[1].children[0].innerHTML = "+";
            //form.children[1].setAttribute("id", "edit_button");

            console.log(form.children[0].value);


            form.children[1].addEventListener("click", function() {


                fetch(`/edit/${id}`, {
                    method: 'PUT',
                    body: JSON.stringify({
                    content: form.children[0].value
                    })})
                    .then(response => response.json())
                    .then(response => {

                        console.log(response.post)

                        tar.innerHTML = "";
                    
                        tar.appendChild(document.createElement("p"));
                        tar.children[0].setAttribute("id", "body_content");
                        tar.children[0].innerHTML = response.post;
                        tar.appendChild(document.createElement("p"));
                        tar.children[1].setAttribute("id", "timestamp");
                        tar.children[1].innerHTML = feed[post].timestamp
                        tar.appendChild(document.createElement("p"));
                        tar.children[2].innerHTML = feed[post].id;
                        tar.children[2].style.display = "none";

                    })



            })



        });



        //Clicking on a user's name will pull up his page
        userlink.addEventListener("click", function() {
            console.log("User has been clicked"); 

            // Getting the id and username of the poster
            var tar = event.target;
    
            //Hide all the posts
            all_posts.style.display = "none";

            //Create some more shittt
            var header = document.createElement("h1");
            header.setAttribute("id", "header");
            header.innerHTML = tar.innerHTML;

            var ff = document.createElement("div");
            ff.setAttribute("id", "ff");

            var following = document.createElement("div");
            following.setAttribute("id", "following");
            following.innerHTML = "453";
            ff.appendChild(following);

            var text_following = document.createElement("p");
            text_following.setAttribute("id", "text_following");
            text_following.innerHTML = "Following";
            following.appendChild(text_following);

            var followers = document.createElement("div");
            followers.setAttribute("id", "followers");
            followers.innerHTML = "354";
            ff.appendChild(followers);

            var text_followers = document.createElement("p");
            text_followers.setAttribute("id", "text_followers");
            text_followers.innerHTML = "Followers";
            followers.appendChild(text_followers);

            var follow_div = document.createElement("div");
            follow_div.setAttribute("id", "follow_div");

            var follow = document.createElement("button");
            follow.setAttribute('id', 'follow');
            follow.setAttribute('type', 'button');
            follow.setAttribute('class', 'btn btn-danger btn-sm');
            follow_div.appendChild(follow);

            profile.appendChild(header);
            profile.appendChild(ff);
            if (document.querySelector("#java_username").innerHTML != header.innerHTML) {
                console.log(document.querySelector("#java_username").innerHTML)
                console.log(header.innerHTML)
                profile.appendChild(follow_div);

                //Doing the follow stuff
                document.querySelector("#follow").addEventListener("click", () => {
                post_user = tar.innerHTML;
                post_action = follow.innerHTML;
                form = new FormData();
                form.append("user", post_user);
                form.append("action", post_action);
                console.log(post_action);
                fetch("/follow", {
                    method: "POST",
                    body: form,
                })
                .then(response => response.json())
                .then(response => {
                    if (response.status == 201) {
                        
                        follow.innerHTML = response.action;
                        document.querySelector("#followers").innerHTML = `${response.follower_count}`;
                        //Recreateing this bs
                        var text_followers = document.createElement("p");
                        text_followers.setAttribute("id", "text_followers");
                        text_followers.innerHTML = "Followers";
                        followers.appendChild(text_followers);
                    }
                })
            })
            }
            profile.appendChild(document.createElement("hr"));

            

            //Getting the specific user (tar.value = user_id)
            fetch(`/profile_data/${tar.innerHTML}`)
            .then(response => response.json())
            .then(response => {
                // Print data
                console.log(response);

                document.querySelector("#followers").innerHTML = `${response.follower_count}`;
                //Recreateing this bs
                var text_followers = document.createElement("p");
                text_followers.setAttribute("id", "text_followers");
                text_followers.innerHTML = "Followers";
                followers.appendChild(text_followers);

                document.querySelector("#following").innerHTML = `${response.following_count}`;

                var text_following = document.createElement("p");
                text_following.setAttribute("id", "text_following");
                text_following.innerHTML = "Following";
                following.appendChild(text_following);

                document.querySelector("#follow").innerHTML = response.action;



            });
            



            //Getting the specific user (tar.value = user_id)
            fetch(`/profile/${tar.value}`)
            .then(response => response.json())
            .then(user_feed => {
                // Print posts
                console.log(user_feed);

                for (user_post in user_feed) {

                    //Creating the feed elements
                    var wrapper = document.createElement("div");
                    wrapper.setAttribute("id", "wrapper");

                    var user = document.createElement("div");
                    user.setAttribute("id", "user");
                    
                    var userlink = document.createElement("button");
                    userlink.setAttribute("id", "userlink");
                    userlink.setAttribute("type", "button" );
                    userlink.setAttribute("value", `${feed[post].user_id}`)
                    userlink.setAttribute("class", "btn btn-danger btn-sm");
                    user.appendChild(userlink);
                    userlink.innerHTML = user_feed[user_post].user_name;

                    var body = document.createElement("div");
                    body.setAttribute("id", "body");
                    body.appendChild(document.createElement("p"));
                    body.children[0].setAttribute("id", "body_content");
                    body.children[0].innerHTML = user_feed[user_post].body;
                    body.appendChild(document.createElement("p"));
                    body.children[1].setAttribute("id", "timestamp");
                    body.children[1].innerHTML = user_feed[user_post].timestamp

                    var likes = document.createElement("div");
                    likes.setAttribute("id", "likes");
                    likes.appendChild(document.createElement("div"));
                    likes.children[0].setAttribute("id", "likes_icon");
                    likes.children[0].innerHTML = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"20\" height=\"20\" fill=\"currentColor\" class=\"bi bi-heart-fill\" viewBox=\"0 0 16 16\"><path fill-rule=\"evenodd\" d=\"M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z\"/></svg>";
                    likes.appendChild(document.createElement("button"));
                    likes.children[1].setAttribute("id", "edit");
                    likes.children[1].setAttribute("class", "btn btn-danger btn-sm, edit");
                    likes.children[1].innerHTML = "Edit";
                    if (document.querySelector("#java_username").innerHTML != userlink.innerHTML) {
                        likes.children[1].style.display = "none";
                    }
                    likes.appendChild(document.createElement("div"));
                    likes.children[2].innerHTML = user_feed[user_post].likes;
                    likes.children[2].setAttribute("id", "num_likes");

                    wrapper.appendChild(user);
                    wrapper.appendChild(body);
                    wrapper.appendChild(likes);
                    profile.appendChild(wrapper);
                    profile.appendChild(document.createElement("hr"));




                }
                    

            

            });
            



        });




      }




  });
   
  

}

