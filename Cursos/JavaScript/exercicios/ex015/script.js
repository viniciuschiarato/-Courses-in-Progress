function verification(){
    var date = new Date()
    var current_year = date.getFullYear()
    var input_year = document.getElementById('txt_yo')
    var div_output = document.querySelector('div#output')
    if (input_year.value.length == 0 || input_year.value > current_year){
        alert('Dados incorretos. Digite novamente')
    }
}
