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