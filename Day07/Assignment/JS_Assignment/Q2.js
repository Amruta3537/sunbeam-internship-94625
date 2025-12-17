let students =["sakshi", "pooja","rohit", "sonali"]

console.log(students)

//new student added
students.push("arihant")
console.log("After adding a student:", students)

//remove the first student from list
students.shift()
console.log("After removing first student:", students)


//total number of students
console.log("Total number of students:", students.length)

//display the last student in the list
console.log("Last student:", students[students.length - 1]);