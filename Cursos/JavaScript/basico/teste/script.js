var texto = document.getElementsByClassName("texto")
let i=1
function aumentar(){
    i++
    for(p of texto){
        p.style.fontSize = i+'em'; 
    }
}
