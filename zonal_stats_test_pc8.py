
# aux
# python
# import os
# import grass.script as grass
# os.chdir('F:/__data/')
# import zonal_stats_test_pc8


#---------------------------------------------------------------------------------------
"""
 Script to test generalized zonal stats in GRASS GIS
 Bernardo B. S. Niebuhr - bernardo_brandaum@yahoo.com.br
 
 Laboratorio de Ecologia Espacial e Conservacao
 Universidade Estadual Paulista - UNESP
 Rio Claro - SP - Brasil
 This script runs in GRASS GIS 7.X environment.
"""
#--------------------------------------------------------------------------------------- 

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

    #------------------
# 4.
# Run zonal stats

# We will use the Patch ID map to calculate the number of patches within a shapefile feature (municipality in this example)
# We will use the binary eucaliptus map to calculate the proportion of eucaliputs within a shapefile feature (municipality in this example)

# Change to the script folder
script_dir = r'F:/__data/muylaert/GRASS-GIS-Landscape-Metrics-master/scripts'

os.chdir(script_dir)

# Import generalized_zonal_stats class and functions
from generalized_zonal_stats import generalized_zonal_stats, proportion_habitat, number_patches

#------------------
# 4.2.
# Running for proportion of eucaliptus for only 3 years - 2002-2004

# Input shape and rasters
input_shp = 'mun_teste_wgs84'
input_rast = ['BR_2002_euca_9', 'BR_2003_euca_9', 'BR_2004_euca_9']

# Initialize and select maps to be used in zonal stats
test_prop_euca = generalized_zonal_stats(input_shape = input_shp, input_rasters = input_rast, folder = input_dir)

# Create new cols
cols = ['p_euc_02', 'p_euc_03', 'p_euc_04'] # Col name
col_type = ['float', 'float', 'float'] # Col type

# WARNING! GRASS GIS does not like col names longer than 8-10 characters, so try to be very concise!!
# Or later you can do something like 
# grass.run_command('v.db.renamecolumn', map=shape_name, column='oldcolname,newcolname')
#grass.run_command('v.db.renamecolumn', map=shape_name, column='prp_euca_2001,p_eu_2001')

# Create cols
test_prop_euca.create_new_column(column_names = cols, type_col = col_type)

# Monitoring time
start = time.time()

# Calculate proportion of eucaliptus in each feature using proportion_habitat function
test_prop_euca.run_zonal_stats(proportion_habitat)

# Monitoring time
end = time.time()

# Print total time
print 'The zonal stats for prop of habitat for 3 years took us '+str((end - start)/60)+' minutes.'

#------------------
# 4.3.
# Running for number of patches for 2002-2004

# Input shape and rasters
input_shp = 'mun_teste_wgs84'
input_rast = ['BR_2002_euca_9_pid', 'BR_2003_euca_9_pid', 'BR_2004_euca_9_pid']


pid_dir = r'F:/__data/muylaert/paraber/PID'
os.chdir(pid_dir)

# Initialize and select maps to be used in zonal stats
test_np = generalized_zonal_stats(input_shape = input_shp, input_rasters = input_rast, folder = pid_dir)

# Create new cols
cols = ['np_2002', 'np_2003', 'np_2004'] # Col names
col_type = ['int', 'int', 'int'] # Col type

# WARNING! GRASS GIS does not like col names longer than 8-10 characters, so try to be very concise!!

# Create cols
test_np.create_new_column(column_names = cols, type_col=col_type)

# Monitoring time
start = time.time()

# Calculate number of patches (clumps) of eucaliptus in each feature using number_patches function
test_np.run_zonal_stats(number_patches, mask = True)

# Monitoring time
end = time.time()

# Print total time
print 'The zonal stats for number of patches for 3 years took us '+str((end - start)/60)+' minutes.'
shape_name = 'mun_teste_wgs84'
# Export shapefile
os.chdir(input_dir)
# export shape file
grass.run_command('v.out.ogr', input = shape_name, output = shape_name+'_prop_euca_np_t6.shp', overwrite = True)




#######################################################
