function high(x) {

    const arr = x.split(' ')
    let temp = 0
    let max = 0
    let ans = ''
    for (let word of arr){
        for (let char of word){
            temp += char.charCodeAt()-96
            console.log(char.charCodeAt()-96,char)
        }
        console.log(temp,word)
        if (temp > max){
            max = temp
            ans = word
            console.log('max word till',ans)
        }
        temp = 0  

    }
    console.log(ans)

}

high('what time are we climbing up the volcano') 
// high('man i need a taxi up to ubud')