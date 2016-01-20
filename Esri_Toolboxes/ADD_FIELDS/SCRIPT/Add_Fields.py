#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:	   Add multiple fields to multiple feature classes in a .mxd
#
# Author:      Blake Harcourt
#
# Created:     21/11/2013
# Copyright:   (c) Blakeharcourt 2013
# Licence:     Blake Harcourt
#-------------------------------------------------------------------------------
#IMPORTS
import arcpy
import os


mxd = arcpy.mapping.MapDocument("CURRENT")          #The script is being ran from the current MXD.
layers = arcpy.mapping.ListLayers(mxd, "*")         #All layers in the current MXD can be acessed by the script.
df = arcpy.mapping.ListDataFrames(mxd)[0]           #The dataframe in the current MXD can be accessed by the script.

#VARIABLES
FEATURE_CLASS_COUNT = 0
FIELD_COUNT = 0
TOTAL_COUNT = 0
CURRENT_COUNT = 0

#INPUTS FROM GUI
LAYERS_TO_ADD = arcpy.GetParameterAsText(0)         #Gets the input from the script GUI to find which feature classes to add.
FIELDS_TO_ADD = arcpy.GetParameterAsText(1)

#DISPLAY MESSAGES---------------------------------------------------------------
arcpy.AddMessage("***Script Created by Blake Harcourt***")
arcpy.AddMessage("-----------------")

#COUNT NUMBER OF FEATURE CLASSES
for FEATURES in LAYERS_TO_ADD.split(';'):         #SPLITS THE INPUT LIST AND DISPLAYS THE FEATURE CLASSES TO COPY
    FEATURE_CLASS_COUNT = FEATURE_CLASS_COUNT + 1
arcpy.AddMessage("TOTAL NUMBER OF FEATURE CLASSES = " + str(FEATURE_CLASS_COUNT))

#COUNT NUMBER OF FIELDS CLASSES
for FIELDS in FIELDS_TO_ADD.split(';'):         #SPLITS THE INPUT LIST AND DISPLAYS THE FEATURE CLASSES TO COPY
    FIELD_COUNT = FIELD_COUNT + 1
arcpy.AddMessage("TOTAL NUMBER OF FIELDS = " + str(FIELD_COUNT))

#TOTAL NUMBER OF OPERATIONS TO PERFORM
TOTAL_COUNT = FEATURE_CLASS_COUNT*FIELD_COUNT

#ADD FIELDS TO FEATURE CLASSES
for FEATURES in LAYERS_TO_ADD.split(';'):
	for FIELDS in FIELDS_TO_ADD.split(';'):
		String = FIELDS
		String2 = String.replace(",", " ") #Replace all commas with single spaces
		String3 = String2.replace("  ", " ")#Replace all double spaces with single spaces
		String4 = String3.replace("\"", "")
		FIELDS_TEXT = String4.split()

		FIELD_NAME = FIELDS_TEXT[0]
		FIELD_ALISAS = FIELDS_TEXT[1]
		FIELD_EDITABLE = FIELDS_TEXT[2]
		FIELD_ISNULLABLE = FIELDS_TEXT[3]
		FIELD_ISREQUIRED = FIELDS_TEXT[4]
		FIELD_SIZE = FIELDS_TEXT[5]
		FIELD_TYPE = FIELDS_TEXT[6]
		FIELD_PRECISION = FIELDS_TEXT[7]
		FIELD_SCALE = FIELDS_TEXT[8]
		FIELD_MERGERULE = FIELDS_TEXT[9]
		FIELD_DELIMETER = FIELDS_TEXT[10]

		arcpy.AddField_management(FEATURES, FIELD_NAME,FIELD_TYPE,FIELD_PRECISION,FIELD_SCALE,FIELD_SIZE,FIELD_ALISAS,FIELD_ISNULLABLE,FIELD_ISREQUIRED)
		CURRENT_COUNT = CURRENT_COUNT + 1
		arcpy.AddMessage("COMPLETED " + str(CURRENT_COUNT) + "/" + str(TOTAL_COUNT))


#[Field Name] [Alias] [Editable] [IsNullable] [IsRequired] [Size] [Type]
#[Precision] [Scale], [Merge Rule], [Delimiter], [Input Field Location, Input
#Field Name], [Start Postion, End Postion], [Additional Input Field Location,
#Input Field Name], [Start Postion, End Postion]










