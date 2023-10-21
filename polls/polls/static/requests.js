// Supongamos que la vista está en la URL '/mi_ruta/' en tu sitio de Django
const url = '/main/';

fetch(url)
  .then(response => {
    if (response.ok) {
      return response.text(); // Puedes usar .json() en lugar de .text() si esperas una respuesta en formato JSON
    }
    throw new Error('Error en la respuesta del servidor');
  })
  .then(data => {
    // Manipula los datos recibidos, por ejemplo, insertándolos en el DOM
    console.log(data);
  })
  .catch(error => {
    // Maneja los errores
    console.error(error);
  });