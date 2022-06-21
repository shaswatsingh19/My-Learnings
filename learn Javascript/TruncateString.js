//https://codedamn.com/challenge/5UFJFJeXsraoD9LJCrp6L
const str = 'JavaScript is simple but not easy to master';
const wordLimit = 3

function truncateWithWordLimit(str, wordLimit) {
    // write your solution here
    let ans = "";
    let f=0;
    str = str.split(" ");
    for(let i=0;i<wordLimit;i++){
        ans += str[i]+" ";
    }
    return ans.trim();
}

console.log(`Truncated string: ${truncateWithWordLimit(str, wordLimit)}`)
