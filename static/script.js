function validar() {
    const usuario = document.getElementById("name").value;
    const password = document.getElementById("password").value;
    if (usuario === "" || password === "") {
        alert("Porfavor rellene el formulario");
        return false;
    }
    return true;
}
function TooglePassword() {
    const input = document.getElementById("password");
    if (input.type === "password") {
        input.type = "text";
    } else {
        input.type = "password"
    }
}
function validar_crear() {
    const titulo = document.getElementById("titulo").value;
    const contenido = document.getElementById("contenido").value;
    if (titulo === "" || contenido === "") {
        alert("Porfavor rellenar el formulario");
        return false;
    }
    return true;
}