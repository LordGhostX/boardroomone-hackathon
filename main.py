from dotenv import load_dotenv
import cloudinary_service

if __name__ == "__main__":
    load_dotenv()
    cloudinary_service.init_config()

    print(cloudinary_service.crop_image_with_detection("da0tnak5env6andrkwtl", 896, 592))
