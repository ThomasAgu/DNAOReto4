var itemsContainer = document.getElementById('items-container');
var index = 0; // Índice para recorrer los elementos

// Función para realizar la solicitud a la API y obtener los datos
function fetchData() {
    // URL de la API de JSONPlaceholder para obtener los todos
    var apiUrl = 'https://jsonplaceholder.typicode.com/todos';

    // Realizar la solicitud GET a la API
    fetch(apiUrl)
        .then(response => response.json())
        .then(responseData => {
            // Mostrar los primeros elementos
            addItemsToContainer(responseData);
        })
        .catch(error => {
            console.log('Error al obtener los datos de la API:', error);
        });
}

// Función para agregar elementos al contenedor
function addItemsToContainer(data) {
    // Obtener el rango de elementos para mostrar
    var startIndex = index;
    var endIndex = index + 3; // Mostrar 3 elementos por fila

    // Recorrer los elementos y agregarlos al contenedor
    for (var i = startIndex; i < endIndex; i++) {
        var item = document.createElement('div');
        item.classList.add('item');
        item.textContent = data[i].title; // Mostrar el título de cada elemento (puedes personalizarlo según los datos que necesites)
        itemsContainer.appendChild(item);
    }

    // Actualizar el índice
    index += 3;

    // Si se llega al final de los datos, reiniciar la visualización
    if (index >= data.length) {
        index = 0;
    }
}

// Función para verificar si se llegó al final de la página y agregar más elementos
function checkScroll() {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        fetchData();
    }
}

// Detectar el evento de scroll
window.addEventListener('scroll', checkScroll);

// Llamar a la función para obtener los datos de la API
fetchData();