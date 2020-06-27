var massa = document.getElementById("massa");
var altura = document.getElementById("altura");
var imc = massa/(altura*altura);

function bot (){
    document.getElementById("resultado").innerHTML = "<b>Seu IMC é :</b>"imc;
}
