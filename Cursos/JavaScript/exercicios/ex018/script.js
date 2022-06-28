var lista = []

function duplicidade(value, arr){
    if(arr.indexOf(Number(value)) != -1){
      return true
    }
    else{
      return false
    }
}

function numero_natural(value){
    if(value < 0){
        return true
    }
    else{
        return false
    }
}

function campo_vazio(value){
    if(value == ""){
        return true
    }
    else{
        return false
    }
}
function adicionar() {

    var numero = Number(document.getElementById('entrada').value)
    if (duplicidade(numero, lista) ||numero_natural(numero)|| numero > 100 || campo_vazio(numero)) {
        alert('Valor é inválido ou já encontrado na lista')
    }
    else {
        lista.push(numero)
        var conferencia = document.getElementById('conferencia')
        var info = document.createElement('option')
        info.text = `Valor ${numero} adicionado`
        conferencia.appendChild(info)
    }
}
function resposta() {
    if (lista == ""){
        alert("adicione valores antes de finalizar")
    }
    else{
        function soma_lista(lista_) {
            soma = 0
            for (var pos in lista_) {
                soma += lista_[pos]
            }
            return soma
        }
    
        function media_lista(lista_) {
    
            soma = 0
    
            media = lista_.length
            for (var pos in lista_) {
                soma += lista_[pos]
            }
            media = soma / media
            return media
        }
        var campo_resposta = document.getElementById('campo_resposta')
        campo_resposta.innerHTML = `<p>Ao todo, temos ${lista.length} número cadastrados.</p>`
        campo_resposta.innerHTML += `<p>O maior valor informado foi ${Math.max.apply(null, lista)}</p>`
        campo_resposta.innerHTML += `<p>O menor valor informado foi ${Math.min.apply(null, lista)}</p>`
        campo_resposta.innerHTML += `<p>Somando todos os valores, temos ${soma_lista(lista)}</p>`
        campo_resposta.innerHTML += `<p>A média dos valores digitados é ${media_lista(lista)}</p>`
    }
}
