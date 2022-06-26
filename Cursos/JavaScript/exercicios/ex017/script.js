function tabuada(){
    numero = Number(document.getElementById('entrada').value)
    resultado = document.getElementById('seltab')
    if (numero == ''){
        alert('Por favor, digite um número!')
    }
    else{
        resultado.innerHTML = "" //CLEAR()
        var c = 1
        while (c <= 10){
            line = document.createElement('option')
            line.text = `${numero} x ${c} = ${numero * c}`
            line.value = `line${c}`
            resultado.appendChild(line)
            c++
        }
    }
}
