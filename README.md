# LSmetrics_testes_re
Tests for LS_metrics main procedures for patch ids in temporal series, and for generalized_zonal_stats defs

### Last version of LSmetrics tested available at
https://github.com/LEEClab/LS_METRICS

### Original scripts
https://github.com/mauriciovancine/GRASS-GIS-Landscape-Metrics/tree/master/scripts

#### Comments

- The script which calculates patch number in zonal statistics depends on LSmetrics outputs of pids (patch id info); 
- LSmetrics gui works well for a single raster, but fot running the option for a sequence of rasters with a string common pattern in raster file name, you must use the symbol "*": 
for example, if the file names' common pattern is all that starts with BR, put: BR *;
if it is all that has "forest" in the middle of file name, put: * forest *;
if it's all that ends with forest_albers, type: * forest_albers in the white box of LSmetrics (Pattern).

#### Some important tips for running python script without copying and pasting code

- Use an auxiliary set of five lines as a starter, so you don´t need to type anything else on the terminal
- Always type code in the black screen. The python shell in GRASS GIS DO NOT run well all the defs created!!!
- Remove the command python from inner script. If you let it there, the code will stop, since from the auxiliary code you already got into python inside GRASS command line. However, if you could call a python code from GRASS command line without calling python first, then the auxiliary code would change. But I don´t know how to start a large script differently

### The auxiliary starter code has five lines

- python # calls python in GRASS 
- import os # allows changing directory
- import grass.script as grass # allows importing scripts
- os.chdir('F:/__data/') # set directory where the script was saved
- import zonal_stats_test_pc8 # imports the script and make your life easier
- After that, if everything is correctly written in the script, you can wait for the results and rest.




