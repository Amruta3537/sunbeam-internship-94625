// Higher Order Functions
function arithmeticExecuter(fn) {
    const res1 = fn(10,20)
    console.log(`Result in Executer - ${res1}`)
}

arithmeticExecuter((n1, n2) => n1 + n2)
arithmeticExecuter((n1, n2) => n1 - n2)
arithmeticExecuter((n1, n2) => n1 * n2)
arithmeticExecuter((n1, n2) => n1 / n2)


// arithmeticExecuter(function (n1, n2) {
//     return n1 + n2
// })

// arithmeticExecuter((n1, n2) => {
//     return n1 + n2
// })