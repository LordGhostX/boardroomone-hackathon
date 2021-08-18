from dotenv import load_dotenv
import cloudinary_service
from remove_bg_service import remove_image_background

if __name__ == "__main__":
    load_dotenv()
    cloudinary_service.init_config()

    # read file
    image_file = open("image.jpg", "rb")

    # remove background
    image_without_background = remove_image_background(image_file)

    # upload to cloudinary
    uploaded_image = cloudinary_service.upload_image_with_detection(image_without_background)

    # crop image
    cropped_image = cloudinary_service.crop_image_with_detection(
        uploaded_image["public_id"],
        uploaded_image["height"],
        uploaded_image["width"]
    )

    # return final URL
    print(cropped_image)
