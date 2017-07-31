#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Quan
#
# Created:     01/06/2017
# Copyright:   (c) Quan 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy
import os
from arcpy import env

def clipShp(path):
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if filename.endswith('.shp'):
                in_features = os.sep.join([dirpath, filename])
                clip_features = "D:\\Our Data\\Bondaries\\Fire Planning Units\\fpu\\az_bound.shp"
                out_feature_class = in_features[:-4] + "_AZ.shp"
                arcpy.Clip_analysis(in_features, clip_features, out_feature_class)

def main():
    clipShp("D:\\Our Data\\Bondaries\\Fire Planning Units\\AZ")

if __name__ == '__main__':
    main()



