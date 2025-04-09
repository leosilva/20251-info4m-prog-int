function trocarLampada() {
	var imgLampada = document.getElementById("lampada");
	if (imgLampada.src.includes("off")) {
		imgLampada.src = "http://www.w3schools.com/js/pic_bulbon.gif"
	} else {
		imgLampada.src = "http://www.w3schools.com/js/pic_bulboff.gif"
	}
}