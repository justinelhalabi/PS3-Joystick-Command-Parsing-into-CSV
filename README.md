# PS3-Joystick-Command-Parsing-into-CSV
rtest.py: (Python 2.7) This code parses the input commands from a PS3 joystick into a more readable .csv file format. It takes the x-y-z commands with the corresponding time and places them in rows. This code also detects and displays when the X, Square, Circle, or triangle buttons are pressed.

rtest2.py: (Python 3) This code takes all the .csv files in a folder (which is set in the code by the user) and takes all the velociy commands of the joystick and places them in an array format as such: [x y z]. It also displays a histogram with some data analytics do get the average number of samples for every sequence. It also displays on the terminal where the code is ran: the number of samples found, min and Max size, Mean, Median, and Deviation.

If you're looking to use these scripts and our data, please cite our work:

J.   Elhalabi,   M.   Al   Aawar,   M.   Kassem   Zein,   I.   H.   Elhajj,   andD.   Asmar,   “Drone   motion   primitive   dataset,”   2020.   [Online].Available: http://dx.doi.org/10.21227/7wb1-0r93
