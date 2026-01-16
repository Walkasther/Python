document.addEventListener("DOMContentLoaded", () => {
    const container = document.querySelector(".container"); // Div principal que vai conter os inputs

    // Função para buscar o tipo de eleição no backend
    const obterTipoEleicao = async () => {
        try {
            const response = await fetch("/obter_tipo_eleicao"); // Rota para consultar o tipo de eleição
            const data = await response.json();

            if (data.tipoEleicao) {
                renderizarCampos(data.tipoEleicao);
            } else {
                alert("Erro: Não foi possível determinar o tipo da eleição.");
            }
        } catch (error) {
            console.error("Erro ao obter o tipo de eleição:", error);
            alert("Erro ao conectar com o servidor. Tente novamente.");
        }
    };

    // Função para criar dinamicamente os campos com base no tipo de eleição
    const renderizarCampos = (tipoEleicao) => {
        // Limpa o container para evitar duplicações
        container.innerHTML = "";

        // Define o número de etapas baseado no tipo de eleição
        const etapas = tipoEleicao === "presidente" ? 5 : 2;
        const cargos = tipoEleicao === "presidente"
            ? ["Deputado Estadual", "Deputado Federal", "Senador", "Governador", "Presidente"]
            : ["Vereador", "Prefeito"];

        // Cria dinamicamente os campos
        for (let i = 0; i < etapas; i++) {
            const div = document.createElement("div");
            div.className = "campo-voto";

            const label = document.createElement("label");
            label.textContent = `Digite o número do candidato para ${cargos[i]}:`;
            label.setAttribute("for", `candidato-${i}`);

            const input = document.createElement("input");
            input.type = "number";
            input.id = `candidato-${i}`;
            input.name = `candidato-${i}`;
            input.required = true;

            div.appendChild(label);
            div.appendChild(input);

            container.appendChild(div);
        }
    };

    // Chama a função ao carregar a página
    obterTipoEleicao();
});
