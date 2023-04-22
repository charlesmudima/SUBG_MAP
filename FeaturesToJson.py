# import arcpy
import os 
import json
import sys
import arcpy
import arcpy.sa
import arcpy.da

listPath = arcpy.ListFeatureClasses()


print (listPath)

print(sys.path)
arcpy.env.workspace = "c:/data"
arcpy.FeaturesToJSON_conversion(os.path.join("outgdb.gdb", "myfeatures"),
                                "myjsonfeatures.json")
arcpy.FeaturesToJSON_conversion(os.path.join("outgdb.gdb", "myfeatures"),
                                "mypjsonfeatures.json", "FORMATTED")