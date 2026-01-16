const formSessao = document.getElementById('form-sessao');
const formUpload = document.getElementById('form-upload');
const codigoSessao = document.getElementById('codigo-sessao');
const formUpload = document.getElementById('form-upload');


formSessao.addEventListener('submit', async (e) => {
    e.preventDefault();
    const quiosqueId = document.getElementById('quiosque-id').value;
    const response = await fetch('/api/sessoes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ quiosque_id: quiosqueId })
    });
    const data = await response.json();
    codigoSessao.textContent = `Código da Sessão: ${data.codigo_sessao}`;
});

formUpload.addEventListener('submit', async (e) => {
    e.preventDefault();
    const foto = document.getElementById('foto').files[0];
    const formData = new FormData();
    formData.append('foto', foto);
    const response = await fetch('/api/upload', {
        method: 'POST',
        body: formData
    });
    const data = await response.json();
    console.log(data);
});



