# -*- coding: utf-8 -*-
"""

File initiated by Tristan Amaral, Univ. of Idaho, Nov 16, 2018
Modifications by Tim Bartholomaus on Dec 4, 2018

Extracts an evenly spaced profile, defined along a shapefile polyline,
    from a geotiff.
    
"""

#%%
def extract_profile(tif, line_file, ds):
    """ Extracts an evenly spaced profile, defined along a shapefile polyline,
    from a geotiff.
    
    Inputs include:
        tif: a geotiff file passed as a string (with path).  File is
                    expected to have units of meters.
        line_file: a shapefile (string of filename, with path) consisting
                    of only one polyline along which to extract the 
                    profile values.
        ds: the spacing of points along the polyline at which to extract
                    profile values from the geotiff, assumed to be in meters.
                    
    Returns include:
        disti: a vector (np.array) of evenly-space distances along
                    the shapefile.
        profile: values drawn from tif at the distances of disti.
        
    """

    import numpy as np
    import gdal
    import fiona
    from scipy.interpolate import interp1d
#    from scipy.interpolate import interp2d
    from scipy.ndimage import map_coordinates
    
    #%% Create evenly spaced points
    # Read coordinates of the profile line from shapefile
    fiona_obj = fiona.open(line_file)
#    line = fiona_obj.next()
    line = iter(fiona_obj).next() # this line is proper syntax for fiona v2.  Corrected on Mar 12, 2021 by TCB
    coords = np.array( line['geometry']['coordinates'] ) # m the easting and northing coordinates of the vertices along the shapefile
    
    sqrd_deltas = np.diff(coords, axis=0)**2 # squared differences between x and y coordinates
    deltas = np.sum(sqrd_deltas, axis=1)**0.5 # m  straight-line path length between adjacent points in the shapefile
    dist = np.cumsum( np.append(0, deltas) ) # m  running distance along the shapefile from one end.
    
    disti = np.arange(dist[0], dist[-1], ds) # m  vector of evenly spaced distances along the shapefile,
                                                    # equivalent to an evenly spaced version of dist
    xi = interp1d(dist, coords[:,0])(disti) # m  the easting coordinates of disti points, at which profile will be extracted
    yi = interp1d(dist, coords[:,1])(disti) # m  the northing coordinates of disti points, at which profile will be extracted

    #%% Manipulate the raster and extract its data
    # ---- dimensions of geotiff
    gtif = gdal.Open(tif)
    xmin,xres,xskew,ymax,yskew,yres = gtif.GetGeoTransform()


    # convert the profile coordinates into pixel coordinates
    px = (xi - xmin) / xres
    py = (yi - ymax) / yres
#    px = np.round(col).astype(int)
#    py = np.round(row).astype(int)
    
    
    # pull out the array of raster data.  Data are assumed to be in band 1.
    gtif_data = gtif.GetRasterBand(1).ReadAsArray()
#    gtif_data = band.ReadAsArray()px,py, 1, 1)
    
    # Two early versions of extacting the data:
            #    profile = map_coordinates(gtif_data,[px,py],order=0,cval=np.nan)
            #    profile = interp2d(np.arange(gtif_data.shape[1]), np.arange(gtif_data.shape[0]), 
            #                       gtif_data)(px, py)

    # Interpolate within gtif_data at given pixel coordinates to identify values from the geotiff  
    #   Uses a 1st order spline interpolant to extract estimated values of
    #   gtif_data at the (non-integer) pixel values px and py.
    #   Function returns `cval' at undefined values of gtif_data.
    profile = map_coordinates(gtif_data, np.vstack((py, px)),
                              order=1, cval=np.nan)
    
#    profile = np.array(profile,dtype=float)
    if type(profile[0]) == float:
        profile[np.abs(profile) == 9999] = np.nan
   
    return disti, profile
        
#%%
