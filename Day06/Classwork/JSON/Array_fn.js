// Array
const arr1 = [10, 22.33, 33.44, 40, 50]
console.log(arr1)

const arr2 = ["Anil", "Mukesh", "Ramesh", "Suresh"]
console.log(arr2)

const arr3 = [function (n1, n2) { return n1 + n2 }, function (n1, n2) { return n1 - n2 }]
console.log(arr3)
console.log(arr3[0])
console.log(arr3[0](10, 20))

const arr4 = [{ name: "Anil", age: 30 }, { name: "Mukesh", age: 35 }, { name: "Ramesh", age: 40 }]
arr4[1].mobile = "9876543210"
arr4[1]["email  id"] = "mukesh@gmail.com"
console.log(arr4)