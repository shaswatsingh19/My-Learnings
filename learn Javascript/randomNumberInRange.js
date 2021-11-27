// https://codedamn.com/challenge/Ia-7GPHBN7EENeQzargcz
function randomNumberGeneratorInRange(rangeStart, rangeEnd) {
	// write your solution here

	return (Math.random()*(rangeEnd-rangeStart)) + rangeStart;
}

console.log(`My random number: ${randomNumberGeneratorInRange(5, 100)}`)
