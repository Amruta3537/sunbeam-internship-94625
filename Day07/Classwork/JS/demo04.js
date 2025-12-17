const arr = [11, 22, 33, 44, 55, 66, 77, 88]

// display the square of odd numbers
arr.filter(e => e % 2 != 0).map(e => e * e).forEach(e => console.log(e))

console.log(arr)