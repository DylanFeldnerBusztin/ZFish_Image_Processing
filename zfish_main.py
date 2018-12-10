def zfish_main():
    
    import ants
    import ds_image
    from datetime import datetime
    
    # Downsample
    
    # Load template image
    template_image = '/home/dylan/Elavl3-H2BRFP.tif'
    temp = ants.image_read(template_image)
    
    # Call downsampling script
    #%run -i ds_image.py
    #downsampled_image = ds_img(template_image)
    
    # Write to file
    # ants.image_write(downsampled_image, 'downsampled_' + datetime.now().strftime('%H_%M')+ '.tif')
    
    # Register
    
    # Load mean image
    mean_image = ants.image_read('/home/dylan/Downloads/Mean_Image_2.tif')
    
    # Run registration
    %run -i reg_temp.py
    registered_img = reg_temp(temp, mean_image)
    
    # Write to file
    #ants.image_write(registered_img, 'registered_' + datetime.now().strftime('%H_%M')+ '.tif')
    
    #ants.plot(temp, overlay_cmap = 'magma', overlay = registered_img, overlay_alpha = .5, figsize = 4, axis = 2, slices = range(9))
    
    # Old code
    # mean_image = ants.image_read('/home/dylan/Mean_Image_1.tif')
    # ants.plot(mean_image, figsize = 4)
    
    