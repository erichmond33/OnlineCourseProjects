document.addEventListener('DOMContentLoaded', function() {

    
    //load_page()

});

function load_page() {
    //Check if Metamask is installed
    if (typeof window.ethereum !== 'undefined') {
        console.log('MetaMask is installed!');

        // If it is installed.. Check if user is connected
        let web3 = new Web3(Web3.givenProvider)
        web3.eth.getAccounts(function(err, accounts) {
            if (err != null) {
                console.error("An error occurred: "+err);
            }
            // If the user isn't connected.. Show them the connect button
            else if (accounts.length == 0) {
                console.log("User is not connected to MetaMask");
                
                document.querySelector("#div1_1_1").style.display = "none";
                document.querySelector("#div1_1_2").style.display = "block";
                document.querySelector("#div1_1_3").style.display = "none";

                // Connect to MetaMask
                document.querySelector("#button2").addEventListener('click', () => {
                    ethereum.request({ method: 'eth_requestAccounts' });
                });
            }
            // If the user is connected.. Show them the form
            else {
                document.querySelector("#div1_1_1").style.display = "none";
                document.querySelector("#div1_1_2").style.display = "none";
                document.querySelector("#div1_1_3").style.display = "block";

                // Mint the number of NFTs specified in the form
                document.querySelector("#form1").addEventListener('submit', function(e) {
                    e.preventDefault();
                    const error = document.querySelector("#p1")
                    const count = parseInt(document.querySelector("#count").value);
                    console.log(count)

                    //Ensure input is a number
                    if (!Number.isInteger(count)) {
                        error.style.display = "block";
                        error.innerHTML = "** Must be a <u>number</u> from 0-40 **";
                    }
                    //Ensure number is smaller than 40
                    else if (count > 40) {
                        error.style.display = "block";
                        error.innerHTML = "** Must be a number from <u>0-40</u> **";
                    }
                    //Ensure number isn't 0
                    else if (count == 0){
                        error.style.display = "block";
                        error.innerHTML = "** Must be a number from <u>0-40</u> **";
                    }
                    //Finally we can mint
                    else {
                        mint(count);
                        document.querySelector("#h1_3").innerHTML = "Welcome To The Club!"
                    }

                });
            }
        });
      }
    //If the user doesn't have metamask.. show them the link to download it
    else {
        console.log("Install MetaMask")

        document.querySelector("#div1_1_1").style.display = "block";
        document.querySelector("#div1_1_2").style.display = "none";
        document.querySelector("#div1_1_3").style.display = "none";
    }




}