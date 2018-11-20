def reg_line():
    
    import ants
    import numpy as np
    import os
    
    tifsFile = '/home/dylan/Desktop/ZFish/ZFish_ImageSequence_Reg'
    
    # The number of tifs in the folder
    numTifs = len(os.listdir(tifsFile))
    
    # Img array
    # A zero-array that will seventually contain the mean image. The array dimensions are hardcoded according to the image size
    img_arr = numpy.zeros((100,464,313),numpy.float)
    
    #print(ants.image_read(tifsFile + os.sep + tif).shape)
    exampleTif = ants.image_read(tifsFile + os.sep + os.listdir(tifsFile)[0])

    
    # Loop through tifs registering them to the mean
    i = 0
    for tif in os.listdir(tifsFile):
        tif = ants.image_read(tifsFile + os.sep + tif)
        tif = tif.numpy
        arr = tif()
        tif_frame = np.take(arr, 4, axis =2)
        #print(type(img_arr))
        #print(type(tif_frame))
        #print(tif_frame.shape)
        #img_arr = np.append(img_arr, tif_frame, axis = 2)
        img_arr[i] = tif_frame
    
    img_arr = np.moveaxis(img_arr, 0, -1)
    meanImage = ants.from_numpy(img_arr)
    ants.image_write(meanImage, 'test.tif')
    
    print(img_arr.shape)
        
        #img_arr = np.concatenate(img_arr, img_arr, axis = 2)
        