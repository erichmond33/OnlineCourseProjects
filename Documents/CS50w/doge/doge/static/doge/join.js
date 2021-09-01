document.addEventListener('DOMContentLoaded', function() {

    
    load_page()

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




    ////////////////////
    // CONTRACT CALL
    ///////////////////
    async function mint(nof_tokens) {
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
        // Calculate the price
        const price = web3.utils.toWei('0.06') * nof_tokens;
        // MINT!
        await contract.methods.mintAvantGardes(nof_tokens).send( {from: account, value: price})
        

        ////////////////////
        // Extra Calls/Sends 
        ////////////////////


        //let result;

        //console.log(web3.eth.getBlock("latest", (err, result) => {console.log(result)}))
        
        //await contract.methods.setBaseURI("Poo/turds/$h*t").send( {from: account })
        //result = await contract.methods.baseURI().call()
        //console.log(`This is the baseURI: ${result}`)
        
        //await contract.methods.reserve(6).send( {from: account})

        //await contract.methods.flipSaleState().send( {from: account })

        //result = await contract.methods.tokenURI(7).call()
        //console.log(`Token URI: ${result}`)

        //result = await contract.methods.totalSupply().call()
        //console.log(`Total Supply: ${result}`)
    }
}