const url_de_la_api = 'https://jsonplaceholder.typicode.com/todos/'

let page = 1; // Variable para realizar el seguimiento de la página actual
const limit = 60; // Número de elementos a cargar en cada solicitud


window.addEventListener('scroll', () => {
    const { scrollTop, scrollHeight, clientHeight } = document.documentElement;

    if (scrollTop + clientHeight >= scrollHeight) {
        // Aquí se realiza una petición para cargar más contenido
        // Puedes utilizar AJAX, Fetch API o alguna otra técnica para obtener nuevos datos
        fetch(`https://jsonplaceholder.typicode.com/todos?_page=${page}&_limit=${limit}`)
        .then(response => response.json())
        .then(data => {
            data.forEach(todo => {
                const newContent = document.createElement('div');
                newContent.innerHTML = 
                    `
                    <div class='element'>
                        <h3>Title: ${todo.title} </h3>
                        <p class=${todo.completed}> <strong>Completed:</strong> ${todo.completed}</p>
                        <p class='id'> ID: ${todo.id}</p>
                     </div>`;
                document.getElementById('content').appendChild(newContent);
            });

            page++;
        })
        .catch(error => {
            console.error('Error al obtener nuevos datos:', error);
        });
    }
});
