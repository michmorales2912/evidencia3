console.log("Script para la página principal cargado correctamente.");

console.log("Script para la página de menú cargado correctamente.");

console.log("Script para la página de sistema de pedidos cargado correctamente.");

console.log("Script para la página de realizar pedido cargado correctamente.");

function addToOrder() {
    var selectedItem = document.getElementById('order-item').value;
    var quantity = document.getElementById('quantity').value;

    console.log(`Añadido al pedido: ${quantity} x ${selectedItem}`);
}
