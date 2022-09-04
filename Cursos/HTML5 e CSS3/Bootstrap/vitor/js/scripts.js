var paragrafos = document.getElementsByTagName('p')
var body = document.getElementById('corpo')
var div_tom_dif = document.getElementById('tom_dif')

console.log(body)

p_size = 1.2

function aumentar(){
    p_size += 0.25
    for(p of paragrafos){
        p.style.fontSize = p_size + 'em'; 
    }
}

function diminuir(){
    p_size -= 0.25
    for(p of paragrafos){
        p.style.fontSize = p_size + 'em'; 
    }
}

function tema_escuro(){

    //body.classList.add('bg-dark')
    body.style.background = '#15202B'
    div_tom_dif.style.background = '#1D2A35'

    for(p of paragrafos){
        p.style.color = 'white'
    }
    
    
}