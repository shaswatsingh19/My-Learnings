// https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/javascript
function reverseWords(str) {
  // Go for it
  let ans = ''
  
  let strArr = str.split(' ')
  strArr.forEach(el => {
    ans += el.split('').reverse().join('')+" "
    console.log(ans)
  })
  
  return ans.trim()
  
}