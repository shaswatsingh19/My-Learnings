const totalGrains = (input) => {
	// Code here
    let total = 0n;
    let i =0
    while (i<input){
        total += BigInt(Math.pow(2,i))
        i+=1
    }
    return total
    
}

const grainsOn = (input) => {
	// Code here
	return BigInt(Math.pow(2,input-1))
}

console.log(`Grains on 5th square: ${grainsOn(5)}`)
console.log(`Total grains upto 5th square: ${totalGrains(5)}`)
