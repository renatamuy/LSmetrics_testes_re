# LS metrics October 24th version
# create_pids_pc8
# Test for for four years at once


# aux
# python
# import os
# import grass.script as grass
# os.chdir('F:/__data/')
# import create_pids_pc8

#------------------
# 1.
# First create a GRASS GIS location based on the input shapefile and open GRASS within it



# Import modules
import os
import grass.script as grass
import subprocess
import time


#------------------
# 2.
# Import files

# Set folder where input files are
input_dir = r'F:/__data/muylaert/paraber/'
os.chdir(input_dir)

# Import shape file (municipalities of South Brazil)
shape_name = 'mun_teste_wgs84'
grass.run_command('v.in.ogr', input = shape_name+'.shp', output = shape_name, overwrite = True)

# Import rasters (areas of Eucalyptus plantation in 2001-2004)
maps = ['BR_2001_euca_9', 'BR_2002_euca_9', 'BR_2003_euca_9', 'BR_2004_euca_9']
for i in maps:
    grass.run_command('r.in.gdal', input = i+'.tif', output = i, overwrite = True)

lsmetrics_dir = r'F:/__data/muylaert/LS_METRICS-master-october/LS_METRICS-master/_LSMetrics_v1_0_0/'

os.chdir(lsmetrics_dir)

# Run LSMetrics
subprocess.call('python LSMetrics_v1_0_0.py', shell=True) # runs and wait
# Here it is important to decide whether pixels on the diagonal will be considered as the same patch or not!!

#------------------
