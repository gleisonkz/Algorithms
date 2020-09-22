// String methods //

/* charAt() */

let message = "HELLO WORLD";
let result = message.charAt(message.length - 1)
console.log(`The last letter is : ${result}`)

/* charCodeAt() */

const name = "John";
const unicode = name.charCodeAt(name.length - 1)
const info = "The unicode for the character is: "
console.log(info, unicode)

/* concat() */

const string1 = "Hello ";
const string2 = "world!";
const string3 = " Have a nice day!";
result = string1.concat(string2, string3);
result;

/* endsWith() */

message = "Hello world, welcome to the universe.";
result = message.endsWith("universe.");
result;
result = message.endsWith("world", 11);
result;

/* fromCharCode() */

result = String.fromCharCode(72, 69, 76, 76, 79);
result;

/* includes() */

message = "Hello world, welcome to the universe.";
result = message.includes('world')
result;

result = message.includes('world', 10)
result;

/* indexOf() */

message = "Hello world, welcome to the universe.";
result = message.indexOf('world')
result;

result = message.indexOf('world', 10)
result;

/* lastIndexOf() */

message = "Hello planet earth, you are a great planet.";
result = message.lastIndexOf('planet')
result;

result = message.lastIndexOf('planet', 11)
result;

result = message.lastIndexOf('planet', 5)
result;

/* match() */

message = "The rain in SPAIN plain";;
result = message.match(/ain/);
result;

result = message.match(/ain/g);
result;

result = message.match(/u/g);
result;

/* repeat() */

message = "Hello world!";

result = message.repeat(2)
result;

result = message.repeat(0)
result;

/* replace() */

message = "Mr Blue has a blue house and a blue car";

result = message.replace("blue", "RED")
result;

result = message.replace(/blue/g, "RED");
result;

/* search() */

message = "Mr. Blue has a blue house";

result = message.search("Blue")
result;

result = message.search("Hi");
result;

result = message.search(/blue/g);
result;



String.prototype.search
