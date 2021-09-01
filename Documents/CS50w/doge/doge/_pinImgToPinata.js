/*document.addEventListener('DOMContentLoaded', function() {

    document.querySelector("#divv").innerHTML = "Hi";
  

    const Web3 = require("web3")
    const rpcURL = "http://127.0.0.1:7545"
    const web3 = new Web3(rpcURL)

    const abi = [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"flipSaleState","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"numberOfTokens","type":"uint256"}],"name":"mintCraniums","outputs":[],"stateMutability":"payable","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"nof_tokens","type":"uint256"}],"name":"reserveCraniums","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"baseURI","type":"string"}],"name":"setBaseURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"baseURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"craniumPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_CRANIUMS","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxCraniumPurchase","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PROV","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"saleIsActive","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]
    const address = '0xFf96FA1120C924cbeD1B0dC5cA3218A9D17A215C'

    const contract = new web3.eth.Contract(abi, address)

    const owner = "0x059B3969FaD8d9b1D5A49bF3c4A2725271E301A4"
    const user1 = "0x596a8626165551F4050F13D51bdA718222749788"
    const user2 = "0x12Adc2239B5EAc38c0ab957ce007040D32be64cB"

    const baseURI = "https://6969AvantGardes/metadata/001/"

    const num = 1

    async function run() {
        web3.eth.getBlock("latest", (err, result) => {console.log(result)})
        let result

        await contract.methods.setBaseURI(baseURI).send( {from: owner })


        result = await contract.methods.baseURI().call()
        console.log(`This is the baseURI: ${result}`)

        await contract.methods.reserveCraniums(num).send( {from: owner, gas: 150000})

        result = await contract.methods.totalSupply().call()
        console.log(`This is the total supply: ${result}`)
    }

    document.querySelector("#divv").addEventListener("click", function() {
        document.querySelector("#divv").innerHTML = "Hello";
        console.log("Hello")
    })


});*/

/*
Free acount
API Key: 392d7e605a508b830dad
API Secret: d0083387b73e374151eee5dcc02d8d15879f29df5588c1b1d4243957c6ba58aa
JWT: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiJkYjQ1ODE0Mi0yMTAyLTRjZTctODZmMC0xZWQzODFlZDExNmUiLCJlbWFpbCI6ImVlcmljaG1vbmRzcGFtQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwaW5fcG9saWN5Ijp7InJlZ2lvbnMiOlt7ImlkIjoiTllDMSIsImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxfV0sInZlcnNpb24iOjF9LCJtZmFfZW5hYmxlZCI6ZmFsc2V9LCJhdXRoZW50aWNhdGlvblR5cGUiOiJzY29wZWRLZXkiLCJzY29wZWRLZXlLZXkiOiIzOTJkN2U2MDVhNTA4YjgzMGRhZCIsInNjb3BlZEtleVNlY3JldCI6ImQwMDgzMzg3YjczZTM3NDE1MWVlZTVkY2MwMmQ4ZDE1ODc5ZjI5ZGY1NTg4YzFiMWQ0MjQzOTU3YzZiYTU4YWEiLCJpYXQiOjE2MjgwMDM1MTJ9.AinvGqcv5ExpfiCEM1JzH_gtEICVw8-WJqabpFAQUxk
 
Paid Account
API Key: bce4108aa4a39b116b4d
API Secret: 6ada3ec39737f91450a4df29e3c25e98e93448610a4c5afd1249611f33ec5c9b
JWT: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI0MzcwZjRlMC1hZjYzLTRjZWYtOGM0OC04NmFiMGE3NGRhNDAiLCJlbWFpbCI6ImF2YW50Z2FyZGVzdjFAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siaWQiOiJOWUMxIiwiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjF9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZX0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6ImJjZTQxMDhhYTRhMzliMTE2YjRkIiwic2NvcGVkS2V5U2VjcmV0IjoiNmFkYTNlYzM5NzM3ZjkxNDUwYTRkZjI5ZTNjMjVlOThlOTM0NDg2MTBhNGM1YWZkMTI0OTYxMWYzM2VjNWM5YiIsImlhdCI6MTYyODU3MzI3Nn0.k7TGmFQd3IlT0n8hZaYs5glDoGFJVcKRnRAnzB2ZAvs

*/

//imports needed for this function
const process = require("process");
const fs = require("fs");
const pinataSDK = require("@pinata/sdk");
const PINATA_API_KEY = "bce4108aa4a39b116b4d";
const PINATA_SECRET_API_KEY = "6ada3ec39737f91450a4df29e3c25e98e93448610a4c5afd1249611f33ec5c9b";
const pinata = pinataSDK(PINATA_API_KEY,PINATA_SECRET_API_KEY);

var imgPath = process.argv[2]
const readableStreamForFile =fs.createReadStream(imgPath);
const options = {};

pinata.pinFileToIPFS(readableStreamForFile, options).then((result) => {
    console.log(result["IpfsHash"])
}).catch((err) => {
    console.log(err)
});



