import arcpy
import os

workspace = r"D:\Our Data\tl_2012_04_cousub"
outputspace = workspace

targetFeatures = os.path.join(workspace, "testSpatialJoin.shp")
joinFeatures = os.path.join(workspace, "tl_2012_04_cousub.shp")
output = os.path.join(workspace, "testresult8.shp")

fieldmappings = arcpy.FieldMappings()
fieldmappings.addTable(targetFeatures)
fieldmappings.addTable(joinFeatures)

namefiled = fieldmappings.findFieldMapIndex("NAME")
fieldmap = fieldmappings.getFieldMap(namefiled)

field = fieldmap.outputField
field.name = "unitName"
field.aliasName = "unitName"
fieldmap.outputField = field

fieldmappings.replaceFieldMap(namefiled, fieldmap)
arcpy.SpatialJoin_analysis(targetFeatures, joinFeatures, output, "#", "#", fieldmappings)

fields = arcpy.ListFields(output)
keepFields = [u'FID', u'Shape', u'Join_Count', u'TARGET_FID', u'Id', u'unitName', u"NAMELSAD"]
dropFields = [x.name for x in fields if x.name not in keepFields]
arcpy.DeleteField_management(output, dropFields)
