document.addEventListener('DOMContentLoaded', function() {

    load_page()
    
});

window.addEventListener('load', function() { // can also use window.addEventListener('load', (event) => {
    
    load_page2()

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
            // If the user isn't connected.. Show them the preview
            else if (accounts.length == 0) {
                document.querySelector("#p1_1").innerHTML = "** This is for explanation purposes only **";
                document.querySelector("#div2").style.display = 'inline-flex';
            }
            // If the user is connected and a memeber don't show them the preview
            else {
                member()
            }
        });
      }
    //If the user doesn't have metamask.. show the preview
    else {
        document.querySelector("#p1_1").innerHTML = "** This is for explanation purposes only **";
        document.querySelector("#div2").style.display = 'inline-flex';
    }

    ////////////////////
    // CONTRACT CALL TO SEE IF THE USER HAS A MEMBERSHIP
    ///////////////////
    async function member() {
        // Get the accounts
        const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
        const account = accounts[0]
        //Initiate web3 instance
        let web3 = new Web3(Web3.givenProvider)
        await web3.eth.getAccounts(console.log);
        //Connect to the contract
        const abi = [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"MAX_AVANT_GARDES","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PROV","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"baseURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"flipSaleState","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxPurchase","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"numberOfTokens","type":"uint256"}],"name":"mintAvantGardes","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"price","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"nof_tokens","type":"uint256"}],"name":"reserve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"saleIsActive","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"baseURI","type":"string"}],"name":"setBaseURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]
        const address = '0xAbFA030A042ecbaa4FF1C6f0b27F331E0F7beebf'
        const contract = new web3.eth.Contract(abi, address)
        // Determine how many tokens our user has
        const tokenBalance = await contract.methods.balanceOf(account).call()

        if (tokenBalance >= 1) {
            document.querySelector("#p1_1").innerHTML = "\"The Memes\",\"The Cycle\", and \"The ATM\" are currently not avaliable. Rest assured that the Avant-Gardes team are working like mad men to create these functionalities ASAP. In the meantime, all of \"The Memes\" weekly competitions are being held on Twitter. Each week on Saturday at noon the winners are selected. <br><br> ** You must own an Avant-Garde in order to win the contest **";
            document.querySelector("#div2").style.display = 'none';
            document.querySelector("#button1").style.display = "none";
        }
        else {
            document.querySelector("#p1_1").innerHTML = "** This is for explanation purposes only **";
            document.querySelector("#div2").style.display = 'inline-flex';
            document.querySelector("#button1").style.display = "block";
        }

    }



}

function load_page2() {

    /*////////////////////////////
    ///// This is the Show Guide button
    /////////////////////////////////*/
    var count = 0;

    document.querySelector("#button1").addEventListener("click", () => {
        var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
        var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)});
        


        if (count % 2 == 0) {
            for (const tt of tooltipList) {
                tt.show()
            }

            document.querySelector("#button1").innerHTML = "Hide Guide";
        }
        else {
            window.location.reload();
        }

        count++;
        
    })

    /*//////////////////////
    //// Determing what should be in the profile
    /////////////////////////*/

    const post_div = document.querySelector("#div2_2")
    var height = document.querySelector("#img2_1").clientHeight + 59;

    // Deteting the scrolling
    post_div.addEventListener("scroll", ()=> {
        // ALways be at the top of the scroll
        document.querySelector("#profile-div").scrollTo(0, 0);

        if (isInViewport(document.querySelector("#h2_2_1"))) {
            // This is Bill Yates
            document.querySelector("#profile-name").innerHTML = "Bill Yates";
            document.querySelector("#description").innerHTML = "Bill Gate's identical adopted twin. Internet explorer fanatic, and the patent holder for sliced bread.";
            document.querySelector("#profile-img").src = "/static/doge/images/billyates.png";
        }
        else if (isInViewport(document.querySelector("#h2_2_2"))) {
            // This is Crack Sparrow
            document.querySelector("#profile-name").innerHTML = "Crack Sparrow";
            document.querySelector("#description").innerHTML = "Best friends with Pablo Escobar, Johnny Hopkins, and Sloan Kettering. Sailing the seven seas since the dawn of time.";
            document.querySelector("#profile-img").src = "/static/doge/images/cracksparrow.png";
        }
        else if (isInViewport(document.querySelector("#h2_2_3"))) {
            // This is BAYC
            document.querySelector("#profile-name").innerHTML = "BAYCCLMG";
            document.querySelector("#description").innerHTML = "Owner of Saturn, and top landscaper within my immediate family. My interests include horseshoes and hand grenades. No not the band.";
            document.querySelector("#profile-img").src = "/static/doge/images/bayc.png";
        }
        else if (isInViewport(document.querySelector("#h2_2_4"))) {
            // This is Hydrated Brick
            document.querySelector("#profile-name").innerHTML = "Hydrated Brick";
            document.querySelector("#description").innerHTML = "\"When moisture meets the man... maybe then you will understand\" <br><br> Imagine taking out a mortgage on your life and using your reputation as collateral. What a crazy concept XD";
            document.querySelector("#profile-img").src = "/static/doge/images/post-img4.png";
        }
        else if (isInViewport(document.querySelector("#h2_2_5"))) {
            // This is Holden
            document.querySelector("#profile-name").innerHTML = "Holden Tudix";
            document.querySelector("#description").innerHTML = "Senior Vice Prez at InnuendoCorp.gov<br>Catch me on Soundcloud.<br><br>\"I drive the ladies crazy. All the fathers hate me, but the daughters wanna date me. Never lazy cause this game ain't free\"";
            document.querySelector("#profile-img").src = "/static/doge/images/post-img5.png";
        }
        else if (isInViewport(document.querySelector("#h2_2_6"))) {
            // This is BAYC
            document.querySelector("#profile-name").innerHTML = "Mother Nature";
            document.querySelector("#description").innerHTML = "My middle name is Larry.";
            document.querySelector("#profile-img").src = "/static/doge/images/post-img6.png";
        }
        else if (isInViewport(document.querySelector("#h2_2_7"))) {
            // This is BAYC
            document.querySelector("#profile-name").innerHTML = "Hot Einstein";
            document.querySelector("#description").innerHTML = "What if we made a hologram, and then sent the photos faster than the speed of light into the past?";
            document.querySelector("#profile-img").src = "/static/doge/images/post-img7.png";
        }
        else if (isInViewport(document.querySelector("#h2_2_8"))) {
            // This is BAYC
            document.querySelector("#profile-name").innerHTML = "born2hug";
            document.querySelector("#description").innerHTML = "Ancestry.com said I was 1/8th squash. TBH I can see the resemblence in my facial features.";
            document.querySelector("#profile-img").src = "/static/doge/images/post-img8.png";
        }
        else if (isInViewport(document.querySelector("#h2_2_9"))) {
            // This is BAYC
            document.querySelector("#profile-name").innerHTML = "Kuul Aid";
            document.querySelector("#description").innerHTML = "Like a juul, but you just drink the nicotine... Put the juice in a tide pods like container, and I think we are onto something huge here.";
            document.querySelector("#profile-img").src = "/static/doge/images/post-img9.png";
        }



        else if (isInViewport(document.querySelector("#h2_2_12"))) {
            // This is BAYC
            document.querySelector("#profile-name").innerHTML = "JustRemember";
            document.querySelector("#description").innerHTML = "Comedy is subjective :)<br><br>I think you get the point. You post whatever makes you laugh.";
            document.querySelector("#profile-img").src = "/static/doge/images/post-img10.png";
        }
    })

    function isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }
    
    /*///////////////
    /// Controling the heights of the scrollables
    /////////////////*/

    // Intializing
    var height = document.querySelector("#img2_1").clientHeight + 59;
    document.querySelector("#div2_2").style.height = `${height}px`;
    document.querySelector("#profile-div").style.height = `${height - 68}px`;
    //document.querySelectorAll(".profile-div")[1].style.height = `${height}px`;

    // Updating
    window.addEventListener("resize", function() {
        var height2 = document.querySelector("#img2_1").clientHeight + 59;
        document.querySelector("#div2_2").style.height = `${height2}px`;
        document.querySelector("#profile-div").style.height = `${height2 - 67}px`;
        console.log(height)
        //document.querySelectorAll(".profile-div")[1].style.height2 = `${height2}px`;
    })
};