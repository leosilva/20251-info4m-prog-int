function calcularMedia() {
    var n1 = $("#nota1").val()
    var n2 = $("#nota2").val()
    var n3 = $("#nota3").val()
    var n4 = $("#nota4").val()

    media = (n1 + n2 + n3 + n4) / 4

    $("#media").val(media)
}