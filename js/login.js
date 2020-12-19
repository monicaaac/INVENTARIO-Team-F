function validate(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if ( username == "Maguileraa" && password == "password1"){
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