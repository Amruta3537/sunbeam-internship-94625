// Array
const arr = [] // Array
console.log(typeof (arr))
console.log(arr)

const arr2 = [10, 20]
console.log(arr2)

const arr3 = new Array()
arr3.push(10)
arr3.push(20)
arr3.push(30)
arr3.push(40)

arr3.pop()
console.log(arr3.length)
console.log(arr3)

// Array
const arr4 = [10, 20, 30, 40, 50, 60]
// index based for loop
for (let i = 0; i < arr4.length; i++)
    console.log(`element - ${arr4[i]}`)

// for-of loop
for (const element of arr)
    console.log(`element - ${element}`)