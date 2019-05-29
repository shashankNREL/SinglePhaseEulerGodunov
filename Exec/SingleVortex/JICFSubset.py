#!/usr/local/bin/python
from numpy import *
#import math
from visit_utils import *
import glob
import os
OpenDatabase("localhost:/Users/natarajan/Desktop/Research/NGA/AMR/amrex/Tutorials/Amr/FluidsSolverFrameworkRefCrit_bkp/Exec/SingleVortex/movie.visit", 0)
AddPlot("Subset", "levels", 1, 1)
DrawPlots()
SubsetAtts = SubsetAttributes()
SubsetAtts.colorType = SubsetAtts.ColorByMultipleColors  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
SubsetAtts.colorTableName = "Default"
SubsetAtts.invertColorTable = 0
SubsetAtts.legendFlag = 1
SubsetAtts.lineStyle = SubsetAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
SubsetAtts.lineWidth = 2
SubsetAtts.singleColor = (0, 0, 0, 255)
SubsetAtts.SetMultiColor(0, (255, 0, 0, 255))
SubsetAtts.SetMultiColor(1, (0, 255, 0, 255))
SubsetAtts.subsetNames = ("1", "2")
SubsetAtts.opacity = 1
SubsetAtts.wireframe = 1
SubsetAtts.drawInternal = 0
SubsetAtts.smoothingLevel = 0
SubsetAtts.pointSize = 0.05
SubsetAtts.pointType = SubsetAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
SubsetAtts.pointSizeVarEnabled = 0
SubsetAtts.pointSizeVar = "default"
SubsetAtts.pointSizePixels = 2
SetPlotOptions(SubsetAtts)
	
