//Create student object
let student = {
    studentId: 101,
    fullName: "sakshi magdum",
    email: "sakshi@gmail.com",
    course: "AIML",
    marks: [78, 85, 69, 90]
};

//Convert object to JSON string
let studentJSON = JSON.stringify(student);
console.log("JSON String:");
console.log(studentJSON);

//Convert JSON string back to JavaScript object
let studentObject = JSON.parse(studentJSON);
console.log("JavaScript Object:");
console.log(studentObject);
