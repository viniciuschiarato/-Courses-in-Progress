var lista = []
function adicionar() {
    var numero = Number(document.getElementById('entrada').value)
    lista.push(numero)
    var conferencia = document.getElementById('conferencia')
    var info = document.createElement('option')
    info.text = `Valor ${numero} adicionado`
    conferencia.appendChild(info)
}
function resposta() {
    resp = []
    resp.push(`Ao todo, temos ${lista.length} número cadastrados.`)
    resp.push(`O maior valor informado foi ${lista.Max}`)
    resp.push(`O menor valor informado foi ${1}`)
    resp.push(`Somando todos os valores, temos ${1}`)
    resp.push(`A média dos valores digitados é ${1}`)
    for( var frase in resp){
        var campo_resposta = document.getElementById('campo_resposta')
        var verify = document.createElement('p')
        verify.textContent = `conteudo ${frase}`
        campo_resposta.appendChild(verify)
    }
}