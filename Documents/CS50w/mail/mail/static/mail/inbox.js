document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  var archive = document.createElement('button');
  archive.innerHTML = "Archive";
  archive.setAttribute("id", "archive");
  archive.setAttribute("class", "btn btn-sm btn-primary");
  document.querySelector("#navBar").append(archive);
  archive.style.float = "right";

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  //Changing some css
  document.querySelector("#compose-sender").style.borderRadius = "25px"; 
  document.querySelector("#compose-recipients").style.borderRadius = "25px";
  document.querySelector("#compose-subject").style.borderRadius = "25px";
  document.querySelector("#compose-body").style.borderRadius = "10px 25px 10px 25px";

  document.querySelector("#compose-recipients").style.border = "1px solid"
  document.querySelector("#compose-subject").style.border = "1px solid"
  document.querySelector("#compose-body").style.border = "1px solid"
  document.querySelector("#compose-sender").style.border = "1px solid";
  
  document.querySelector("#shitButton").style.borderRadius = "25px";

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  //Sending an email
  document.querySelector('#compose-form').onsubmit = function() {

    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
          recipients: document.querySelector('#compose-recipients').value,
          subject: document.querySelector('#compose-subject').value,
          body: document.querySelector('#compose-body').value
      })
    })
    .then(response => response.json())
    .then(result => {
        // Print result
        console.log(result);
    }).then(load_mailbox('sent'));

    return false;
  }
}


function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  var email_view = document.querySelector('#emails-view')
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';

  email_view.style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;



  // THESE ARE JUST TO TEST MY DAMN WEBSITE
  ////var mail = document.createElement('div');
  ////mail.textContent = "dick eater yes no";
  ///document.querySelector('#emails-view').appendChild(mail);

  /* THIS IS JUST TO CHANGE VALUES ARTIFICIALLY
  fetch("/emails/5", {
    method: 'PUT',
    body: JSON.stringify({
    read: false
    })
    })
  */ 

  //Saving the page so I can archive properly
  var prevPage = document.querySelector("#emails-view").children[0].innerHTML;
  document.querySelector("#archive").style.display = "none";




  //Using the "GET" method to fetch a users inbox/sent/archieved mail
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
      // Print emails
      console.log(emails);

      // ... do something else with emails ...
      for (email in emails) {

        var mail = document.createElement("div");
        mail.setAttribute("id", "mail");
        var id = document.createElement('p');
        var subject = document.createElement("p");
        var sender = document.createElement("p");
        var time = document.createElement("p");

        id.innerHTML = emails[email].id;
        subject.innerHTML = emails[email].subject;
        sender.innerHTML = emails[email].sender;
        time.innerHTML = emails[email].timestamp;
      
        mail.appendChild(sender);
        mail.appendChild(subject);
        mail.appendChild(time);
        mail.appendChild(id);

        document.querySelector('#emails-view').appendChild(mail);

        //CSS STUF ----------------
        id.style.display = "none";

        if (emails[email].read == true) {
          mail.style.backgroundColor = "lightGray";
        }
        else {
          mail.style.backgroundColor = "white";
        }

        mail.style.border = '1px solid';
        mail.style.borderBottom = "none";
        mail.style.lineHeight = "0";
        mail.style.textAlign = "center";
        mail.style.borderRadius = "5px";
        
        if (emails[email] == emails[emails.length - 1]) {
          mail.style.border = "1px solid";
        }

        subject.style.display = "inline-block";
        subject.style.margin = "1rem";
        sender.style.display = "inline-block";
        sender.style.margin = "1rem";
        sender.style.float = "left";
        time.style.display = "inline-block";
        time.style.margin = "1rem";
        time.style.float = "right";



        /////////////////////////////////////

  

        // This is going to load emails when they are clicked
        mail.addEventListener("click", function() {
          console.log("Email has been clicked");
          console.log(prevPage);

          var tar = event.target;

          if(!(tar.tagName == "DIV")) {
            tar = tar.parentElement;
          }
          //Clear the page
          document.querySelector("#emails-view").innerHTML = "";

          //Set up a header (div(h6)(p)) then a sub (div(h5)(p)) then a body (div(p))
          var header = document.createElement("div");
          header.setAttribute("id", "header");
          header.appendChild(document.createElement("h6"));
          header.appendChild(document.createElement("p"));
          header.children[0].setAttribute("id", "header0")
          header.style.border = "1px solid";
          header.style.lineHeight = "0";
          header.style.borderRadius = "25px";
          header.style.paddingLeft = "1rem";
          header.children[1].style.fontSize = ".75em";

          var sub = document.createElement("div");
          sub.setAttribute("id", "sub");
          sub.appendChild(document.createElement("h5"));
          sub.appendChild(document.createElement("p"));
          sub.style.border = "1px solid";
          sub.style.lineHeight = "0";
          sub.style.borderRadius = "10px 25px 0px 0px";
          sub.style.paddingLeft = "1rem";
          sub.children[1].style.fontSize = ".75em";

          var body = document.createElement('div');
          body.setAttribute("id", "body");
          body.appendChild(document.createElement("p"));
          body.style.border = "1px solid";
          body.style.borderRadius = "0px 0px 10px 25px";
          body.style.paddingLeft = "1rem";
          body.style.paddingTop = "1rem";
          body.style.borderTop = "none";

          ///////////// Reply Button ////////////////////

          var reply = document.createElement('button');
          reply.innerHTML = "Reply";
          reply.setAttribute("id", "reply");
          reply.setAttribute("class", "btn btn-sm btn-primary");
          reply.style.borderRadius = "25px";
          var space = document.createElement("hr");

          ///////////////////////////////////////////////////

          document.querySelector("#emails-view").appendChild(header);
          document.querySelector("#emails-view").appendChild(document.createElement("br"));
          document.querySelector("#emails-view").appendChild(sub);
          document.querySelector("#emails-view").appendChild(body);
          document.querySelector("#emails-view").appendChild(space);
          document.querySelector("#emails-view").append(reply);

          // Getting the email that was clicked on, then updating it to read
          fetch(`/emails/${tar.children[3].innerHTML}`)
          .then(response => response.json())
          .then(email => {
              // Print email
              console.log(email);

              // ... do something else with email ...
              header.children[0].innerHTML = `${email.sender}`;
              header.children[1].innerHTML = `To: ${email.recipients}`;
              sub.children[0].innerHTML = `${email.subject}`;
              sub.children[1].innerHTML = `${email.timestamp}`;
              body.children[0].innerHTML = `${email.body}`;

              
          });

          fetch(`/emails/${tar.children[3].innerHTML}`, {
            method: 'PUT',
            body: JSON.stringify({
            read: true
            })
            })

            ////////////////////////////////////////


          // Creating the archive function
          if (prevPage == "Inbox") {
            console.log("INbox");
            //Archive elements
            document.querySelector("#archive").style.display = "block";
            document.querySelector("#archive").innerHTML = "Archive";
            prevPage = "";

            document.querySelector("#archive").onclick = function() {
              fetch(`/emails/${tar.children[3].innerHTML}`, {
                method: 'PUT',
                body: JSON.stringify({
                archived: true
                })
                });
                setTimeout(() => {  load_mailbox("inbox"); }, 10);
              }
          }
          else if (prevPage == "Archive") {
            console.log("arch");
            //Archive elements
            document.querySelector("#archive").style.display = "block";
            document.querySelector("#archive").innerHTML = "Unarchive";
            prevPage = "";

            document.querySelector("#archive").onclick = function() {
              fetch(`/emails/${tar.children[3].innerHTML}`, {
                method: 'PUT',
                body: JSON.stringify({
                archived: false
                })
                })
                setTimeout(() => {  load_mailbox("inbox"); }, 10);
            }
          }
          else {
            document.querySelector("#archive").style.display = "none";
          }


          ////////////////////////// REPLY FUNCTION ///////////////////////

          document.querySelector("#reply").onclick = function() {
            
            fetch(`/emails/${tar.children[3].innerHTML}`)
            .then(response => response.json())
            .then(email => {
                // Print email
                console.log(email);

                // ... do something else with email ...
                compose_email();

                // Fill in composition fields
                document.querySelector('#compose-recipients').value = `${email.sender}`;
                document.querySelector('#compose-subject').value = `Re: ${email.subject}`;
                document.querySelector('#compose-body').value = `On ${email.timestamp} ${email.sender} wrote: ${email.body}`;
            });
          }
  


        });
      
      }    
  });
}