document.addEventListener('DOMContentLoaded', function() {

    ////////////////////////
    /// WEB3 and METAMASK
    ///////////////////////

    //Check if Metamask is installed
    if (typeof window.ethereum !== 'undefined') {
        console.log('MetaMask is installed!');

        //Keeping the website updated on chain/account changes
        ethereum.on('accountsChanged', function (accounts) {
            // Reload
            location.reload();
        });
        ethereum.on('chainChanged', (chainId) => {
            // Reload
            location.reload();
        });

        // If it is installed.. Check if user is connected
        let web3 = new Web3(Web3.givenProvider)
        web3.eth.getAccounts(function(err, accounts) {
            if (err != null) {
                console.error("An error occurred: "+err);
            }
            // If the user isn't connected.. Show them the connect button
            else if (accounts.length == 0) {
                console.log("User is not connected to MetaMask");
                
                document.querySelector("#login-button").innerHTML = "Connect";

                // Connect to MetaMask
                document.querySelector("#login-button").addEventListener('click', () => {
                    ethereum.request({ method: 'eth_requestAccounts' });
                });
            }
            // If the user is connected.. Show them Connected
            else {
                document.querySelector("#login-button").innerHTML = "Connected";
                // If the user also has a membership.. Reroute them to the membership page
                member()
            }
        });
        }
    //If the user doesn't have metamask.. show them the link to download it
    else {
        console.log("Install MetaMask");

        document.querySelector("#login-button").innerHTML = "Install";
        
        document.querySelector("#login-button").addEventListener('click', () => {
            window.open('https://metamask.io','_blank')
        });
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
            console.log("You are a memeber.")
            /*
            document.querySelector("#navbarFoldout").style.display = "none";
            document.querySelector("#navbarFoldout2").style.display = "inline-flex";*/

        }

    }


    ///////////////////
    ////// Navbar disappear/reappear function
    /////////////////////
    var scrollBefore = 0;

    window.addEventListener("scroll", function() {
        const scrolled = window.scrollY;

        if (document.querySelector(".navbar-toggler").getAttribute("aria-expanded") == "false") {


            if(scrollBefore <= 0) {
                document.querySelector("#navBar").style.visibility = "visible";
                scrollBefore = scrolled;
            }
            else if((window.scrollY + window.innerHeight) >= document.body.scrollHeight) {
                document.querySelector("#navBar").style.visibility = "hidden";
                scrollBefore = scrolled;
            }
            else if(scrollBefore > scrolled) {
                document.querySelector("#navBar").style.visibility = "visible";
                scrollBefore = scrolled;
            }
            else {
                scrollBefore = scrolled;
                document.querySelector("#navBar").style.visibility = "hidden";
            }
            
        }

    });





    //Changing the navbarFoldout when the window reaches the larger view
    /*
    window.addEventListener("resize", function() {
        var position = document.querySelector(".navbar-toggler").getBoundingClientRect();

        if (position.left == "0") {
        document.querySelector("#navbarFoldout").style.background = "none";
        }
        else {
            document.querySelector("#navbarFoldout").style.background = "#c1cdb8;";
        }
    })*/



    //Logging in
    /*
    document.querySelector("#login").addEventListener("click", function() {

        document.querySelector("#no-login-view1").style.display = "none";
        document.querySelector("#no-login-view2").style.display = "none";
        document.querySelector("#no-login-view3").style.display = "none";


        

        document.querySelector("#login-view1").style.display = "block";
        document.querySelector("#login-view2").style.display = "block";
        document.querySelector("#login-view3").style.display = "block";
        


    });*/





    /*
    // Configuring the page
    var position = document.querySelector(".navbar-toggler").getBoundingClientRect();

        if (position.left == "0") {
        document.querySelector("#navbarFoldout").style.background = "none";
        }
        else {
            document.querySelector("#navbarFoldout").style.background = "#c1cdb8;";
        }*/




});


