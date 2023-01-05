/*function comparador(){
    numQuestoes = Number(document.getElementById('numQuestoes').value)
    saida = document.getElementById('saida')
    gabaritoProva = []
    gabaritoAluno = []
    let contador = 0
    do{
        saida.innerHTML = `
        <p>
        <label for="respostaCerta">Informe a resposta da questão ${contador} </label>
        <input type="text" id="respostaCerta" placeholder="A,B,C,D ou E?">
        </p>
        <input type="submit" value="Próximo" formaction="javascript:adicionar()">
        `
        contador++
        var input = document.getElementById('respostaCerta')
        //gabaritoProva.push(input)
        alert(input)

    }while(contador <= numQuestoes)
    

}*/

gabaritoProva = []
gabaritoAluno = []
let contador = 0
do{
    
    contador++
}while(contador <= numQuestoes)