//default argument function

function f1(n1=1,n2=2,n3=3){
    console.log(`n1-${n1}, n2-${n2}, n3-${n3}`)
}

f1(10,20,30) //(10,20,30)
f1(10) //default value print(10,2,3)
f1(10,20) //default value print(10,20,3)
f1() //default value print (1,2,3)
f1(10,20,30,40) //ignores 40