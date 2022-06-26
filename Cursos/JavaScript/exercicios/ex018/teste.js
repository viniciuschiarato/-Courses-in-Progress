let valores = [8, 1, 7, 4, 2, 9]
//valores.sort()
console.log(valores)

/*
for (pos = 0; pos < valores.length; pos++) {
    console.log(`A posição ${pos} tem o valor ${valores[pos]}`)
}
*/
for(let pos in valores) {
    console.log(`A posição ${pos} tem o valor ${valores[pos]}`)
}
num = [4, 5, 6, 7, 8]

console.log(num.indexOf(3))  // return "3" the key
console.log(num.indexOf(3))  // return "-1" not found
