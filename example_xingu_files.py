#---------------------------------------------------------------------------------------
''' Cutting example rasters for GenZonalStats
 renatamuy@gmail.com
 Laboratorio de Ecologia Espacial e Conservacao
 Universidade Estadual Paulista - UNESP
 Rio Claro - SP - Brasil
 This script runs in GRASS GIS 7.X environment.
'''
#--------------------------------------------------------------------------------------- 

# aux
# python
# import os
# import grass.script as grass
# os.chdir('F:/__data/')

''' Files used as input in GeneralizedZonalStats were created here
 xingu_region_wgs84.shp
 BR_2000_forest_xingu.tif
 BR_2006_forest_xingu.tif
 BR_2012_forest_xingu.tif
 BR_2016_forest_xingu.tif
 '''

# Import shape file (municipalities of Brazil)

input_dir = r'F:/__data/muylaert/malhas_grass/'
os.chdir(input_dir)

shape_name = 'malha_mun_91_wgs84'
grass.run_command('v.in.ogr', input = shape_name+'.shp', output = shape_name, overwrite = True)

# Select the region of interest

grass.run_command('g.region', raster = map_list, flags = 'p')

g.region()

# Various zoom options > set region from display

grass.run_command('g.region', flags= 'p')

# Region info 
#projection: 3 (Latitude-Longitude)
#zone:       0
#datum:      wgs84
#ellipsoid:  wgs84
#north:      9:31:02.89478S
#south:      15:03:56.971055S
#west:       58:03:23.076049W
#east:       49:06:44.725388W
#nsres:      0:00:00.970181
#ewres:      0:00:00.970181
#rows:       20588
#cols:       33188
#cells:      683274544

grass.run_command('r.mask', vector="malha_mun_91_wgs84@forest_PID_mapset")

# Name output files

example_rast = ['BR_2000_forest', 'BR_2006_forest', 'BR_2012_forest', 'BR_2016_forest']
output_rast = []
element_end = '_xingu'


for j in range(len(example_rast)):
    output_rast.append(example_rast[j]+element_end)


output_rast
# Export raster subsets (choose compression)

for k in range(len(example_rast)):
    print(example_rast[k])
    grass.run_command('r.out.gdal', input = example_rast[k], output = output_rast[k]+'.tif', createopt="TFW=YES,COMPRESS=DEFLATE", overwrite = True)

# Exporting vector subset for this region
# Teoricamente v.overlay using the mask of set region as boundary would work
# v.overlay ainput=malha_mun_91_wgs84@forest_PID_mapset binput=malha_mun_91_wgs84@forest_PID_mapset operator=and output=xingu_overlay
# Na prática eu selecionei os polígonos dentro da region com select vector features na mão e cliquei em "Create New Map"

# Exporting the example shapefile
malha_mun_91_wgs84_selection = malha_mun_91_wgs84_selectionOMA

grass.run_command('v.out.ogr', input = malha_mun_91_wgs84_selectionOMA , output = 'xingu_region_wgs84.shp', format='ESRI_Shapefile',
                  overwrite = True, flags= 'e')

# v.out.ogr --overwrite input=malha_mun_91_wgs84_selectionOMA output=F:\__data\muylaert\malhas_grass\xingu_region_wgs84.shp format=ESRI_Shapefile
# r.mask -r remove mask
