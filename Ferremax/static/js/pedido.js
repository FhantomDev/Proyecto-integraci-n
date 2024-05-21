document.addEventListener('DOMContentLoaded', () => {

    const total = localStorage.getItem('total-compra')
    const pesos = document.querySelector('#pesos')
    const monto = document.querySelector('#monto')

    pesos.textContent = total;
    monto.value = total;
    numerosRandom()
})

function numerosRandom() {
    const ordenTxt = document.querySelector('#orden_txt')
    const ordenV = document.querySelector('#orden_value')
    const sesionTxt = document.querySelector('#sesion_txt')
    const sesionV = document.querySelector('#sesion_value')

    let randomOrden = Math.floor(Math.random() * (90000000 - 10000000 + 1)) + 10000000;
    console.log(randomOrden)
    ordenTxt.textContent = randomOrden;
    ordenV.value = randomOrden;

    let randomSesion = Math.floor(Math.random() * (90000000 - 10000000 + 1)) + 10000000;
    console.log(randomSesion)
    sesionTxt.textContent = randomSesion;
    sesionV.value = randomSesion;
}