function contar() {
    inicio = (Number(document.getElementById('inicio').value))
    fim = (Number(document.getElementById('fim').value))
    passo = (Number(document.getElementById('passo').value))
    resultado = document.getElementById('resultado')
    resultado.innerHTML = 'Contando:<br>'
    if (inicio == '' || fim == '') {
        resultado.innerHTML = 'Impossível contar.'
    }
    else if (inicio > fim) {
        c = 0
        for (inicio; inicio >= fim; inicio -= passo) {
            c++
            if (c == 1) {
                resultado.innerHTML += `${inicio}`
            }
            else {
                resultado.innerHTML += ` → ${inicio}`
            }
        }
        resultado.innerHTML += '🚩' // \u{cód.}

    }
    else {  
        if (passo == 0 || passo == '') {
            alert('[ERRO] Passo inválido! Considerando passo = 1.')
            passo = 1
        }
    
        c = 0
        for (inicio; inicio <= fim; inicio += passo) {
            c++
            if (c == 1) {
                resultado.innerHTML += `${inicio}`
            }
            else {
                resultado.innerHTML += ` → ${inicio}`
            }
        }
        resultado.innerHTML += '🚩'
    }
}
