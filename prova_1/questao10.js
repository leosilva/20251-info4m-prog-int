function trocarTexto() {
    var texto1 = $("#div1").innerHTML
    var texto2 = $("#div2").innerHTML

    $("#div1").innerHTML = texto2
    $("#div2").innerHTML = texto1
}