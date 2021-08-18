import os
import cloudinary
import cloudinary.uploader
from utils import calculate_diagonal_size


# initialize cloudinary configuration variables
def init_config():
    cloudinary.config(
        cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),
        api_key=os.environ.get("CLOUDINARY_API_KEY"),
        api_secret=os.environ.get("CLOUDINARY_API_SECRET")
    )


# upload a given image to cloudinary for further processing
def upload_image(image_url_or_path, detection=None):
    result = cloudinary.uploader.upload(image_url_or_path, detection=detection)
    return result


# upload a given image to cloudinary and detect faces along the way
def upload_image_with_detection(image_url_or_path):
    return upload_image(image_url_or_path, detection="adv_face")


# crop the headshot of the user and fill the background
def crop_image_with_detection(public_id, height, width):
    diagonal_size = calculate_diagonal_size(height, width)

    return "https://res.cloudinary.com/{}/image/upload/c_thumb,g_adv_face,h_{},w_{},b_rgb:000/{}.png".format(
        os.environ.get("CLOUDINARY_CLOUD_NAME"),
        diagonal_size,
        diagonal_size,
        public_id
    )
