
# So what do i want to do??
# I want a script that converts shapefiles to .js
# The scripts can be stored inside this folder 

import os 
import json
import sys
import arcpy
import arcpy.sa
import arcpy.da
import shapefile
import geojson
from geojson import Feature, FeatureCollection, Point

arcpy.env.workspace = "c:/data"
arcpy.FeaturesToJSON_conversion(os.path.join("outgdb.gdb", "myfeatures"),
                                "myjsonfeatures.json")
arcpy.FeaturesToJSON_conversion(os.path.join("outgdb.gdb", "myfeatures"),
                                "mypjsonfeatures.json", "FORMATTED")