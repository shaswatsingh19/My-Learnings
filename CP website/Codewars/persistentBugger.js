// https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/javascript
function persistence(num) {
  console.log('new question')
    let temp = 1
    let cnt =0
    
  while (num>9){
    cnt+=1
    temp = 1
    String(num).split('').forEach(el => {
      temp = temp*parseInt(el)
    }) 
    num = temp
  }
  return cnt
}