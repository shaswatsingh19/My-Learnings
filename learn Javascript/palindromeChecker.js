function palindrome(str) {
    str = str.replace(/[^0-9a-zA-Z]/g, '')
    str = str.toLowerCase()
    console.log(str)
    let i = 0
    let j = str.length - 1
    while (i<j){
        if (str[i] != str[j]){
            return false
        }
        i+=1
        j-=1
    }
    return true
}
palindrome("A man, a plan, a canal. Panama")
