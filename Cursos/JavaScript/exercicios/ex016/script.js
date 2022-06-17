function contar(){
    inicio = (Number(document.getElementById('inicio').value))
    fim = (Number(document.getElementById('fim').value))
    passo = (Number(document.getElementById('passo').value))
    resultado = document.getElementById('resultado')
    resultado.innerHTML = 'Contando:<br>'
    c = 0
    for(inicio; inicio <= fim; inicio += passo){
        c++
        if (c == 1){
            resultado.innerHTML += `${inicio}`
        }
        else{
            resultado.innerHTML += ` → ${inicio}`
        }
        
    }
    resultado.innerHTML += '🚩'
}
