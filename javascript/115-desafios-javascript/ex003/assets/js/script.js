//Crie um programa que leia dois números e mostre a soma entre eles.

const form = document.querySelector('.form');
const resposta = document.querySelector('.resposta');

form.addEventListener('submit', somar);

function somar(evento) {
    evento.preventDefault();

    const num1 = form.querySelector('#num1').value;
    const num2 = form.querySelector('#num2').value;

    if (Number(num1.length) === 0 || Number(num2.length) === 0) {
        resposta.innerHTML = "Digite os dois número para realizar a soma";
        resposta.style.background = "#ff6961";
        resposta.style.color = "#fff";
    } else {
        const soma = Number(num1) + Number(num2);
        resposta.innerHTML = `A soma de ${num1} + ${num2} = ${soma}`;
        resposta.style.background = "none";
        resposta.style.color = "#000";

        form.querySelector('#num1').value = "";
        form.querySelector('#num2').value = "";
    }
}


form.addEventListener('reset', limpar);

function limpar(evento) {
    evento.preventDefault();

    form.querySelector('#num1').value = "";
    form.querySelector('#num2').value = "";

    resposta.innerHTML = "";
    resposta.style.background = "none";
    resposta.style.color = "#000";
}
