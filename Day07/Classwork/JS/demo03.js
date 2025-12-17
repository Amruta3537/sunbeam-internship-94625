const arr = [11, 22, 33, 44, 55, 66, 77, 88]

for (const e of arr) {
    const res = e * e
    console.log(res)
}

console.log("using map")

arr.map((value, index, array) => {
        return value * value
    }) // returns the array of values
    .forEach(value => console.log(value))

console.log("using map in single line")
arr.map(value => value * value).forEach(value => console.log(value))