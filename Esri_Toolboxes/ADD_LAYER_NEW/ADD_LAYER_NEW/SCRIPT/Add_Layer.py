#-------------------------------------------------------------------------------
# Name:        Add_Layer
# Purpose:     Add multiple layers to multiple mxds
#
# Author:      Blake Harcourt
#
# Created:     21/11/2013
# Copyright:   (c) Blakeharcourt 2013
# Licence:     Blake Harcourt
#-------------------------------------------------------------------------------

#Imports
import arcpy
import os


mxd = arcpy.mapping.MapDocument("CURRENT")          #The script is being ran from the current MXD.
layers = arcpy.mapping.ListLayers(mxd, "*")         #All layers in the current MXD can be acessed by the script.
df = arcpy.mapping.ListDataFrames(mxd)[0]           #The dataframe in the current MXD can be accessed by the script.

FEATURE_CLASS_COUNT = 0
MXD_COUNT = 0


LAYERS_TO_ADD = arcpy.GetParameterAsText(0)         #Gets the input from the script GUI to find which feature classes to add.
MAPS_TO_ADD = arcpy.GetParameterAsText(1)           #Gets the input from the script GUI to find which MXDS to add feature classes to.
POSITION_CHECK = arcpy.GetParameterAsText(2)        #Gets the input from the script GUI to find the position to add the new feature classes.

#DISPLAY MESSAGES---------------------------------------------------------------
arcpy.AddMessage("***Script Created by Blake Harcourt***")
arcpy.AddMessage("-----------------")
arcpy.AddMessage("FEATURE CLASSES = ")

for FC_DISPLAY in LAYERS_TO_ADD.split(';'):         #SPLITS THE INPUT LIST AND DISPLAYS THE FEATURE CLASSES TO COPY
    arcpy.AddMessage(FC_DISPLAY)                    #DISPLAYS EACH FEATURE CLASS
    FEATURE_CLASS_COUNT = FEATURE_CLASS_COUNT + 1

arcpy.AddMessage("TOTAL NUMBER OF FEATURE CLASSES = " + str(FEATURE_CLASS_COUNT))


arcpy.AddMessage("-----------------")
arcpy.AddMessage("MXDS = ")

for MAPS_DISPLAY in MAPS_TO_ADD.split(';'):         #SPLITS THE INPUT LIST AND DISPLAYS THE MXDS TO ADD LAYERS TO
    arcpy.AddMessage(MAPS_DISPLAY)                  #DISPLAS EACH MXD
    MXD_COUNT = MXD_COUNT + 1

arcpy.AddMessage("TOTAL NUMBER OF MXDS = " + str(MXD_COUNT))

arcpy.AddMessage("-----------------")
if str(POSITION_CHECK) == 'true':
    arcpy.AddMessage("TOC POSITION = TOP")
else:
    arcpy.AddMessage("TOC POSITION = BOTTOM")


#ADD LAYERS TO MAPS-------------------------------------------------------------
arcpy.AddMessage("-----------------")
arcpy.AddMessage("COPYING FEATURE CLASSES TO MXD")
for MAP in MAPS_TO_ADD.split(';'):
    MXD2 =arcpy.mapping.MapDocument(MAP)
    DF2 = arcpy.mapping.ListDataFrames(mxd)[0]


    for LAYER in LAYERS_TO_ADD.split(';'):
        arcpy.AddMessage(MAP + " "+LAYER)
        df1 = arcpy.mapping.ListDataFrames(MXD2, "Layers")[0]
        addLayer = arcpy.mapping.Layer(LAYER)
        if str(POSITION_CHECK) == 'true':
            arcpy.mapping.AddLayer(df1 ,addLayer ,"TOP")
            arcpy.AddMessage("Copying Layers...")
        else:
            arcpy.mapping.AddLayer(df1 ,addLayer ,"BOTTOM")
            arcpy.AddMessage("Copying Layers...")
        del  addLayer
    arcpy.AddMessage("-----------------")
    arcpy.AddMessage("SAVING MXD")
    arcpy.AddMessage("-----------------")
    MXD2.save()
    del MXD2






























