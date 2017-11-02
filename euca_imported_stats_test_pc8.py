
# aux
# import os
# import grass.script as grass
# os.chdir('F:/__data/')
# import euca_imported_stats_test_pc8

#####Testing script for imported maps

import time
import os

#grass.run_command('g.list', type = 'raster')

# Zonal stats for imported Euca imported files for Mapbiomas collection 2

# Set shapefile of municipalities of reference
input_dir = r'F:/__data/muylaert/malhas_grass'
os.chdir(input_dir)

# Import shape file (municipalities of South Brazil)
shape_name = 'malha_mun_91_wgs84'
grass.run_command('v.in.ogr', input = shape_name+'.shp', output = shape_name, overwrite = True)

# Change to the script folder
script_dir = r'F:/__data/muylaert/GRASS-GIS-Landscape-Metrics-master/scripts'

os.chdir(script_dir)

# Import generalized_zonal_stats class and functions
from generalized_zonal_stats import generalized_zonal_stats, proportion_habitat, number_patches

# Running for proportion of eucaliptus
input_shp = 'malha_mun_91_wgs84'

# Raster names
input_rast = []
element_rast = 'BR_'
element_end = '_euca_9'

for j in range(2000, 2015):
    input_rast.append(element_rast+str(j)+element_end)

input_rast

# Initialize and select maps to be used in zonal stats
test_prop_euca = generalized_zonal_stats(input_shape = input_shp, input_rasters = input_rast)

# Create new cols
cols = []

for k in range(2000, 2015):
    cols.append('p_eu_'+str(k))


cols
###
    
# Col type 
col_type = []
element = 'float'

for i in range(15):
    col_type.append(element)

####

# Create cols
test_prop_euca.create_new_column(column_names = cols, type_col = col_type)

# Monitoring time
start = time.time()

# Calculate proportion of eucaliptus in each feature using proportion_habitat function
test_prop_euca.run_zonal_stats(proportion_habitat)

# Monitoring time
end = time.time()

# Print total time
print 'The zonal stats for prop of habitat for 14 years took us '+str((end - start)/60)+' minutes.'

#------------------
# 4.3.
# Running for number of patches for 2002-2004
#NP #NP #NP #NP #NP #NP #NP #NP #NP #NP #NP #NP #NP #NP

# Input shape and rasters
input_shp = 'malha_mun_91_wgs84'
#
#
input_rast = []
element_rast = 'BR_'
element_end = '_euca_9_pid'

for j in range(2000, 2015):
    input_rast.append(element_rast+str(j)+element_end)

input_rast

# Initialize and select maps to be used in zonal stats
test_np = generalized_zonal_stats(input_shape = input_shp, input_rasters = input_rast)

# Create new cols
cols = []

for k in range(2000, 2015):
    cols.append('np_eu_'+str(k))

# Type n times
col_type = []
x = 'int'
for i in range(15):
    col_type.append(x)
    
# Create cols
test_np.create_new_column(column_names = cols, type_col=col_type)

# Monitoring time
start = time.time()

# Calculate number of patches (clumps) of eucaliptus in each feature using number_patches function
test_np.run_zonal_stats(number_patches, mask = True)

# Monitoring time
end = time.time()

# Print total time
print 'The zonal stats for number of patches for 14 years took us '+str((end - start)/60)+' minutes.'
shape_name = 'malha_mun_91_wgs84'

# Export shapefile
os.chdir(input_dir)
# export shape file
grass.run_command('v.out.ogr', input = shape_name, output = shape_name+'_prop_np_euca_91.shp', overwrite = True)



