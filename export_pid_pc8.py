##########################################################################################
#
# Renata Muylaert 2017
# Exporting pids for eucalyptus 2000-2014 maps ready inside GRASS environment (outputs from LSmetrics)
# Remember that the temporal series is available as binary from 2000-2016
# 
########################################################################################## 
output_dir = r'F:/PID_euca/'
os.chdir(output_dir)

# Raster list

grass.run_command('g.list', type = 'raster')

# Setting output raster names

output_rast = []
element_rast = 'BR_'
element_end = '_euca_9_pid'

for j in range(2000, 2015):
    output_rast.append(element_rast+str(j)+element_end)

# Making sure you export things within the right region

grass.run_command('g.region', raster = output_rast[-1], flags = 'p')

# Or just set the region that includes the extent of all raster list just to prevent

map_list = grass.list_grouped('rast', pattern = '*'+'pid')['PERMANENT']

grass.run_command('g.region', raster = map_list, flags = 'p')

# Export rasters (maybe it takes some hours per map)

for k in output_rast:
    print(k)
    grass.run_command('r.out.ogr', input =  k, output = k+'.tif', overwrite = True)
    

##########################################################################################
    
