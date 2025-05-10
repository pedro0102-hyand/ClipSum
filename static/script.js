async function atualizar() {
    try {
        const resposta = await fetch('/get_data');
        const dados = await resposta.json();
        document.getElementById('original').value = dados.original;
        document.getElementById('resumo').value = dados.summary;
    } catch (erro) {
        console.error("Erro ao buscar dados:", erro);
    }
}

setInterval(atualizar, 3000); // atualiza a cada 3 segundos
