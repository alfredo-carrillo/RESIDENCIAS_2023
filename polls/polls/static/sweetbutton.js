let pk = window.location.pathname.substring(1, 3)
// script.js

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

let token = getCookie("csrftoken");
console.log(token);

document.addEventListener("DOMContentLoaded", function() {
    // Obtener el botón por su ID
    let choiceFormButton = document.getElementById("add_fields");

    // Agregar un evento de clic al botón
    choiceFormButton.addEventListener("click", function() {
        showSweetAlert();
    });

    function showSweetAlert() {
        // Crear un formulario personalizado en HTML
        let formHTML = `
            <form id="custom-form">
                <label for="inputField">Campo de entrada:</label>
                <input type="text" id="inputField" name="inputField">
            </form>`;
    
        Swal.fire({
            title: 'Agrega nuevas Opciones',
            html: formHTML,
            showCancelButton: true,
            confirmButtonText: 'Enviar',
            showLoaderOnConfirm: true,
            preConfirm : async (data_object) => {
                // Obtener los valores del formulario
                let inputFieldValue = document.getElementById('inputField').value;
                let data = new FormData()
                data.append("csrfmiddlewaretoken", getCookie("csrftoken"));
                data.append("inputField", inputFieldValue)
    
                // Realizar la solicitud Fetch con los datos del formulario
                let reques = await fetch(`/${pk}/choice/add/`, {
                    method: 'POST',
                    body: data,
                    
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('La solicitud no se pudo completar');
                    }
                    return response.json();
                })
                .then(data => {
                    return data;
                })
                .catch(error => {
                    Swal.showValidationMessage(`Error: ${error}`);
                });
            },
            allowOutsideClick: () => !Swal.isLoading()
        })
        .then(result => {
            if (result.isConfirmed) {
                Swal.fire('Respuesta del servidor', result.value.message, 'success');
            }
        });
    }

});
