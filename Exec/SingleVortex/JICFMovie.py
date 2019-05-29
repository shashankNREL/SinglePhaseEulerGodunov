#!/usr/local/bin/python
from numpy import *
#import math
from visit_utils import *
import glob
import os
#OpenDatabase("localhost:/Users/natarajan/Desktop/Research/NGA/AMR/amrex/Tutorials/Amr/FluidsSolverFrameworkRefCrit_bkp/Exec/SingleVortex/movie.visit", 0)
for i in range(22000,24000,100):
	solnfile="./plt%0.5d/Header"%i
	print solnfile
	#OpenDatabase("/Users/natarajan/Desktop/Research/NGA/AMR/amrex/Tutorials/Amr/FluidsSolverFrameworkRefCrit_bkp/Exec/SingleVortex/plt%0.5d/Header"%i, 0)
	OpenDatabase(solnfile, 0)
        filename='JICF_AMReX%0.5d'%i
	print filename
	AddPlot("Contour", "vorticity_magnitude", 1, 0)
	DrawPlots()
	ContourAtts = ContourAttributes()
	ContourAtts.defaultPalette.GetControlPoints(0).colors = (255, 0, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(0).position = 0
	ContourAtts.defaultPalette.GetControlPoints(1).colors = (0, 255, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(1).position = 0.034
	ContourAtts.defaultPalette.GetControlPoints(2).colors = (0, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(2).position = 0.069
	ContourAtts.defaultPalette.GetControlPoints(3).colors = (0, 255, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(3).position = 0.103
	ContourAtts.defaultPalette.GetControlPoints(4).colors = (255, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(4).position = 0.138
	ContourAtts.defaultPalette.GetControlPoints(5).colors = (255, 255, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(5).position = 0.172
	ContourAtts.defaultPalette.GetControlPoints(6).colors = (255, 135, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(6).position = 0.207
	ContourAtts.defaultPalette.GetControlPoints(7).colors = (255, 0, 135, 255)
	ContourAtts.defaultPalette.GetControlPoints(7).position = 0.241
	ContourAtts.defaultPalette.GetControlPoints(8).colors = (168, 168, 168, 255)
	ContourAtts.defaultPalette.GetControlPoints(8).position = 0.276
	ContourAtts.defaultPalette.GetControlPoints(9).colors = (255, 68, 68, 255)
	ContourAtts.defaultPalette.GetControlPoints(9).position = 0.31
	ContourAtts.defaultPalette.GetControlPoints(10).colors = (99, 255, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(10).position = 0.345
	ContourAtts.defaultPalette.GetControlPoints(11).colors = (99, 99, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(11).position = 0.379
	ContourAtts.defaultPalette.GetControlPoints(12).colors = (40, 165, 165, 255)
	ContourAtts.defaultPalette.GetControlPoints(12).position = 0.414
	ContourAtts.defaultPalette.GetControlPoints(13).colors = (255, 99, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(13).position = 0.448
	ContourAtts.defaultPalette.GetControlPoints(14).colors = (255, 255, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(14).position = 0.483
	ContourAtts.defaultPalette.GetControlPoints(15).colors = (255, 170, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(15).position = 0.517
	ContourAtts.defaultPalette.GetControlPoints(16).colors = (170, 79, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(16).position = 0.552
	ContourAtts.defaultPalette.GetControlPoints(17).colors = (150, 0, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(17).position = 0.586
	ContourAtts.defaultPalette.GetControlPoints(18).colors = (0, 150, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(18).position = 0.621
	ContourAtts.defaultPalette.GetControlPoints(19).colors = (0, 0, 150, 255)
	ContourAtts.defaultPalette.GetControlPoints(19).position = 0.655
	ContourAtts.defaultPalette.GetControlPoints(20).colors = (0, 109, 109, 255)
	ContourAtts.defaultPalette.GetControlPoints(20).position = 0.69
	ContourAtts.defaultPalette.GetControlPoints(21).colors = (150, 0, 150, 255)
	ContourAtts.defaultPalette.GetControlPoints(21).position = 0.724
	ContourAtts.defaultPalette.GetControlPoints(22).colors = (150, 150, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(22).position = 0.759
	ContourAtts.defaultPalette.GetControlPoints(23).colors = (150, 84, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(23).position = 0.793
	ContourAtts.defaultPalette.GetControlPoints(24).colors = (160, 0, 79, 255)
	ContourAtts.defaultPalette.GetControlPoints(24).position = 0.828
	ContourAtts.defaultPalette.GetControlPoints(25).colors = (255, 104, 28, 255)
	ContourAtts.defaultPalette.GetControlPoints(25).position = 0.862
	ContourAtts.defaultPalette.GetControlPoints(26).colors = (0, 170, 81, 255)
	ContourAtts.defaultPalette.GetControlPoints(26).position = 0.897
	ContourAtts.defaultPalette.GetControlPoints(27).colors = (68, 255, 124, 255)
	ContourAtts.defaultPalette.GetControlPoints(27).position = 0.931
	ContourAtts.defaultPalette.GetControlPoints(28).colors = (0, 130, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(28).position = 0.966
	ContourAtts.defaultPalette.GetControlPoints(29).colors = (130, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(29).position = 1
	ContourAtts.defaultPalette.smoothing = ContourAtts.defaultPalette.None  # None, Linear, CubicSpline
	ContourAtts.defaultPalette.equalSpacingFlag = 1
	ContourAtts.defaultPalette.discreteFlag = 1
	ContourAtts.defaultPalette.categoryName = "Standard"
	ContourAtts.changedColors = ()
	ContourAtts.colorType = ContourAtts.ColorByMultipleColors  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
	ContourAtts.colorTableName = "Default"
	ContourAtts.invertColorTable = 0
	ContourAtts.legendFlag = 1
	ContourAtts.lineStyle = ContourAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
	ContourAtts.lineWidth = 0
	ContourAtts.singleColor = (255, 0, 0, 255)
	ContourAtts.SetMultiColor(0, (255, 0, 0, 255))
	ContourAtts.SetMultiColor(1, (0, 255, 0, 255))
	ContourAtts.SetMultiColor(2, (0, 0, 255, 255))
	ContourAtts.SetMultiColor(3, (0, 255, 255, 255))
	ContourAtts.SetMultiColor(4, (255, 0, 255, 255))
	ContourAtts.SetMultiColor(5, (255, 255, 0, 255))
	ContourAtts.SetMultiColor(6, (255, 135, 0, 255))
	ContourAtts.SetMultiColor(7, (255, 0, 135, 255))
	ContourAtts.SetMultiColor(8, (168, 168, 168, 255))
	ContourAtts.SetMultiColor(9, (255, 68, 68, 255))
	ContourAtts.contourNLevels = 10
	ContourAtts.contourValue = ()
	ContourAtts.contourPercent = ()
	ContourAtts.contourMethod = ContourAtts.Value  # Level, Value, Percent
	ContourAtts.minFlag = 0
	ContourAtts.maxFlag = 0
	ContourAtts.min = 0
	ContourAtts.max = 1
	ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
	ContourAtts.wireframe = 0
	SetPlotOptions(ContourAtts)
	ContourAtts = ContourAttributes()
	ContourAtts.defaultPalette.GetControlPoints(0).colors = (255, 0, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(0).position = 0
	ContourAtts.defaultPalette.GetControlPoints(1).colors = (0, 255, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(1).position = 0.034
	ContourAtts.defaultPalette.GetControlPoints(2).colors = (0, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(2).position = 0.069
	ContourAtts.defaultPalette.GetControlPoints(3).colors = (0, 255, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(3).position = 0.103
	ContourAtts.defaultPalette.GetControlPoints(4).colors = (255, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(4).position = 0.138
	ContourAtts.defaultPalette.GetControlPoints(5).colors = (255, 255, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(5).position = 0.172
	ContourAtts.defaultPalette.GetControlPoints(6).colors = (255, 135, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(6).position = 0.207
	ContourAtts.defaultPalette.GetControlPoints(7).colors = (255, 0, 135, 255)
	ContourAtts.defaultPalette.GetControlPoints(7).position = 0.241
	ContourAtts.defaultPalette.GetControlPoints(8).colors = (168, 168, 168, 255)
	ContourAtts.defaultPalette.GetControlPoints(8).position = 0.276
	ContourAtts.defaultPalette.GetControlPoints(9).colors = (255, 68, 68, 255)
	ContourAtts.defaultPalette.GetControlPoints(9).position = 0.31
	ContourAtts.defaultPalette.GetControlPoints(10).colors = (99, 255, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(10).position = 0.345
	ContourAtts.defaultPalette.GetControlPoints(11).colors = (99, 99, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(11).position = 0.379
	ContourAtts.defaultPalette.GetControlPoints(12).colors = (40, 165, 165, 255)
	ContourAtts.defaultPalette.GetControlPoints(12).position = 0.414
	ContourAtts.defaultPalette.GetControlPoints(13).colors = (255, 99, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(13).position = 0.448
	ContourAtts.defaultPalette.GetControlPoints(14).colors = (255, 255, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(14).position = 0.483
	ContourAtts.defaultPalette.GetControlPoints(15).colors = (255, 170, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(15).position = 0.517
	ContourAtts.defaultPalette.GetControlPoints(16).colors = (170, 79, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(16).position = 0.552
	ContourAtts.defaultPalette.GetControlPoints(17).colors = (150, 0, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(17).position = 0.586
	ContourAtts.defaultPalette.GetControlPoints(18).colors = (0, 150, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(18).position = 0.621
	ContourAtts.defaultPalette.GetControlPoints(19).colors = (0, 0, 150, 255)
	ContourAtts.defaultPalette.GetControlPoints(19).position = 0.655
	ContourAtts.defaultPalette.GetControlPoints(20).colors = (0, 109, 109, 255)
	ContourAtts.defaultPalette.GetControlPoints(20).position = 0.69
	ContourAtts.defaultPalette.GetControlPoints(21).colors = (150, 0, 150, 255)
	ContourAtts.defaultPalette.GetControlPoints(21).position = 0.724
	ContourAtts.defaultPalette.GetControlPoints(22).colors = (150, 150, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(22).position = 0.759
	ContourAtts.defaultPalette.GetControlPoints(23).colors = (150, 84, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(23).position = 0.793
	ContourAtts.defaultPalette.GetControlPoints(24).colors = (160, 0, 79, 255)
	ContourAtts.defaultPalette.GetControlPoints(24).position = 0.828
	ContourAtts.defaultPalette.GetControlPoints(25).colors = (255, 104, 28, 255)
	ContourAtts.defaultPalette.GetControlPoints(25).position = 0.862
	ContourAtts.defaultPalette.GetControlPoints(26).colors = (0, 170, 81, 255)
	ContourAtts.defaultPalette.GetControlPoints(26).position = 0.897
	ContourAtts.defaultPalette.GetControlPoints(27).colors = (68, 255, 124, 255)
	ContourAtts.defaultPalette.GetControlPoints(27).position = 0.931
	ContourAtts.defaultPalette.GetControlPoints(28).colors = (0, 130, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(28).position = 0.966
	ContourAtts.defaultPalette.GetControlPoints(29).colors = (130, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(29).position = 1
	ContourAtts.defaultPalette.smoothing = ContourAtts.defaultPalette.None  # None, Linear, CubicSpline
	ContourAtts.defaultPalette.equalSpacingFlag = 1
	ContourAtts.defaultPalette.discreteFlag = 1
	ContourAtts.defaultPalette.categoryName = "Standard"
	ContourAtts.changedColors = ()
	ContourAtts.colorType = ContourAtts.ColorByMultipleColors  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
	ContourAtts.colorTableName = "Default"
	ContourAtts.invertColorTable = 0
	ContourAtts.legendFlag = 1
	ContourAtts.lineStyle = ContourAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
	ContourAtts.lineWidth = 0
	ContourAtts.singleColor = (255, 0, 0, 255)
	ContourAtts.SetMultiColor(0, (255, 0, 0, 255))
	ContourAtts.SetMultiColor(1, (0, 255, 0, 255))
	ContourAtts.SetMultiColor(2, (0, 0, 255, 255))
	ContourAtts.SetMultiColor(3, (0, 255, 255, 255))
	ContourAtts.SetMultiColor(4, (255, 0, 255, 255))
	ContourAtts.SetMultiColor(5, (255, 255, 0, 255))
	ContourAtts.SetMultiColor(6, (255, 135, 0, 255))
	ContourAtts.SetMultiColor(7, (255, 0, 135, 255))
	ContourAtts.SetMultiColor(8, (168, 168, 168, 255))
	ContourAtts.SetMultiColor(9, (255, 68, 68, 255))
	ContourAtts.contourNLevels = 10
	ContourAtts.contourValue = (600)
	ContourAtts.contourPercent = ()
	ContourAtts.contourMethod = ContourAtts.Value  # Level, Value, Percent
	ContourAtts.minFlag = 0
	ContourAtts.maxFlag = 0
	ContourAtts.min = 0
	ContourAtts.max = 1
	ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
	ContourAtts.wireframe = 0
	SetPlotOptions(ContourAtts)
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
	SubsetAtts.SetMultiColor(2, (0, 0, 255, 255))
        SubsetAtts.subsetNames = ("1", "2", "3")
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
        DrawPlots()
# Begin spontaneous state
	View3DAtts = View3DAttributes()	
	print  i
	if i>3000 and i<=21000:
		angle=(i-3000)/100.0*2.0*3.1415/180.0
	else:
		print "Inside here"
		angle=2.0*3.1415/180.0
	View3DAtts.viewNormal = (0.15, math.cos(angle), math.sin(angle))
	View3DAtts.focus = (7.5, 0, 3.5)
	View3DAtts.viewUp = (1.0, 0.0, 0.0)
	View3DAtts.viewAngle = 30
	View3DAtts.parallelScale = 12.3895
	View3DAtts.nearPlane = -24.779
	View3DAtts.farPlane = 24.779
	View3DAtts.imagePan = (0, 0)
	View3DAtts.imageZoom = 1.21
	View3DAtts.perspective = 0
	View3DAtts.eyeAngle = 2
	View3DAtts.centerOfRotationSet = 0
	View3DAtts.centerOfRotation = (7.5, 0, 3.5)
	View3DAtts.axis3DScaleFlag = 0
	View3DAtts.axis3DScales = (1, 1, 1)
	View3DAtts.shear = (0, 0, 1)
	View3DAtts.windowValid = 1
	SetView3D(View3DAtts)
	# End spontaneous state
	
	ViewCurveAtts = ViewCurveAttributes()
	ViewCurveAtts.domainCoords = (0, 1)
	ViewCurveAtts.rangeCoords = (0, 1)
	ViewCurveAtts.viewportCoords = (0.2, 0.95, 0.15, 0.95)
	ViewCurveAtts.domainScale = ViewCurveAtts.LINEAR  # LINEAR, LOG
	ViewCurveAtts.rangeScale = ViewCurveAtts.LINEAR  # LINEAR, LOG
	SetViewCurve(ViewCurveAtts)
	View2DAtts = View2DAttributes()
	View2DAtts.windowCoords = (0, 15, -5, 12)
	View2DAtts.viewportCoords = (0.2, 0.95, 0.15, 0.95)
	View2DAtts.fullFrameActivationMode = View2DAtts.Auto  # On, Off, Auto
	View2DAtts.fullFrameAutoThreshold = 100
	View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
	View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
	View2DAtts.windowValid = 1
	SetView2D(View2DAtts)
	View3DAtts = View3DAttributes()
	View3DAtts.viewNormal = (0.15, math.cos(angle), math.sin(angle))
	View3DAtts.focus = (7.5, 0, 3.5)
	View3DAtts.viewUp = (1.0, 0.0, 0.0)
	View3DAtts.viewAngle = 30
	View3DAtts.parallelScale = 12.3895
	View3DAtts.nearPlane = -24.779
	View3DAtts.farPlane = 24.779
	View3DAtts.imagePan = (0, 0)
	View3DAtts.imageZoom = 1.21
	View3DAtts.perspective = 0
	View3DAtts.eyeAngle = 2
	View3DAtts.centerOfRotationSet = 0
	View3DAtts.centerOfRotation = (7.5, 0, 3.5)
	View3DAtts.axis3DScaleFlag = 0
	View3DAtts.axis3DScales = (1, 1, 1)
	View3DAtts.shear = (0, 0, 1)
	View3DAtts.windowValid = 1
	SetView3D(View3DAtts)
	ViewAxisArrayAtts = ViewAxisArrayAttributes()
	ViewAxisArrayAtts.domainCoords = (0, 1)
	ViewAxisArrayAtts.rangeCoords = (0, 1)
	ViewAxisArrayAtts.viewportCoords = (0.15, 0.9, 0.1, 0.85)
	SetViewAxisArray(ViewAxisArrayAtts)
 # Logging for SetAnnotationObjectOptions is not implemented yet.
        AnnotationAtts = AnnotationAttributes()
        AnnotationAtts.axes2D.visible = 1
        AnnotationAtts.axes2D.autoSetTicks = 1
        AnnotationAtts.axes2D.autoSetScaling = 1
        AnnotationAtts.axes2D.lineWidth = 0
        AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
        AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
        AnnotationAtts.axes2D.xAxis.title.visible = 1
        AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Courier  # Arial, Courier, Times
        AnnotationAtts.axes2D.xAxis.title.font.scale = 1
        AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
        AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
        AnnotationAtts.axes2D.xAxis.title.font.bold = 1
        AnnotationAtts.axes2D.xAxis.title.font.italic = 1
        AnnotationAtts.axes2D.xAxis.title.userTitle = 0
        AnnotationAtts.axes2D.xAxis.title.userUnits = 0
        AnnotationAtts.axes2D.xAxis.title.title = "X-Axis"
        AnnotationAtts.axes2D.xAxis.title.units = ""
        AnnotationAtts.axes2D.xAxis.label.visible = 1
        AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Courier  # Arial, Courier, Times
        AnnotationAtts.axes2D.xAxis.label.font.scale = 1
        AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
        AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
        AnnotationAtts.axes2D.xAxis.label.font.bold = 1
        AnnotationAtts.axes2D.xAxis.label.font.italic = 1
        AnnotationAtts.axes2D.xAxis.label.scaling = 0
        AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
        AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
        AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
        AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
        AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
        AnnotationAtts.axes2D.xAxis.grid = 0
        AnnotationAtts.axes2D.yAxis.title.visible = 1
        AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Courier  # Arial, Courier, Times
        AnnotationAtts.axes2D.yAxis.title.font.scale = 1
        AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
        AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
        AnnotationAtts.axes2D.yAxis.title.font.bold = 1
        AnnotationAtts.axes2D.yAxis.title.font.italic = 1
        AnnotationAtts.axes2D.yAxis.title.userTitle = 0
        AnnotationAtts.axes2D.yAxis.title.userUnits = 0
        AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis"
        AnnotationAtts.axes2D.yAxis.title.units = ""
        AnnotationAtts.axes2D.yAxis.label.visible = 1
        AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Courier  # Arial, Courier, Times
        AnnotationAtts.axes2D.yAxis.label.font.scale = 1
        AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
        AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
        AnnotationAtts.axes2D.yAxis.label.font.bold = 1
        AnnotationAtts.axes2D.yAxis.label.font.italic = 1
        AnnotationAtts.axes2D.yAxis.label.scaling = 0
        AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
        AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
        AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
        AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
        AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
        AnnotationAtts.axes2D.yAxis.grid = 0
        AnnotationAtts.axes3D.visible = 1
        AnnotationAtts.axes3D.autoSetTicks = 1
        AnnotationAtts.axes3D.autoSetScaling = 1
        AnnotationAtts.axes3D.lineWidth = 0
        AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
        AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
        AnnotationAtts.axes3D.triadFlag = 0
        AnnotationAtts.axes3D.bboxFlag = 1
        AnnotationAtts.axes3D.xAxis.title.visible = 0
        AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
        AnnotationAtts.axes3D.xAxis.title.font.scale = 1
        AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
        AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
        AnnotationAtts.axes3D.xAxis.title.font.bold = 0
        AnnotationAtts.axes3D.xAxis.title.font.italic = 0
        AnnotationAtts.axes3D.xAxis.title.userTitle = 0
        AnnotationAtts.axes3D.xAxis.title.userUnits = 0
        AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
        AnnotationAtts.axes3D.xAxis.title.units = ""
        AnnotationAtts.axes3D.xAxis.label.visible = 1
        AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
        AnnotationAtts.axes3D.xAxis.label.font.scale = 1
        AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
        AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
        AnnotationAtts.axes3D.xAxis.label.font.bold = 0
        AnnotationAtts.axes3D.xAxis.label.font.italic = 0
        AnnotationAtts.axes3D.xAxis.label.scaling = 0
        AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
        AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
        AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
        AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
        AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
        AnnotationAtts.axes3D.xAxis.grid = 0
        AnnotationAtts.axes3D.yAxis.title.visible = 0
        AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
        AnnotationAtts.axes3D.yAxis.title.font.scale = 1
        AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
        AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
        AnnotationAtts.axes3D.yAxis.title.font.bold = 0
        AnnotationAtts.axes3D.yAxis.title.font.italic = 0
        AnnotationAtts.axes3D.yAxis.title.userTitle = 0
        AnnotationAtts.axes3D.yAxis.title.userUnits = 0
	AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
        AnnotationAtts.axes3D.yAxis.title.units = ""
        AnnotationAtts.axes3D.yAxis.label.visible = 1
        AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
        AnnotationAtts.axes3D.yAxis.label.font.scale = 1
        AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
        AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
        AnnotationAtts.axes3D.yAxis.label.font.bold = 0
        AnnotationAtts.axes3D.yAxis.label.font.italic = 0
        AnnotationAtts.axes3D.yAxis.label.scaling = 0
        AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
        AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
        AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
        AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
        AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
        AnnotationAtts.axes3D.yAxis.grid = 0
        AnnotationAtts.axes3D.zAxis.title.visible = 0
        AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
        AnnotationAtts.axes3D.zAxis.title.font.scale = 1
        AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
        AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
        AnnotationAtts.axes3D.zAxis.title.font.bold = 0
        AnnotationAtts.axes3D.zAxis.title.font.italic = 0
        AnnotationAtts.axes3D.zAxis.title.userTitle = 0
        AnnotationAtts.axes3D.zAxis.title.userUnits = 0
        AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
        AnnotationAtts.axes3D.zAxis.title.units = ""
        AnnotationAtts.axes3D.zAxis.label.visible = 1
        AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
        AnnotationAtts.axes3D.zAxis.label.font.scale = 1
        AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
        AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
        AnnotationAtts.axes3D.zAxis.label.font.bold = 0
        AnnotationAtts.axes3D.zAxis.label.font.italic = 0
        AnnotationAtts.axes3D.zAxis.label.scaling = 0
        AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
        AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
        AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
        AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
        AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
        AnnotationAtts.axes3D.zAxis.grid = 0
        AnnotationAtts.axes3D.setBBoxLocation = 0
        AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
        AnnotationAtts.userInfoFlag = 0
        AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
        AnnotationAtts.userInfoFont.scale = 1
        AnnotationAtts.userInfoFont.useForegroundColor = 1
        AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
        AnnotationAtts.userInfoFont.bold = 0
        AnnotationAtts.userInfoFont.italic = 0
 	AnnotationAtts.databaseInfoFlag = 0
        AnnotationAtts.timeInfoFlag = 1
        AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
        AnnotationAtts.databaseInfoFont.scale = 1
        AnnotationAtts.databaseInfoFont.useForegroundColor = 1
        AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
        AnnotationAtts.databaseInfoFont.bold = 0
        AnnotationAtts.databaseInfoFont.italic = 0
        AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
        AnnotationAtts.databaseInfoTimeScale = 1
        AnnotationAtts.databaseInfoTimeOffset = 0
        AnnotationAtts.legendInfoFlag = 0
        AnnotationAtts.backgroundColor = (255, 255, 255, 255)
        AnnotationAtts.foregroundColor = (0, 0, 0, 255)
        AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
        AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
        AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
        AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
        AnnotationAtts.backgroundImage = ""
        AnnotationAtts.imageRepeatX = 1
        AnnotationAtts.imageRepeatY = 1
        AnnotationAtts.axesArray.visible = 1
        AnnotationAtts.axesArray.ticksVisible = 1
        AnnotationAtts.axesArray.autoSetTicks = 1
        AnnotationAtts.axesArray.autoSetScaling = 1
        AnnotationAtts.axesArray.lineWidth = 0
        AnnotationAtts.axesArray.axes.title.visible = 1
        AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
        AnnotationAtts.axesArray.axes.title.font.scale = 1
        AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
        AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
        AnnotationAtts.axesArray.axes.title.font.bold = 0
        AnnotationAtts.axesArray.axes.title.font.italic = 0
        AnnotationAtts.axesArray.axes.title.userTitle = 0
        AnnotationAtts.axesArray.axes.title.userUnits = 0
        AnnotationAtts.axesArray.axes.title.title = ""
        AnnotationAtts.axesArray.axes.title.units = ""
        AnnotationAtts.axesArray.axes.label.visible = 1
        AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
        AnnotationAtts.axesArray.axes.label.font.scale = 1
        AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
        AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
        AnnotationAtts.axesArray.axes.label.font.bold = 0
        AnnotationAtts.axesArray.axes.label.font.italic = 0
        AnnotationAtts.axesArray.axes.label.scaling = 0
        AnnotationAtts.axesArray.axes.tickMarks.visible = 1
        AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
        AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
        AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
        AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
	AnnotationAtts.axesArray.axes.grid = 0
        SetAnnotationAttributes(AnnotationAtts)

	SaveWindowAtts = SaveWindowAttributes()
	SaveWindowAtts.outputToCurrentDirectory = 0
	SaveWindowAtts.outputDirectory = "./Figures"
	SaveWindowAtts.fileName = filename
	SaveWindowAtts.family = 0
	SaveWindowAtts.format = SaveWindowAtts.JPEG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
	SaveWindowAtts.width = 1024
	SaveWindowAtts.height = 1024
	SaveWindowAtts.screenCapture = 0
	SaveWindowAtts.saveTiled = 0
	SaveWindowAtts.quality = 80
	SaveWindowAtts.progressive = 0
	SaveWindowAtts.binary = 0
	SaveWindowAtts.stereo = 0
	SaveWindowAtts.compression = SaveWindowAtts.None  # None, PackBits, Jpeg, Deflate
	SaveWindowAtts.forceMerge = 0
	SaveWindowAtts.resConstraint = SaveWindowAtts.ScreenProportions  # NoConstraint, EqualWidthHeight, ScreenProportions
	SaveWindowAtts.advancedMultiWindowSave = 0
	SaveWindowAtts.subWindowAtts.win1.position = (0, 0)
	SaveWindowAtts.subWindowAtts.win1.size = (128, 128)
	SaveWindowAtts.subWindowAtts.win1.layer = 0
	SaveWindowAtts.subWindowAtts.win1.transparency = 0
	SaveWindowAtts.subWindowAtts.win1.omitWindow = 0
	SaveWindowAtts.subWindowAtts.win2.position = (0, 0)
	SaveWindowAtts.subWindowAtts.win2.size = (128, 128)
	SaveWindowAtts.subWindowAtts.win2.layer = 0
	SaveWindowAtts.subWindowAtts.win2.transparency = 0
	SaveWindowAtts.subWindowAtts.win2.omitWindow = 0
	SaveWindowAtts.subWindowAtts.win3.position = (0, 0)
	SaveWindowAtts.subWindowAtts.win3.size = (128, 128)
	SaveWindowAtts.subWindowAtts.win3.layer = 0
	SaveWindowAtts.subWindowAtts.win3.transparency = 0
	SaveWindowAtts.subWindowAtts.win3.omitWindow = 0
	SaveWindowAtts.subWindowAtts.win4.position = (0, 0)
	SaveWindowAtts.subWindowAtts.win4.size = (128, 128)
	SaveWindowAtts.subWindowAtts.win4.layer = 0
	SaveWindowAtts.subWindowAtts.win4.transparency = 0
	SaveWindowAtts.subWindowAtts.win4.omitWindow = 0
	SaveWindowAtts.subWindowAtts.win5.position = (0, 0)
	SaveWindowAtts.subWindowAtts.win5.size = (128, 128)
	SaveWindowAtts.subWindowAtts.win5.layer = 0
	SaveWindowAtts.subWindowAtts.win5.transparency = 0
	SaveWindowAtts.subWindowAtts.win5.omitWindow = 0
	SaveWindowAtts.subWindowAtts.win6.position = (0, 0)
	SaveWindowAtts.subWindowAtts.win6.size = (128, 128)
	SaveWindowAtts.subWindowAtts.win6.layer = 0
	SaveWindowAtts.subWindowAtts.win6.transparency = 0
	SaveWindowAtts.subWindowAtts.win6.omitWindow = 0
	SaveWindowAtts.subWindowAtts.win7.position = (0, 0)
	SaveWindowAtts.subWindowAtts.win7.size = (128, 128)
	SaveWindowAtts.subWindowAtts.win7.layer = 0
	SaveWindowAtts.subWindowAtts.win7.transparency = 0
	SaveWindowAtts.subWindowAtts.win7.omitWindow = 0
	SaveWindowAtts.subWindowAtts.win8.position = (0, 0)
	SaveWindowAtts.subWindowAtts.win8.size = (128, 128)
	SaveWindowAtts.subWindowAtts.win8.layer = 0
	SaveWindowAtts.subWindowAtts.win8.transparency = 0
	SaveWindowAtts.subWindowAtts.win8.omitWindow = 0
	SaveWindowAtts.subWindowAtts.win9.position = (0, 0)
	SaveWindowAtts.subWindowAtts.win9.size = (128, 128)
	SaveWindowAtts.subWindowAtts.win9.layer = 0
	SaveWindowAtts.subWindowAtts.win9.transparency = 0
	SaveWindowAtts.subWindowAtts.win9.omitWindow = 0
	SaveWindowAtts.subWindowAtts.win10.position = (0, 0)
	SaveWindowAtts.subWindowAtts.win10.size = (128, 128)
	SaveWindowAtts.subWindowAtts.win10.layer = 0
	SaveWindowAtts.subWindowAtts.win10.transparency = 0
	SaveWindowAtts.subWindowAtts.win10.omitWindow = 0
	SaveWindowAtts.subWindowAtts.win11.position = (0, 0)
	SaveWindowAtts.subWindowAtts.win11.size = (128, 128)
	SaveWindowAtts.subWindowAtts.win11.layer = 0
	SaveWindowAtts.subWindowAtts.win11.transparency = 0
	SaveWindowAtts.subWindowAtts.win11.omitWindow = 0
	SaveWindowAtts.subWindowAtts.win12.position = (0, 0)
	SaveWindowAtts.subWindowAtts.win12.size = (128, 128)
	SaveWindowAtts.subWindowAtts.win12.layer = 0
	SaveWindowAtts.subWindowAtts.win12.transparency = 0
	SaveWindowAtts.subWindowAtts.win12.omitWindow = 0
	SaveWindowAtts.subWindowAtts.win13.position = (0, 0)
	SaveWindowAtts.subWindowAtts.win13.size = (128, 128)
	SaveWindowAtts.subWindowAtts.win13.layer = 0
	SaveWindowAtts.subWindowAtts.win13.transparency = 0
	SaveWindowAtts.subWindowAtts.win13.omitWindow = 0
	SaveWindowAtts.subWindowAtts.win14.position = (0, 0)
	SaveWindowAtts.subWindowAtts.win14.size = (128, 128)
	SaveWindowAtts.subWindowAtts.win14.layer = 0
	SaveWindowAtts.subWindowAtts.win14.transparency = 0
	SaveWindowAtts.subWindowAtts.win14.omitWindow = 0
	SaveWindowAtts.subWindowAtts.win15.position = (0, 0)
	SaveWindowAtts.subWindowAtts.win15.size = (128, 128)
	SaveWindowAtts.subWindowAtts.win15.layer = 0
	SaveWindowAtts.subWindowAtts.win15.transparency = 0
	SaveWindowAtts.subWindowAtts.win15.omitWindow = 0
	SaveWindowAtts.subWindowAtts.win16.position = (0, 0)
	SaveWindowAtts.subWindowAtts.win16.size = (128, 128)
	SaveWindowAtts.subWindowAtts.win16.layer = 0
	SaveWindowAtts.subWindowAtts.win16.transparency = 0
	SaveWindowAtts.subWindowAtts.win16.omitWindow = 0
	SetSaveWindowAttributes(SaveWindowAtts)

	SaveWindow()
	DeleteActivePlots()
	DeleteActivePlots()
	OpenDatabase(solnfile)
#	TimeSliderNextState()
	
