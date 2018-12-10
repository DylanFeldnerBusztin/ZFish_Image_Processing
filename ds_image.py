def ds_img(img):
# Create downsampled image

    import ants
    import numpy
    from scipy.ndimage import zoom
    import scipy
    from PIL import Image
    import warnings
    warnings.filterwarnings('ignore', '.*output shape of zoom.*')
    
    input1  = img_path
    input_array = input1.numpy
    
    downsampled_array = zoom(input_array(), (0.66, 1, 0.145))
    
    # Create image from array
    downsampled_image = ants.from_numpy(downsampled_array)
    
    # Write downsampled image to file
    # ants.image_write(downsampled_image, 'downsampled_4.tif_')
    
    return downsampled_image

    # Old code
    # downsampled_array = zoom(input_array(), (0.33, 0.504, 0.073))
    # downsampled_array = zoom(input_array(), (0.66, 1, 0.145))

     # print(input_array().shape)
     # print(downsampled_array.shape)