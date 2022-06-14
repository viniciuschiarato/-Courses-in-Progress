lib_date = new Date
hora = lib_date.getHours()
//hora = 15
sec_modified = document.getElementsByTagName('section')[0]
body_modified = document.getElementsByTagName('body')[0]
sec_modified.innerHTML = `<h3>Agora são ${hora} horas</h3>`

if (hora > 0 && hora < 6 || hora > 18) {
    sec_modified.innerHTML += `<img src="imagens/modified/noite.png" alt="Noite">`
    body_modified.style.background = '#01021b'
    sec_modified.style.background = '#000000b6'
}
else if (hora < 12) {
    sec_modified.innerHTML += `<img src="imagens/modified/manha.png" alt="Amanhecer">`
    body_modified.style.background = '#5fc5c5c7'
}
else {
    sec_modified.innerHTML += `<img src="imagens/modified/entardecer.png" alt="Entardecer">`
    body_modified.style.background = '#c56c30e0'
}