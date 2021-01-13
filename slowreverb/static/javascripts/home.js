var convertBtn = document.querySelector('.convert-button'); // convert button
var URLinput = document.querySelector('.url-input');        // url input
var convertTxt = document.getElementById("converting");     // text informing user of conversion process
var embedDiv = document.getElementById("embedDiv");         // div element to store convert text and bar
var progress = document.getElementById("myProgress");       // progress bar
var url = document.getElementById("URL").value;             // url value from python parameters
var audio = document.getElementById("audio");               // audio element

if (!window.location.href.includes('convert')) {
    audio.style.visibility = "hidden";
    audio.setAttribute('src', '');
}   // sets audio to invisible on homepage

// checks if user has converted link correctly
if (String(url).includes("mp3") && !String(window.location.href).includes("download")) {
    var link = document.getElementById("download");         // a tag for automatic download
    link.setAttribute("href", `/static/audio/${url}/`)
    link.setAttribute("download", `/static/audio/${url}/`);
    link.click();                                           // clicks a tag that forces download
    // audio.setAttribute('src', `/static/audio/${url}/`)   // changes audio element to reference converted file
    window.location.href = 
    `${window.location.href.substring(0,22)}download${window.location.href.substring(29)}`; // changes url to download url
}

// checks if user click conversion button
convertBtn.addEventListener('click', () => {
    if (!URLinput.value.includes("youtube.com/watch?v=")) {
        return;
    }                                                       // checks if URL input is a YouTube link
    sendURL(URLinput.value);                                // calls sendURL() to change url
    
    audio.style.visibility = "hidden";                      //
    audio.setAttribute('src', '');                          // hides audio if conversion clicked on convert page
    embedDiv.appendChild(convertTxt);                       // moves conversion text above audio
    embedDiv.appendChild(progress);                         // moves progress bar above audio

    convertTxt.style.visibility = "visible";                // makes convert text visible
    progress.style.visibility = "visible";                  // makes progress bar visible
    move();
});

// changes url to conversion url
function sendURL(URL) {
    window.location.href = `http://localhost:8000/convert?URL=${URL}`;  // changes url to conversion url
}

var i = 0;  // variable for width of inner progress bar
// move progress bar
function move() {
  if (i == 0) {
    i = 1;
    var elem = document.getElementById("myBar");
    var width = 0;
    var id = setInterval(frame, 10);
    function frame() {
      if (width >= 100) {
        clearInterval(id);
        i = 0;
      } else {
        width += 0.2;
        elem.style.width = width + "%";
        elem.innerHTML = Math.round(width) + "%";
      }
    }
  }
}