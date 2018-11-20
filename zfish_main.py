def zfish_main():
    
    import ants
    import ds_image
    from datetime import datetime
    
    # Downsample
    
    # Load template image
    template_image = '/home/dylan/Elavl3-H2BRFP.tif'
    # Call ds script
    %run -i ds_image.py
    downsampled_image = ds_img(template_image)
    # Write to file
    # ants.image_write(downsampled_image, 'downsampled_' + datetime.now().strftime('%H_%M')+ '.tif')
    
    # Register
    
    # Load mean image
    mean_image = ants.image_read('/home/dylan/Mean_Image_1.tif')
     # Run registration
    %run -i reg_temp.py
    registered_img = reg_temp(downsampled_image, mean_image)
    # Write to file
    ants.image_write(registered_img, 'registered_' + datetime.now().strftime('%H_%M')+ '.tif')