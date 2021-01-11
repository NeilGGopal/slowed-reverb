var convertBtn = document.querySelector('.convert-button');
var URLinput = document.querySelector('.url-input');
var downloadBtn = document.querySelector('.download-button');
var slider = document.getElementById("myRange");
var output = document.getElementById("value");
var video = document.getElementById("video");
output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
    output.innerHTML = this.value;
    video.playbackRate = output.innerHTML;
}

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

function upload() {
    var input = document.getElementById("upload");
    var reader = new FileReader();

    reader.readAsDataURL(input.files[0]);

    reader.onload = function() {
        document.getElementById("video").src = reader.result;
    };

    reader.readAsDataURL(file);
}