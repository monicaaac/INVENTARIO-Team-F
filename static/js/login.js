function validate(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if ( username == "Monica" && password == "password1"){
    alert ("Ingreso Exitoso");
         }
         else{
           alert("Clave o Usuario Invalido");
           }
         return false;
         }



function request_email (valor){
	re=/^([\da-z_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/
	if(!re.exec(valor)){
		alert('email no valido');
	}
	else alert('email valido, el correo ha sido enviado!!');
  }


  //validar formulario

  function validar_formulario(){
    var usuario = document.getElementById("username");
    var correo = document.getElementById("email");
    var clave = document.getElementById("password");
        
    var usuario_len = usuario.value.length;
    if(usuario_len == 0 || usuario_len < 8)
    {
        alert("Debes ingresar un usuario con mínimo 8 caracteres");
        // passid.focus();
        return false; //Para la parte dos, que los datos se conserven
    }

    var formatoCorreo = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if(!correo.value.match(formatoCorreo))
    {
        alert("Debes ingresar un correo electronico valido!");
        // correo.focus();
        return false; //Para la parte dos, que los datos se conserven
    }
    
    var passid_len = clave.value.length;

    if (passid_len == 0 || passid_len < 8)
    {
        alert("Debes ingresar una clave con mas de 8 caracteres");
        // passid.focus();
        return false;
    }

}

function mostrarPassword() {
    var obj = document.getElementById('password');
    obj.type = "text";
}

function ocultarPassword() {
    var obj = document.getElementById('password');
    obj.type = "password";
}