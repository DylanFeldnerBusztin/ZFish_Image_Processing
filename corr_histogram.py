def corr_histogram():
    
    import ants
    import numpy as np
    import os
    from scipy.stats.stats import pearsonr
    import matplotlib.pyplot as plt
    
    # Load mean image
    fix_mean = ants.image_read('/home/dylan/Mean_Image_1.tif')
    fix_mean.set_spacing(list([1.6,1.6,8]))
    
    # Convert mean image to 1D array
    mean_arr = fix_mean.numpy
    mean_arr = mean_arr()
    flat_mean_arr = mean_arr.flatten()

    # Load tif file path
    tifsFile = '/home/dylan/Desktop/Correlation_test_2'
    
    # The number of tifs in the folder
    numTifs = len(os.listdir(tifsFile))
    
    # Create empy array for plotting
    plot_arr = np.zeros((numTifs),np.float)
    
    i = 0
    # Loop through tifs calculating correlations
    for mov_tif in os.listdir(tifsFile):
        # Convert mov image to 1D array
        mov_tif = ants.image_read(tifsFile + os.sep + mov_tif)
        mov_arr = mov_tif.numpy
        mov_arr = mov_arr()
        flat_mov_arr = mov_arr.flatten()
        # Plot correlation
        corr = pearsonr(flat_mean_arr,flat_mov_arr)[0]
        plot_arr[i] = corr
        if corr < 0.8: print(i)      
        
        i = i + 1
        
    plt.style.use('dark_background')
    plt.plot(plot_arr)
    plt.ylabel('Pearson Correlation')
    plt.show()
    
                                  

