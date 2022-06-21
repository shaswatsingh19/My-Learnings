console.log('LEVEL 1')


try{
  let a = 5/0
  console.log(a)
}catch(err){
  console.log(err)
}finally{
  console.log('I will always run')
}

try{
  console.log(arr)
}catch(err){
  console.log(err.name)
  console.log(err.message)
}
