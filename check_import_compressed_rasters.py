############################################
# Check compressed rasters of euca (pid)
# These rasters were exported
# with the following parameters:
# createopt="TFW=YES,COMPRESS=DEFLATE"
############################################

python

import os

input_dir = 'G:/PID_euca'
os.chdir(input_dir)

maps = ['BR_2001_euca_9', 'BR_2002_euca_9', 'BR_2003_euca_9', 'BR_2004_euca_9']

for i in maps:
    grass.run_command('r.in.gdal', input = i+'_pid.tif', output = i, overwrite = True)

grass.run_command('g.list', type = 'raster')

