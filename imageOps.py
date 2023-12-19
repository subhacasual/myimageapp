from PIL import Image
import cv2
import base64
from io import BytesIO

# writing a function to perform operations on image,
def image_info(img_array):
    """
    This function will return the information of the image
    """
    size = img_array.size # total pixels
    width = img_array.shape[1]
    height = img_array.shape[0]
    channels = img_array.shape[2]

    return size, width, height, channels

def grey(img_array):
    """
    This function will convert the image to grey scale
    """
    grey_img = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    return grey_img

def resize(img_array, width, height):
    """ 
    This function will resize the image
    """
    resized_img = cv2.resize(img_array, (width, height))
    return resized_img

    

def get_image_download_link(img):
    """
    Generates a link allowing the PIL image to be downloaded
    """
    img = Image.fromarray(img)
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/jpg;base64,{img_str}" download ="result.jpg">Download Image</a>'
    return href