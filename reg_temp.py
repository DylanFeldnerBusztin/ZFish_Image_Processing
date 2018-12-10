def reg_temp(fi, mo):
    
    # template dimensions: 1406, 621, 138
    # mean dimensions: 464, 313, 10
    
    import ants
    import numpy as np
    
    print( 'Before transform: ')
    print(ants.image_mutual_information(fi, mo))

    
    #fi = ants.iMath_histogram_equalization(fi, 0, 1)
    
    #fi = ds_image(fi)
    
    fi.set_direction(np.array([[1., 0., 0.],[0., 1., 0.],[0., 0., 1.]]))
    fi.set_spacing(list([0.798, 0.798, 2.0]))
    fi  = ants.crop_indices(fi, [90, 0, 0], [1200, 600, 138])
    fi  = ants.resample_image(image = fi, resample_params = [1, 1, 4])
    
    
    #mo = ants.iMath_histogram_equalization(mo, 0, 1)
    mo.set_direction(np.array([[1., 0., 0.],[0., 1., 0.],[0., 0., 1.]]))
    mo.set_spacing(list([1.6,1.6,8]))
    #   mo.set_spacing(list([1.6,1.6,8]))
    #   fi.set_spacing(list([0.798, 0.798, 2.0]))
    
    mrtr = ants.registration(fi, mo, type_of_transforms = 'Rigid', verbose = 1)
    mr   = ants.apply_transforms(fi, mo, transformlist=mrtr['fwdtransforms'])
    
    #fi  = ants.resample_image(image = fi, resample_params = [1.2, 1.2, 3.5])
    #fi.set_spacing(list([0.798, 0.798, 2.0]))
    #fi = ants.resample_image_to_target(fi, mo)
    
    #output = ants.registration(fi, mo, type_of_transform='Rigid')
    
    ants.plot(fi , overlay_cmap = 'magma', overlay = mr, overlay_alpha = .5, figsize = 4, axis = 2, slices = range(9))
    
    #print( 'After Rigid transform: ')
    #print(ants.image_mutual_information(fi, output['warpedmovout']))
    
    #output = ants.registration(fi, mo, type_of_transform='Similarity')
    output = mr
    
    #print( 'After rigid transform: ')
    #print(ants.image_mutual_information(fi, mr))
    
    #  output['warpedmovout'].plot
    
    #return output['warpedmovout']
    return output
    
# import ants
#template_image = '/home/dylan/Elavl3-H2BRFP.tif'    
#temp = ants.image_read(template_image)
#temp.set_spacing(list([0.798, 0.798, 2.0]))
#mean_image = ants.image_read('/home/dylan/Downloads/Mean_Image_2.tif')
#fi  = ants.resample_image(image = temp, resample_params = [1.2, 1.2, 3.5])