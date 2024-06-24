document.addEventListener('DOMContentLoaded', () => {

    const total = localStorage.getItem('total-compra')
    const productos = JSON.parse(localStorage.getItem('carrito'))

    const pesos = document.querySelector('#pesos')
    const monto = document.querySelector('#monto')
    const dolar = document.querySelector('#dolar')
    const euro = document.querySelector('#euro')
    const valorDolar = document.querySelector('#valor-dolares')
    const valorEuro = document.querySelector('#valor-euro')
    const divProductos = document.querySelector('#productos')

    const dolares_obtenidos = total * (1 / dolar.textContent)
    const euros_obtenidos = total * (1 / euro.textContent)

    pesos.textContent = total;
    monto.value = total;
    valorDolar.textContent = dolares_obtenidos.toFixed(2)
    valorEuro.textContent = euros_obtenidos.toFixed(2)
    
    numerosRandom()

    productos.forEach(producto => {
        const nombre = document.createElement('p');
        const cantidad = document.createElement('p');

        nombre.textContent = producto.nombre;
        cantidad.textContent = producto.cantidad;

        divProductos.appendChild(nombre)
        divProductos.appendChild(cantidad)
    });

    console.log(productos)
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