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
            </form>
        `;
    
        Swal.fire({
            title: 'Formulario en SweetAlert',
            html: formHTML,
            showCancelButton: true,
            confirmButtonText: 'Enviar',
            showLoaderOnConfirm: true,
            preConfirm: () => {
                // Obtener los valores del formulario
                let inputFieldValue = document.getElementById('inputField').value;
                let data = new FormData()
                data.append("csrfmiddlewaretoken", token);
                data.append("inputField", inputFieldValue)
    
                // Realizar la solicitud Fetch con los datos del formulario
                return fetch(`/${pk}/choice/add/`, {
                    method: 'POST',
                    body: data,
                   
                })
                .then(response => {
                    if (!response.succes) {
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
                Swal.fire('Respuesta del servidor', result.message, 'success');
            }
        });
    }
    
});



// function create_post() {
//     console.log("create post is working!") // sanity check
//     $.ajax({
//         url : "create_post/", // the endpoint
//         type : "POST", // http method
//         data : { the_post : $('#post-text').val() }, // data sent with the post request

//         // handle a successful response
//         success : function(json) {
//             $('#post-text').val(''); // remove the value from the input
//             console.log(json); // log the returned json to the console
//             console.log("success"); // another sanity check
//         },

//         // handle a non-successful response
//         error : function(xhr,errmsg,err) {
//             $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
//                 " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
//             console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
//         }
//     });
// };