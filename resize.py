from PIL import Image



def resize_img(im):

    im.show()
    resized_im = im.resize((round(im.size[0]*0.5), round(im.size[1]*0.5)))


    return resized_im
    # resized_im.show()
    # resized_im.save('resizedBeach2.jpg')