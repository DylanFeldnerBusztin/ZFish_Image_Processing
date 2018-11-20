def reg_temp(fi, mo):
    
    import ants
    import numpy as np
    
    
    mo.set_direction(np.array([[1., 0., 0.],[0., 1., 0.],[0., 0., 1.]]))
    mo.set_spacing(list([1.6,1.6,8]))
    #   mo.set_spacing(list([1.6,1.6,8]))
    #   fi.set_spacing(list([0.798, 0.798, 2.0]))
    
    
    fi.set_spacing(list([0.798, 0.798, 2.0]))
    #  "fi  = ants.crop_indices(fi, [90, 0, 0], [1200, 600, 138])\n",
    #  "fi  = ants.resample_image(image = fi, resample_params = [1, 1, 4]) "
    output = ants.registration(fi, mo, type_of_transform='SyN')
    
    #  print(fi)
    #  print(mo)
    #  print(output)
    
    #  output['warpedmovout'].plot
    
    return output['warpedmovout']
    