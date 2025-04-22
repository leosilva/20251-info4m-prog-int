function imprimirMultiplos() {
	for (var i = 1; i <= 50; i++) {
		if (i % 4 == 0) {
			document.write("MULTIPLO");
		} else {
			document.write(i);
		}
		document.write("<br/>");
	}
}