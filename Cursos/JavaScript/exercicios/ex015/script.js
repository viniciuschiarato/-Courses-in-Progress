function verificar() {
    var data = new Date
    var ano = data.getFullYear()
    var fano = document.getElementById("txtano")
    var res = document.querySelector('div#res')
    if (fano.value.length == 0 || Number(fano.value) > ano){
        alert('Deu ruim. Você entrou com o ano maior que o atual.')
    }
    else{
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')

        var genero = ''
        if (fsex[0].checked){
            genero = 'Homen'
            if (idade >=0 && idade < 14){
                img.setAttribute("src","imagens/modified/crianca-m.png")
            }
            else if (idade > 14 && idade < 21) {
                img.setAttribute("src","imagens/modified/jovem-m.png")
            }
            else if (idade > 21 && idade < 60) {
                img.setAttribute("src","imagens/modified/adulto-m.png")
            }
            else {
                img.setAttribute("src","imagens/modified/velho-m.png")
            }
        }
        else{
            genero = 'Mulher'
            if (idade >=0 && idade < 14){
                img.setAttribute("src","imagens/modified/crianca-f.png")
            }
            else if (idade > 14 && idade < 21) {
                img.setAttribute("src","imagens/modified/jovem-f.png")
            }
            else if (idade > 21 && idade < 60) {
                img.setAttribute("src","imagens/modified/adulto-f.png")
            }
            else {
                img.setAttribute("src","imagens/modified/velho-f.png")
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${genero} com ${idade} anos<br>`
        res.appendChild(img)

    }
}