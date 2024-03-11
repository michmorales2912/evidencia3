// index.js
console.log("Script para la página principal cargado correctamente.");

// menu.js
console.log("Script para la página de menú cargado correctamente.");

// sistema_pedidos.js
console.log("Script para la página de sistema de pedidos cargado correctamente.");

// realizar_pedido.js
console.log("Script para la página de realizar pedido cargado correctamente.");

// Función para añadir elementos al pedido en realizar_pedido.html
function addToOrder() {
    var selectedItem = document.getElementById('order-item').value;
    var quantity = document.getElementById('quantity').value;

    // Aquí puedes realizar acciones adicionales al añadir elementos al pedido
    console.log(`Añadido al pedido: ${quantity} x ${selectedItem}`);
}
