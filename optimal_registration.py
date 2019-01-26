def optimal_registration():
    
    import ants
    import numpy as np
    import os
    from scipy.stats.stats import pearsonr
    import matplotlib.pyplot as plt
    %matplotlib inline
    import statistics
    import time
    
    # Program that solves optimal parameters for rigid registration of zebrafish images to the mean
    
    # File path
    tifsFile = '/home/dylan/Desktop/Image_Sequence_P_test_mini'
    
    # Load and prepare the mean image as the fixed image for registration
    meanImage = ants.image_read('/home/dylan/Mean_Image_PTZ.tif')
    fix_mean = meanImage
    fix_mean.set_spacing(list([1.6,1.6,8]))
    
    # Create a 1D array out of the mean image
    mean_arr = fix_mean.numpy
    mean_arr = mean_arr()
    flat_mean_arr = mean_arr.flatten()
    
    # The number of tifs in the folder
    numTifs = 100
    
    # Create an empty array for plotting
    plot_arr = np.zeros((numTifs),np.float)
    
    # The number of tifs in the folder
    numTifs = len(os.listdir(tifsFile))
    
    # Initialise performance variables
    aveTime = 0
    aveCorr = 0
    
    i = 0
    for mov_tif in os.listdir(tifsFile):
        
        # Assign tifs to temp
        temp = ants.image_read(tifsFile + os.sep + mov_tif)
        
        start = time.time()
            
        # Register to mean image
        mov_tif = ants.image_read(tifsFile + os.sep + mov_tif)      
        mov_tif.set_direction(np.array([[1., 0., 0.],[0., 1., 0.],[0., 0., 1.]]))            
        mov_tif.set_spacing(list([1.6,1.6,8]))
        reg_tif = ants.registration(fix_mean, mov_tif, type_of_transform='Rigid')
        
        end = time.time()

        # Create 1D array out of registered image
        reg_arr = reg_tif['warpedmovout'].numpy
        reg_arr = reg_arr()
        flat_reg_arr = reg_arr.flatten()

        # Add correlation to array
        corr = pearsonr(flat_mean_arr,flat_reg_arr)[0]
        plot_arr[i] = corr
        
        # Build average values
        aveTime = aveTime + (end - start)/ numTifs
        aveCorr = aveCorr + corr/numTifs
        
        # Check for anomalies
        if corr < 0.2: print(i)
            
        i = i + 1
        
    # Plot correlation     
    plt.style.use('dark_background')
    plt.plot(plot_arr)
    plt.ylabel('Pearson Correlation')
    plt.show()
    
    print('Average time ', round(aveTime,3))
    print('Average correlation ', round(aveCorr,3))