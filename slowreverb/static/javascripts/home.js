var convertBtn = document.querySelector('.convert-button');
var URLinput = document.querySelector('.url-input');
var downloadBtn = document.querySelector('.download-button');
var url = document.getElementById("URL").value;

console.log(url);
if (url == "DOWNLOAD") {
    downloadBtn.style.visibility = "visible";
} else {
    downloadBtn.style.visibility = "hidden";
}

convertBtn.addEventListener('click', () => {
    sendURL(URLinput.value);
});

function sendURL(URL) {
    window.location.href = `http://localhost:8000/convert?URL=${URL}`;
}

function sendURLDownload(URL) {
    window.location.href = `http://localhost:8000/download?URL=${URL}`;
}

downloadBtn.addEventListener('click', () => {
    console.log(`URL: ${window.location.href.substring(34)}`);
    console.log(`${window.location.href.replace('convert', 'download')}`)
    sendURLDownload(window.location.href.substring(34));
});