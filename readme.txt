Take the repository on github. (clone it where you want on your computer). 

command -- git clone https://github.com/thomasViot/Summer-internship -- or directly on the website

Structure of the repository

4 folders : DatFolder, MatlabFolder, PythonFolder and TextFolder. Containing a certian type of extention file.

Steps to start the project :

Do the following steps ones. When you import new .dat data from the company.

- Go to the DatFolder.
- Put the global data into the globalData folder and the specific data into the specific one.
- Use the link.py script. (Yo can luch it with the command -- python link.py -- )
(after using the command we should see .dat files inside the OnlylinkedGlobalData and the OnlyLinkedSpecificData folder)


Do this every time that you want to change the data studied.

- Go to iba analyser software. 
- Take .dat files from the OnlylinkedGlobalData folder or the OnlyLinkedSpecificData folder
- Write on a paper the date of the first .dat file chosen.
- Create one big text file (thanks to iba analyser) and put it in the TextFolder/bigFiles folder.
- rename this file : globalFile.txt or specificFile.txt (depending what you are studing)
- change startingDate variable in the prepareData.py script. Put the date that you wrote on your paper inside. 
(this step is needed to keep the info of the date)
- Lunch the python script prepareData.py with command -- python prepareData.py 1 -- or -- python prepareData.py 2 --
(use 1 for global data and 2 for specific ones) -- (you should see .txt files inside the globalData folder or the specificData folder)
- Go to MatlabFolder 
- lunch command -- python prepareDataMATLAB.py 1 -- or -- python prepareDataMATLAB.py 2 -- (one for global, 2 for specific)
- Go to Matlab software
- use the loadingData script to see signals in matlab.


In loadingData MATLAB script :

- there is lines where you can specify from which to which signal you want to study. (these nuumbers should be between the number of signals that you exported)

PCA MATLAB script :

This script gives you the classification of signals. Here again you can specify from which to which signal you want to work. 
You will have to specify the types of you training data set before lunching the script. 

FIR/ARX/ARMAX model in the Models matlab file. 

