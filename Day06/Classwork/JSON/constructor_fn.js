// Constructor Function
function Student(name, age) {
    this.name = name
    this.age = age
}

const s1 = new Student()
console.log(typeof (s1))
console.log(s1)

const s2 = new Student("Anil", 35)
console.log(s2)

const s3 = new Student("Mukesh", 30)
s3.mobile = "9876543210"
s3["email id"] = 'mukesh@gmail.com'
console.log(s3)