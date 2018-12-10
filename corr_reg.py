def corr_reg():
    
    import ants
    import numpy as np
    import os
    from scipy.stats.stats import pearsonr
    import matplotlib.pyplot as plt
    %matplotlib inline
    
    
    # Load mean image
    fix_mean = ants.image_read('/home/dylan/Mean_Image_1.tif')
    fix_mean.set_spacing(list([1.6,1.6,8]))
    
    # Create 1D array out of mean image
    mean_arr = fix_mean.numpy
    mean_arr = mean_arr()
    flat_mean_arr = mean_arr.flatten()
    
    # Path to raw files
    tifsFile = '/home/dylan/Desktop/Correlation_test_4'
    
    # The number of tifs in the folder
    numTifs = len(os.listdir(tifsFile))
    
    # Create empy array for plotting
    plot_arr = np.zeros((numTifs),np.float)
    
    # Loop through tifs registering them to the mean, then compile correlation array
    i = 0
    for mov_tif in os.listdir(tifsFile):
        
        # Register to mean image
        mov_tif = ants.image_read(tifsFile + os.sep + mov_tif)      
        mov_tif.set_direction(np.array([[1., 0., 0.],[0., 1., 0.],[0., 0., 1.]]))
        mov_tif.set_spacing(list([1.6,1.6,8]))
        reg_tif = ants.registration(fix_mean, mov_tif, type_of_transform='Rigid')
        
        # Create 1D array out of registered image
        reg_arr = reg_tif['warpedmovout'].numpy
        reg_arr = reg_arr()
        flat_reg_arr = reg_arr.flatten()
        
        # Add correlation to array
        corr = pearsonr(flat_mean_arr,flat_reg_arr)[0]
        plot_arr[i] = corr
        if corr < 0.7: 
            print(i)
            #ants.plot(reg_tif, fix_mean, overlay_cmap = 'magma', overlay_alpha = .7, axis = 2, slices = [3*x+40 for x in range(8)], figsize = 8)

        
        i = i + 1
        
    # Plot correlation     
    plt.style.use('dark_background')
    plt.plot(plot_arr)
    plt.ylabel('Pearson Correlation')
    plt.show()