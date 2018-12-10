def mean_Image():
    
    import ants
    import numpy
    import os
    
    # Initialise variables:

    # 1. A zero-array that will seventually contain the mean image. 
    # The array dimensions are hardcoded according to the image size
    meanArray = numpy.zeros((464,313,10),numpy.float)

    # 2. A temporary variable for the loop
    temp = ants.ANTsImage

    # 3. The filepath to the images
    tifsFile = '/home/dylan/Desktop/Image_Sequence'
    
    # 4. The number of tifs in the folder
    numTifs = len(os.listdir(tifsFile))
    
    # Loop through all tifs in the file, appending them to the meanArray

    for tif in os.listdir(tifsFile):
        # Assign tifs to temp
        temp = ants.image_read(tifsFile + os.sep + tif)

        # Convert temp to numpy array
        temp = temp.numpy

        # Add temp to the mean array after dividing it by total number of tifs
        meanArray = meanArray + temp()/numTifs
        
    # Convert meanArray back to an ANTsImage

    meanImage = ants.from_numpy(meanArray)
    
    # Write mean image to file

    ants.image_write(meanImage, 'Mean_Image_3.tif')

