const sueldoBruto =  document.getElementById('sueldoBrutoInput')
const seguroDeVida = document.getElementById('seguroInput')
const perAportes = document.getElementById('aportes')

const alquiler = document.getElementById('alquilerInput')
const expensas = document.getElementById('expensasInput')
const otros = document.getElementById('otrosInput')

var arregloDeIngresos = []

function handleClickCalculate(){
    const perc = (perAportes.value * sueldoBruto.value)/100
    const laborales = (sueldoBruto.value - seguroDeVida.value - perc ) 
    const impuestos = (Number(alquiler.value) + Number(expensas.value) + Number(otros.value))
   
    
    //const pasivos = ingresosPasivos.reduce((v, el) => v + Number(el.ingresos), 0)
    alert (`Sus ingresos netos seran de: ${laborales  - impuestos}$`)
}

function agregarObjeto(event) {
    event.preventDefault();
    // Obtiene los valores del formulario
    var nombre = document.getElementById('nombre').value;
    var valor = document.getElementById('valor').value;
  
    // Crea un nuevo objeto y lo agrega al arreglo
    var nuevoObjeto = {
      nombre: nombre,
      valor: parseInt(valor)
    };
    arregloDeIngresos.push(nuevoObjeto);
  
    // Actualiza la lista de objetos en el HTML
    actualizarListaObjetos();
  
    // Limpia los campos del formulario
    document.getElementById('nombre').value = '';
    document.getElementById('valor').value = '';
  }

// Función para actualizar la lista de objetos en el HTML
function actualizarListaObjetos() {
    var listaObjetos = document.getElementById('listaObjetos');
    listaObjetos.innerHTML = ''; // Limpia la lista actual
  
    // Itera sobre el arreglo de objetos y crea los elementos de la lista
    for (var i = 0; i < arregloDeIngresos.length; i++) {
      var objeto = arregloDeIngresos[i];
      var listItem = document.createElement('li');
      listItem.textContent = 'Nombre: ' + objeto.nombre + ', Valor: ' + objeto.valor;
      arregloDeIngresos.push(listItem);
    }
    console.log(arregloDeIngresos)
  }
  
  // Agrega un event listener al formulario para llamar a la función agregarObjeto
  document.getElementById('formulario').addEventListener('submit', agregarObjeto);