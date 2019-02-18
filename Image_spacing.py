import ants
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

class Image_spacing():
    
    # Prepare template
    #fi = ants.image_read('/home/dylan/Elavl3-H2BRFP.tif')
    #mo = ants.image_read('/home/dylan/Desktop/Lab/Substack_Red_large.tif')
    
    
    
    fi.set_spacing(list([0.798, 0.798, 2.0]))
    mo.set_spacing(list([0.798, 0.798, 2.0]))
    
    print(ants.image_physical_space_consistency(fi,mo))
    
    mrtr_r = ants.registration(fi, mo, type_of_transforms = 'QuickSyN', grad_step = 0.1)
    mrtr = ants.apply_transforms(fi, mo, transformlist=mrtr_r['fwdtransforms'])
    
    ants.plot(mrtr,fi, overlay_cmap = 'magma', overlay_alpha = .7, axis = 2, figsize = 20, slices = [x for x in range(8)])
    
    ants.plot(fi, mrtr, overlay_cmap = 'magma', overlay_alpha = .7, axis = 2,figsize = 8, slices = [x for x in range(8)])
        

    
    
    
    
    
    
    
    """
    
    print(fi.view)
    print(mo.view)
    
    print(fi.shape)
    print(mo.shape)
    
    plt.style.use('dark_background')
   #plt.plot(f_arr, m_arr)
   #plt.ylabel('Number of moves to get to prey')
   #plt.xlabel('Trial')
  # plt.show()
  
  
  print(fi.spacing)
    print(mo.spacing)
    
    imlist = [fi,mo]
    
    imlist = ants.image_type_cast(imlist, pixeltype=None)
    
    #for i in range(5):
        
    fi.set_spacing(list([0.798, 0.798, 2.0]))
    mo.set_direction(np.array([[-1., 0., 0.],[0., 1., 0.],[0., 0., 1.]]))
    mo.set_spacing(list([0.55,0.22, 20.0]))
    
    
    """