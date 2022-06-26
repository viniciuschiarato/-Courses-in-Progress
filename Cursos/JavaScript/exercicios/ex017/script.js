function tabuada(){
    numero = Number(document.getElementById('entrada').value)
    resultado = document.getElementById('resultado')
    if (numero == ''){
        alert('Por favor, digite um número!')
    }
    else{
        var c = 1
        while (c <= 10){
            produto = numero * c
            if (c == 1){
                resultado.innerHTML = '</td>' + numero + ' x ' + c + ' = ' + produto + '</td><br>'}
            else{
            resultado.innerHTML += '</td>' + numero + ' x ' + c + ' = ' + produto + '<br>'}
            c++
        }
    }
}
