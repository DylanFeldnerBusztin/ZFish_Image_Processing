def template_registration():
    
    import numpy as np              # general calculations and stuff
    import ants                     # advanced normalisation tools
    import os                       # dealing with files, paths and extensions and the like
    import matplotlib.pyplot as plt # general plotting capabilities    
    #import nibabel as nib           # to open nii files (if necessary)
    import re                       # regular expressions for finding files
    import shutil                   # to copy transform files out for storage
    import h5py                     # to read anatomical maps stored in H5
    from datetime import datetime
    
    fi  = ants.image_read('/home/dylan/Elavl3-H2BRFP.tif')
    fi.set_spacing(list([0.798, 0.798, 2.0]))
    fi  = ants.crop_indices(fi, [90, 0, 0], [1200, 600, 138])
    fi  = ants.resample_image(image = fi, resample_params = [1, 1, 4])
    
    mo = ants.image_read('/home/dylan/ANTsPy/Mean_Image_2.tif')
    mo.set_direction(np.array([[1., 0., 0.],[0., 1., 0.],[0., 0., 1.]]))
    mo.set_spacing(list([1.6,1.6,8]))
    
    mrtr_r = ants.registration(fi, mo, type_of_transforms = 'Rigid', verbose = 1, gradientStep = 0.1)
    mr_r   = ants.apply_transforms(fi, mo, transformlist=mrtr['fwdtransforms'])
    ants.plot(fi, mr_r, overlay_cmap = 'magma', overlay_alpha = .7, axis = 2, slices = [3*x+40 for x in range(8)], figsize = 8)
    
    mrtr_s = ants.registration(fi, mr_r, type_of_transforms = 'SyN', verbose = 1, gradientStep = 0.1)
    mr_s   = ants.apply_transforms(fi, mr_r, transformlist=mrtr['fwdtransforms'])
    ants.plot(fi, mr_r, overlay_cmap = 'magma', overlay_alpha = .7, axis = 2, slices = [3*x+40 for x in range(8)], figsize = 8)
    
    
    ants.image_write(mr_r, 'registered_' + datetime.now().strftime('%H_%M')+ '.tif')
    
    
    
    # mrtr = ants.registration(fi, mo, type_of_transforms = 'Rigid', verbose = 1, grad_step=0.1, )
    
    # matplotlib, imshow, use vmax and vmin for display