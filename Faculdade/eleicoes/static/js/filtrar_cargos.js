document.addEventListener('DOMContentLoaded', () => {
    const cargos = document.getElementById("tipo_candidato");

    // Opções disponíveis para cada tipo de eleição
    const opcoes = {
        prefeito: [
            { value: "prefeito", text: "Prefeito" },
            { value: "vereador", text: "Vereador" },
        ],
        presidente: [
            { value: "presidente", text: "Presidente" },
            { value: "senador", text: "Senador" },
            { value: "governador", text: "Governador" },
            { value: "deputado_federal", text: "Deputado Federal" },
            { value: "deputado_estadual", text: "Deputado Estadual" },
        ],
    };

    // Buscar o tipo de eleição no banco de dados
    fetch('/verificar_ou_inserir', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ tipo_eleicao: null }) // Apenas consulta
    })
        .then(response => response.json())
        .then(data => {
            console.log("Resposta do backend:", data);

            let tipoEleicao;

            if (data.status === "exists") {
                // Tipo já registrado no banco
                tipoEleicao = data.tipo_eleicao;
                console.log("Tipo de eleição encontrado:", tipoEleicao);
            } else {
                // Tipo não encontrado, exibir o popup para seleção

                function mostrarPopup() {
                    // Mostra um elemento popup no HTML
                    const popup = document.getElementById('popup');
                    if (popup) {
                        popup.style.display = 'block'; // Torna o popup visível
                    } else {
                        console.error("Elemento de popup não encontrado!");
                    }
                }

                function fecharPopup() {
                    // Esconde o elemento popup no HTML
                    const popup = document.getElementById('popup');
                    if (popup) {
                        popup.style.display = 'none'; // Torna o popup invisível
                    } else {
                        console.error("Elemento de popup não encontrado!");
                    }
                }

                mostrarPopup();
                document.getElementById('confirmarEleicao').addEventListener('click', () => {
                    tipoEleicao = document.querySelector('input[name="tipoEleicao"]:checked').value;

                    // Salvar a escolha no banco
                    fetch('/verificar_ou_inserir', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ tipo_eleicao: tipoEleicao })
                    })
                        .then(response => response.json())
                        .then(data => {
                            console.log(data.message);
                            fecharPopup();
                            atualizarTextoETipo(tipoEleicao);
                        })
                        .catch(error => {
                            console.error('Erro ao enviar dados:', error);
                        });
                });
            }

            // Atualizar o texto e os cargos com o tipo de eleição (independente do popup)
            if (tipoEleicao) {
                atualizarTextoETipo(tipoEleicao);
            }
        })
        .catch(error => {
            console.error('Erro ao verificar tipo de eleição:', error);
        });

    // Função para atualizar o texto e os cargos
    function atualizarTextoETipo(tipoEleicao) {
        // Atualizar o texto
        const textoEscolha = document.getElementById("texto_escolha");
        if (textoEscolha) {
            textoEscolha.textContent = `Eleições para ${tipoEleicao.charAt(0).toUpperCase() + tipoEleicao.slice(1)}`;
        } else {
            console.error("Elemento com ID 'texto_escolha' não encontrado.");
        }

        // Atualizar as opções do campo "cargos"
        atualizarCargos(tipoEleicao);
    }

    // Função para atualizar os cargos no dropdown
    function atualizarCargos(tipo) {
        // Remove todas as opções existentes
        cargos.innerHTML = "";

        // Adiciona as opções correspondentes ao tipo selecionado
        opcoes[tipo].forEach(opcao => {
            const option = document.createElement("option");
            option.value = opcao.value;
            option.textContent = opcao.text;
            cargos.appendChild(option);
        });
    }
});
