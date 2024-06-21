# BallPIT
BallPIT (Python Image Tally) is a simple Python script made as a means of counting the number of Ball Grid Array (BGA) balls on a CPU or other integrated circuit.

- Usage:
To start, either run the BallPIT_setup_and_run.bat file to automatically install the required dependencies and then run the script, or just execute the BallPIT.py script via command line.
Once run, the script will ask for an image name. Type in the filename and press enter and the script will echo back how many balls it has calculated in the image, as well as output a file with each ball it identifies, circled in red (this can be useful for checking for errors).

- Limitations:
Currently, the script is only intended to be used on greyscale .png images, as it will count any area that is from 50% grey to pure white (RGB 128,128,128 to 255,255,255).
The picture may need some contrast and level adjustment for accurate results.
