// Estrutura de repetição com teste lógico no início:
/*var c = 1
while (c <= 6){
    console.log(`Passo ${c}`)
    c++
}*/
// Estrutura de repetição com teste lógico no final:
/*var c = 1
do{
    console.log(`Passo ${c}`)
    c++
}while(c <= 6)
*/
//for(inicio; teste; incremento)
/*
console.log('Vai começar...')
for(var c = 1; c <= 6; c++){
    console.log(c)
}
console.log('Fim!')*/

a = 1
b = 10
c2 = 2

inicio = Number(a)
fim = Number(b)
passo = Number(c2)
c = 0
for(inicio; inicio <= fim; inicio += passo){
    c++
    if (c == 1){
        console.log (inicio)
    }
    else{
        console.log (` → ${inicio}`)
    }
    
}
console.log += '🚩'