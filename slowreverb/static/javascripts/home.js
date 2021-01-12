var convertBtn = document.querySelector('.convert-button'); // convert button
var URLinput = document.querySelector('.url-input');        // url input
var url = document.getElementById("URL").value;             // url value from python parameters
var audio = document.getElementById("audio");               // audio element

console.log(url);
if (String(url).includes("wav")) {
    audio.setAttribute('src', `/static/audio/${url}/`)      // changes audio element to reference converted file
}

convertBtn.addEventListener('click', () => {
    sendURL(URLinput.value);                                // calls sendURL() to change url
});

function sendURL(URL) {
    window.location.href = `http://localhost:8000/convert?URL=${URL}`;  // changes url to conversion url
}