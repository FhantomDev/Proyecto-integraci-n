document.addEventListener('DOMContentLoaded', () => {

    const total = localStorage.getItem('total-compra')
    const pesos = document.querySelector('#pesos')
    pesos.textContent = total;

})