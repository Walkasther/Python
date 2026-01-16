document.addEventListener("DOMContentLoaded", () => {
    const tituloInput = document.getElementById("titulo_eleitor");
    const verificarTituloButton = document.getElementById("verificar_titulo");
    const campoTitulo = document.getElementById("campo-titulo");
    const campoVotacao = document.getElementById("campo-votacao");
    const etapaLabel = document.getElementById("etapa-label");
    const numeroCandidatoInput = document.getElementById("numero-candidato");
    const confirmarVotoButton = document.getElementById("confirmar-voto");

    // Sequência de votação
    let tipoEleicao = ""; // presidente ou prefeito
    let etapas = [];
    let etapaAtual = 0;

    // Simula verificar o título de eleitor no backend
    verificarTituloButton.addEventListener("click", () => {
        const titulo = tituloInput.value.trim();

        if (titulo === "") {
            alert("Por favor, insira um título de eleitor válido.");
            return;
        }

        // Simulação de verificação do título no backend
        fetch(`/verificar_titulo?titulo=${titulo}`)
            .then(response => response.json())
            .then(data => {
                if (data.votou) {
                    alert("Você já votou nesta eleição.");
                } else {
                    // Inicia o processo de votação
                    tipoEleicao = data.tipoEleicao; // 'presidente' ou 'prefeito'
                    etapas = tipoEleicao === "presidente"
                        ? ["Deputado Estadual", "Deputado Federal", "Senador", "Governador", "Presidente"]
                        : ["Vereador", "Prefeito"];

                    etapaAtual = 0; // Começa na primeira etapa
                    campoTitulo.style.display = "none"; // Esconde campo do título
                    campoVotacao.style.display = "block"; // Mostra campo de votação
                    carregarEtapa();
                }
            })
            .catch(err => {
                console.error(err);
                alert("Erro ao verificar o título. Tente novamente.");
            });
    });

    // Carrega a etapa atual
    const carregarEtapa = () => {
        if (etapaAtual < etapas.length) {
            etapaLabel.textContent = `Votando para: ${etapas[etapaAtual]}`;
            numeroCandidatoInput.value = ""; // Limpa o campo
        } else {
            alert("Obrigado por votar!");
            document.getElementById("form-votacao").submit();
        }
    };

    // Confirma o voto na etapa atual
    confirmarVotoButton.addEventListener("click", () => {
        const numero = numeroCandidatoInput.value.trim();

        if (numero === "") {
            alert("Por favor, insira o número do candidato.");
            return;
        }

        // Simula o envio do voto para o backend
        fetch(`/votar`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                tipo: etapas[etapaAtual],
                numero: numero,
            }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                etapaAtual++;
                carregarEtapa();
            } else {
                alert(data.message || "Erro ao registrar voto. Tente novamente.");
            }
        })
        .catch(err => {
            console.error(err);
            alert("Erro ao processar o voto. Tente novamente.");
        });
    });
});
