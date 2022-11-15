//exemplo de uma lampada
function alterarEstado() {
    var lampada = document.getElementById('lampada');

    if(lampada.classList.contains("apagada")) {

        lampada.classList.add("ligada");

        lampada.classList.remove("apagada");

        lampada.src = "https://i.stack.imgur.com/ybxlO.jpg";
    }else if(lampada.classList.contains("ligada")) {

        lampada.classList.add("apagada");

        lampada.classList.remove("ligada");

        lampada.src = "https://i.stack.imgur.com/b983w.jpg";
    }
}

var texto = document.createElement("p");
texto.innerHTML = "Exemplo de Javascript";

document.getElementById("content").appendChild(texto);