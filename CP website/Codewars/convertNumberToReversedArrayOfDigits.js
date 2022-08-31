// https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/javascript
function digitize(n) {
  //code here
  
  let arr = String(n).split('').reverse()
  
  console.log(arr)
  
  let newArr = arr.map(el => parseInt(el))
  return newArr

}