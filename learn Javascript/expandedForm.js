function expandedForm(num) {
    // Your code here
    let ans = ''
    let i = 0
    while (num){
        const rem  = num%10;
        ans = Math.pow(10,i)*rem +"+" + ans
        i+=1
        num = parseInt(num/10)
    }
    return ans.substring(0,ans.length-1)
  }
  
  
console.log(expandedForm(242))