$(document).ready(function() {
  // Manejar el envío del Formulario 1
  $("#choice_form").submit(function(event) {
      event.preventDefault();
      
      // Recopilar los datos del formulario 1
      var form_choice = {
          campo1: $("#choice_form input[name ='choice_text']").val(),
          campo2: $("#choice_form input[name ='votes']").val()
      };

     

      // Mostrar los datos en un SweetAlert
      Swal.fire({
          title: 'Datos del Formulario 1',
          text: 'Campo 1: ' + form_choice.campo1,
          text: 'Campo 2: ' + form_choice.campo2,
          icon: 'info'
      });
  });
});