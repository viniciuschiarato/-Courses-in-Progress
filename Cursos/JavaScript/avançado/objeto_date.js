//Objeto date

//js trabalha com milésimos de segundos

const umaHora = 60 * 60 * 1000// 60 segundos 60 vezes, o mil pq o js interpreta o valar como milisegundos.

const tresHoras = 60 * 60 * 3 * 1000// 1 hora vezes três.

const dataAtual = new Date(); //data atual.

//console.log(dataAtual.toString());

const data = new Date(0 + tresHoras); //data 0 Timestamp Unix.

//console.log(data.toString());

const dataDefinida1 = new Date(2019, 0, 20, 15, 14, 27, 999); // 999 são os milésimos de segundos e o mês começa no 0.

//console.log(dataDefinida1.toString());

const dataDefinida2 = new Date(2019, 3, 20);// para uma data definida não é necessario informa a hora o js só precisa do ano e do mês.

//console.log(dataDefinida2.toString()); 

//  Formatos:
//  a m d h mn s ms (números)
//  'a m d T h mn s' (strings) // Pode ser a letra T OU um espaço

const dataDefinida3 = new Date('2019-04-20T20:20:59');

console.log(dataDefinida3.toString()); 

//13:00

// MDN --> https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Date