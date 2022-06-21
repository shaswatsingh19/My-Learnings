// https://codedamn.com/challenge/LxalzcQPyJndNggBWcNjY

const num = 3849;

function reverseGivenInteger(num) {
    // write your solution here
    let ans = 0;
    while(num>0){
        let rem = num%10;
        num  = parseInt(num/10);
        ans =  ans*10 + rem;//9483
    }
    return ans;
}

console.log(`Reversed integer is: ${reverseGivenInteger(num)}`)

