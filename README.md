This is a python script that converts MIDI files to a code that my scratch project "TuneShare" (https://scratch.mit.edu/projects/863714854/) can successfully read and play!

Instructions
- Download everything as a ZIP.
- Open in a new tab the page https://onlinesequencer.net/
- Load a MIDI file in the tab opened, select all the notes and click "copy".
- Go to the `Input` folder, create a new text file, paste the clipboard and save it.
- Before running the `main.py` file, change the "filename" argument in line 100 to the name of the text file you just saved.
- Run the project and a new text file will be created in the `Output` folder.
- Open that file, select all and copy it.
- Open my TuneShare project, log in, create a new tune and import the code you copied.

Credits
- Big thanks to https://scratch.mit.edu/users/nerdboy628/ for creating the first fully working MIDI-to-TuneShare converter and for providing the necessary assets (basically the whole `Assets` folder was created by them). Their project can be found either at https://scratch.mit.edu/projects/870613190/ or https://snap.berkeley.edu/project?username=nerdboy628&projectname=MIDI%20to%20TuneShare%20Converter
