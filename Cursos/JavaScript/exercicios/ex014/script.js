lib_date = new Date
hours = lib_date.getHours()
minutes = lib_date.getMinutes()
seconds = lib_date.getSeconds()
sec_modified = document.getElementsByTagName('section')[0]
body_modified = document.getElementsByTagName('body')[0]
sec_modified.innerHTML = `<h3>${hours}:${minutes}:${seconds}</h3>`

if (hours > 0 && hours < 6 || hours > 18) {
    sec_modified.innerHTML += `<img src="imagens/modified/noite.png" alt="Noite">`
    body_modified.style.background = '#01021b'
    sec_modified.style.background = '#000000b6'
}

else if (hours < 12) {
    sec_modified.innerHTML += `<img src="imagens/modified/manha.png" alt="Amanhecer">`
    body_modified.style.background = '#5fc5c5c7'
}

else {
    sec_modified.innerHTML += `<img src="imagens/modified/entardecer.png" alt="Entardecer">`
    body_modified.style.background = '#c56c30e0'
}