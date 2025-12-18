function changeText(){
    document.getElementById("msg").innerText = "This Text Changed!"
}

function changeColor(){
    document.getElementById("msg").style.color = "yellow"
}

function showText(){
    let name = document.getElementById("name").value
    document.getElementById("title").innerText = "Hello, " +name
}
