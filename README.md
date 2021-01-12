# slowed-reverb
This program takes any YouTube link and applies a slowed & reverbed effect to the audio in the vein of the popular slowed/reverb edits on YouTube. This web application uses pytube by nficano, pysndfx by carlthome, pydub by jiaaro, and the Django web framework.

# Usage
While this program is intended to be hosted on a server and available for people to use, it currently is not. You will need to install the program and run it yourself.

Installation is as simple as cloning this repository and installing the packages listed above. To run the server, make sure you are in the same directory as manage.py and run the command `python3 manage.py runserver`. `python3` will vary depending on your Python version.

# TODO
- Link server to a remote database to store audio files
- Write a cleanup script to get rid of audio files after a certain period of time (ideally a few minutes)
- Find way to convert audio file for use by pysndfx without needing pydub
- Speed up audio conversion process
- Turn off autoplay on the resulting audio file




Pull requests are encouraged and appreciated!




*Created by Neil Gopal*