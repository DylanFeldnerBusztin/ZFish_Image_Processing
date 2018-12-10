def reg_mean():
    
    import ants
    import numpy as np
    import os
    
    # Load mean image
    fix_mean = ants.image_read('/home/dylan/Mean_Image_1.tif')
    fix_mean.set_spacing(list([1.6,1.6,8]))
    
    # Import files
    tifsFile = '/home/dylan/Desktop/Image_Sequence'
    
    # The number of tifs in the folder
    numTifs = len(os.listdir(tifsFile))
    
    # Loop through tifs registering them to the mean
    i = 0
    for mov_tif in os.listdir(tifsFile):
        mov_tif = ants.image_read(tifsFile + os.sep + mov_tif)      
        mov_tif.set_direction(np.array([[1., 0., 0.],[0., 1., 0.],[0., 0., 1.]]))
        mov_tif.set_spacing(list([1.6,1.6,8]))
        reg_tif = ants.registration(fix_mean, mov_tif, type_of_transform='Rigid', )
        ants.image_write(reg_tif['warpedmovout'], str(i) + '_.tif')
        i = i + 1
    
    