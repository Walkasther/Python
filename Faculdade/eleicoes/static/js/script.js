function atualizarCampo() {
                const select = document.getElementById('tipo_candidato');
                const input = document.getElementById('numero');

                if ((select.value === 'prefeito') || (select.value === 'governador') || (select.value === 'presidente')) {
                    input.min = 10;
                    input.max = 99;
                    input.oninput = function () {
                        if (this.value.length > 2) this.value = this.value.slice(0, 2);
                    };
                } else if ((select.value === 'vereador') || (select.value === 'deputado_estadual')) {
                    input.min = 10000;
                    input.max = 99999;
                    input.oninput = function () {
                        if (this.value.length > 5) this.value = this.value.slice(0, 5);
                    };
                } else if (select.value === 'senador') {
                    input.min = 100;
                    input.max = 999;
                    input.oninput = function () {
                        if (this.value.length > 3) this.value = this.value.slice(0,3);
                    }
                } else if (select.value === 'deputado_federal') {
                    input.min = 1000;
                    input.max = 9999;
                    input.oninput = function () {
                        if (this.value.length > 4) this.value = this.value.slice(0,4);
                    }
                }
}

function validarTamanho(input) {
    // Limita o valor ao máximo permitido pelo atributo `max`.
    const maxLength = input.max.toString().length;
    if (input.value.length > maxLength) {
        input.value = input.value.slice(0, maxLength);
    }
}

function validarFormulario(event) {
    const input = document.getElementById('numero');
    const valor = input.value;
    const cargo = document.getElementById('cargo').value;

    if (valor.length === 0) {
        alert("O número do candidato não pode estar vazio.");
        event.preventDefault(); // Cancela o envio do formulário
        return false;
    }

    if (cargo === 'prefeito' && valor.length !== 2) {
        alert("Número inválido: o número do prefeito deve ter exatamente 2 dígitos.");
        event.preventDefault(); // Cancela o envio do formulário
        return false;
    }

    if (cargo === 'vereador' && valor.length !== 5) {
        alert("Número inválido: o número do vereador deve ter exatamente 5 dígitos.");
        event.preventDefault(); // Cancela o envio do formulário
        return false;
    }

    return true; // Permite o envio
}




