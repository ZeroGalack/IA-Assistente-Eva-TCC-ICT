const output = document.querySelector('#output');
window.addEventListener('DOMContentLoaded', function() {

var audio = '';
var gravando = false;

if (window.SpeechRecognition || window.webkitSpeechRecognition) {

    var speech_api = window.SpeechRecognition || window.webkitSpeechRecognition;
    var gravar_audio = new speech_api();

    gravar_audio.continuous = false;
    gravar_audio.interimResults = false;
    gravar_audio.lang = "pt-br";

    gravar_audio.onstart = function () {
        gravando = true;
    };

    gravar_audio.onend = function () {
        gravar_audio.start();
        gravando = false;
    };
    gravar_audio.onresult = function (event) {
    audio = event.results[0][0].transcript;
    output.textContent = audio;

    audio = audio.normalize('NFD').replace(/[\u0300-\u036f]/g, "");
    console.log(audio);

    fetch("https://test7.lucasteixeira23.repl.co/r", {
      method: "POST",
      headers: {
        "Content-Type": "application/json", },
      body: JSON.stringify(audio),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", audio); })
      .catch((error) => {
        console.error("Error:", error); });



    if(audio.toLowerCase() === "gravar"){
        document.getElementById("btn-gravar-audio").click();
        gravar_audio.onend = function () {
        gravando = false; }; } };

    if (gravando) {
        gravar_audio.stop();
        return; }
    gravar_audio.start();
}
else {
    console.log("navegador não apresenta suporte a web speech api");}}, false);