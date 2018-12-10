def reg_line():
    
    import ants
    import numpy as np
    import os
    
    tifsFile = '/home/dylan/Desktop/ZFish/ZFish_ImageSequence_Reg'
    tifsFile_Raw = '/home/dylan/Desktop/ZFish/ZFish_ImageSequence'
    
    # The number of tifs in the folder
    numTifs = len(os.listdir(tifsFile))
    
    # Img array
    # A zero-array that will seventually contain the mean image. The array dimensions are hardcoded according to the image size
    img_arr = numpy.zeros((100,464,313),numpy.float)
    img_arr_raw = numpy.zeros((100,464,313),numpy.float)
    
    # Loop through tifs collecting the middle frame and adding them to array
    i = 0
    for tif in os.listdir(tifsFile_Raw):
        tif = ants.image_read(tifsFile_Raw + os.sep + tif)
        tif = tif.numpy
        arr = tif()
        tif_frame = np.take(arr, 4, axis =2)
        img_arr_raw[i] = tif_frame
        i = i + 1

    
    # Loop through tifs collecting the middle frame and adding them to array
    i = 0
    for tif in os.listdir(tifsFile):
        tif = ants.image_read(tifsFile + os.sep + tif)
        tif = tif.numpy
        arr = tif()
        tif_frame = np.take(arr, 4, axis =2)
        img_arr[i] = tif_frame
        i = i + 1
    
    img_arr = np.moveaxis(img_arr, 0, -1)
    regImage = ants.from_numpy(img_arr)
    ants.image_write(regImage, 'test_reg2.tif')
    
    img_arr_raw = np.moveaxis(img_arr_raw, 0, -1)
    rawImage = ants.from_numpy(img_arr_raw)
    ants.image_write(rawImage, 'test_raw2.tif')
    
    print(img_arr.shape)
        
        