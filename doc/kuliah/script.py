import shapefile
sf = shapefile.Reader("E:/Countries/countries.shp")
shapes = sf.shapes()
print len (shapes)
