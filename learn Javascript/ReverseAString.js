// https://codedamn.com/challenge/yclXQP18JJLX28C26c5SA

const str = "JavaScript is awesome"

function reverseAString(str) {
    // write your solution here
    let ans = "";
    for(let i=str.length-1;i>-1;i--){
        ans+= str[i];
    }
    return ans;
}

console.log(`Reversed string is: ${reverseAString(str)}`)
