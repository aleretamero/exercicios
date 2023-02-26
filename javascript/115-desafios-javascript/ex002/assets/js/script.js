//Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

function meuEscopo() {
    const form = document.querySelector('.form');
    form.addEventListener('submit', boasVindas);
    form.addEventListener('reset', limpar );

    function boasVindas(evento) {
        evento.preventDefault();

        const nome = form.querySelector('#idNome').value;
        const msg = document.querySelector('.two');

        if (Number(nome.length) === 0) {
            window.alert('Por favor, digite um nome!');
            msg.innerHTML = "";
        } else {
            msg.innerHTML = `Seja bem vindo(a) <br/>${nome}.`;
            document.querySelector('#idNome').value = "";
        }
    }

    function limpar(evento) {
        evento.preventDefault();

        const nome = form.querySelector('#idNome').value;
        const msg = document.querySelector('.two');

        document.querySelector('#idNome').value = "";
        msg.innerHTML = "";
    }
}

meuEscopo();
