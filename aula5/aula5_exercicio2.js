function imprimirTabuada() {
	var num = parseInt(prompt("Digite o numero"));
	for (var i = 1; i <= 10; i++) {
		resultado = num * i;
		document.write(i + " x " + num + " = " + resultado + "<br/>")
	}
}