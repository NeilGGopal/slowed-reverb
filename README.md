# slowed-reverb
This program takes any YouTube link and applies a slowed & reverbed effect to the audio in the vein of the popular slowed/reverb edits on YouTube. This web application uses pytube by nficano, pysndfx by carlthome, pydub by jiaaro, youtube-dl, and the Django web framework.

## Usage
The current version works according to my file structure. You'll need to edit the code to have it work for you, as the program is not hosted remotely.

(INSTRUCTIONS IN PROGRESS)

## TODO
- Link server to a remote database to store audio files
- ~~Write a cleanup script to get rid of audio files after a certain period of time (ideally a few minutes)~~ *Backend automatically deletes files*
- ~~Find way to convert audio file for use by pysndfx without needing pydub~~ *Now using MoviePy to convert audio*
- Speed up audio conversion process
- ~~Turn off autoplay on the resulting audio file~~ *`audio` element in home.html prevents autoplay*

---
Pull requests are encouraged and appreciated!

*Created by Neil Gopal*
