// ----VARIABLES----
// let, const, DO NOT USE VAR 
// always use const unless you know you need to reassign
let a=30;
const a1=31

// DATATYPES
// String, Num, Bool, null, undefined

// const name= 'John';
// const age = 30;

// // Concatenation
// const hello =`My name is ${name} and I am ${age}`;
// console.log(hello);

// // String Methods
// const s= 'Hello World';
// console.log(s.length);
// console.log(s.toUpperCase());
// console.log(s.substring(0,5).toUpperCase());
// console.log(s.split(''));


// ARRAYS
const numbers = new Array(1,2,3,4,5);
const fruits = ['apples', 'pears', 'bananas'];

// console.log(numbers);
// console.log(fruits[1]);
// fruits[3]='grapes';

// // add to end
// fruits.push('mangoes');

// // add to beginning
// fruits.unshift('oranges');
// console.log(fruits);

// fruits.pop();
// console.log(fruits);

// // check if is array
// console.log(Array.isArray(fruits));

// // index of value
// console.log(fruits.indexOf('oranges'));


// OBJECT LITERALS
const person = {
	first:'John',
	last:'Doe',
	age:30,
	hobbies:['music', 'movies'],
	address:{
		street: '123 main st',
		city: 'Dallas',
		state:'TX'
	}
}

// console.log(person.first,person.last);
// console.log(person.hobbies[1],person.last);
// console.log(person.address.city)

// const {first , last, address:{state}} = person
// console.log(state);
// console.log(first)

// person.email='john@email.com';
// console.log(person.email)


const todos=[
	{
		id:1,
		text: 'Take out trash',
		isCompleted:true
	},
	{
		id:2,
		text: 'Meeting with Boss',
		isCompleted:true
	},
	{
		id:3,
		text: 'Dentist appt',
		isCompleted:false
	}
];

// console.log(todos[1].text)
// const todoJSON = JSON.stringify(todos);
// console.log(todoJSON);

// FOR LOOP
// for(let i = 0;i<todos.length;i++){
// 	console.log(`This is todo: ${todos[i].text}`);
// }

// for (let todo of todos){
// 	console.log(`This is todo: ${todo.text}`)
// }


// WHILE
// let i=0;
// while (i<10){
// 	console.log(`While loop This is number ${i}`);
// 	i++;
// }

// FOREACH, MAP, FILTER

// todos.forEach(function(todo){
// 	console.log(todo.text);
// });

// const todoText = todos.map(function(todo){
// 	return todo.text
// });
// console.log(todoText)

const todoCompleted = todos.filter(function(todo){
	return todo.isCompleted == true;
}).map(function(todo){
	return todo.text;
})
console.log(todoCompleted)






