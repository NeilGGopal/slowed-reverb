var convertBtn = document.querySelector('.convert-button');
var URLinput = document.querySelector('.url-input');
var downloadBtn = document.querySelector('.download-button');

convertBtn.addEventListener('click', () => {
    console.log(`URL: ${URLinput.value}`);
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