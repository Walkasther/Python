document.addEventListener('DOMContentLoaded', () => {
    // Mapeamento das telas
    const screens = {
        products: document.getElementById('screen-products'),
        quantity: document.getElementById('screen-quantity'),
        // qrCode: document.getElementById('screen-qrcode'), // Futuras telas
    };

    // Função para navegar entre as telas
    function navigateTo(screenName) {
        Object.values(screens).forEach(screen => {
            screen.classList.remove('active');
        });
        if (screens[screenName]) {
            screens[screenName].classList.add('active');
        }
    }

    // --- Lógica da Tela de Produtos ---
    const productCards = document.querySelectorAll('.product-card');
    productCards.forEach(card => {
        card.addEventListener('click', () => {
            const productName = card.getAttribute('data-product-name');
            // Atualiza o nome do produto na próxima tela
            document.getElementById('selected-product-name').textContent = productName;

            // Navega para a tela de quantidade
            navigateTo('quantity');
        });
    });

    // --- Lógica da Tela de Quantidade ---
    const btnBackToProducts = document.getElementById('btn-back-to-products');
    btnBackToProducts.addEventListener('click', () => {
        navigateTo('products');
    });

    // Simulação da navegação para a próxima tela (QR Code)
    const btnToQrCode = document.getElementById('btn-to-qrcode');
    btnToQrCode.addEventListener('click', () => {
        alert('Navegando para a tela de QR Code (a ser implementada)');
        // navigateTo('qrCode');
    });

    // Lógica dos botões de quantidade (a ser detalhada)
    // ...

});
