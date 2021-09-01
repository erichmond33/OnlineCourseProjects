document.addEventListener('DOMContentLoaded', function() {

    document.querySelector("#form1").submit

    ////////////////////////
    //// Random Button
    ///////////////////////
    const backgrounds = ["White", "Red", "Blurple", "Green", "Dingy Yellorange", "Light Blue", "Purple", "Rainbow", "Pink", "Too Loud"]
    const extras = ["Get Hard", "69", "Mike Tyson", "Illuminate", "Prank", "Sniper", "Harry", "Eye Black", "Airpods", "Ranch It Up", "Swords"]
    const clothes = ['Stratton', 'Rick Rolled', 'Bandolier', 'Bake',
    'Original', 'Thriller', 'Spaceman', 'Crocodile Hunter', 
    'Lloyd', 'Swamp People', 'Thrift Shop', 'Denim Jacket',
    'The Champ Champ', 'Shake', 'Doge To The Moon', 'Nacho',
    'Major Payne', 'Terminator', 'Snakeskin', "Cowboy", 'Hotrod', 'McLovin',
    'Harambe', "Magnum Dong", "Fluffy", "DONKEY", "Burgundy", "Carlos", "McCracken",
    "Gravey Train", "Idiot Sandwhich", "Insertchucknorrisjokehere", "Tropic Thunder",
    "Wilder", "Wubba Lubba Dub Dub", "Houdini"]
    const heads = ['Wolverine Hat', 'Planet BS', "The Best Pirate I Have Ever Seen", "Indiana Jones",
    "Turds", "Hulk Hogan", "King George", "Angus Young", "Clint Eastwood",
    "Wildcat", "Alright", "Eminem", "Santa", "Joker", "Army", "Dino",
    "Wolverine", "Tinfoil", "Wax On Wac Off", "Happy Accidents", "Date Mike", "Clark",
    "Somebody Stop Me", "Sombrero", "Classic Bowler", "Captain", "Nobody Cares", "Ducks", "Watermelon"]
    const eyes = ["Wilder", "No Eyes", "Thug Life", "Lazers", "Aviators",
    "Rocketman", "Purple", "Undertaker", "Eyepatch", "Wolfie", "All Knowing",
    "Jackass 3d", "Unistyle", "Truly Unfortunate", "What If I Told You",
    "Wack", "Eyeliner", "Lines"]
    const mouths = ["Snoop Dogg", "Sun Tzu", "Tape", "Leonardo", "Pipe",
    "Hunger Games", "Toothpick", "Piercing", "Speechless", "Sam Elliot",
    "Mutton Chops", "I Can Quit Whenever I Want", "Straw", "Shiv",
    "Bull Ring", "Pucker Up"]



    document.querySelector("#button2").addEventListener('click', function(e) {
        e.preventDefault();

        document.querySelector("#input1").value = get_random(backgrounds);
        document.querySelector("#input2").value = get_random(extras);
        document.querySelector("#input3").value = get_random(eyes);
        document.querySelector("#input4").value = get_random(clothes);
        document.querySelector("#input5").value = get_random(heads);
        document.querySelector("#input6").value = get_random(mouths);
    })
});

function get_random(list) {
    const randomElement = list[Math.floor(Math.random() * list.length)];
    return randomElement;
}
