var hora_do_sistema = new Date()
var hora = hora_do_sistema.getHours()
console.log (`Agora são exatamente ${hora} horas.`)
if (hora > 0 && hora < 6 || hora > 18){ 
    console.log('Boa noite!')
}
else if (hora < 12){
    console.log('Boa dia!')
}
else{
    console.log('Boa tarde!')
}