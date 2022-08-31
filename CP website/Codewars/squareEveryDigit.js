//https://www.codewars.com/kata/546e2562b03326a88e000020/train/javascript
function squareDigits(num){
  
  let s = num+''
  let ans = ''
  s = s.split('')
  s.forEach(el => {
    ans += el*el
  })
  return Number(ans)
}