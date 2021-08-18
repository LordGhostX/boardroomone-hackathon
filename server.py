from flask import Flask, request, jsonify
from dotenv import load_dotenv
import cloudinary_service
from remove_bg_service import remove_image_background

# load environment variables and get the app running
load_dotenv()
cloudinary_service.init_config()
app = Flask(__name__)


@app.route("/profile/", methods=["POST"])
def create_profile_photo():
    # fetch the uploaded profile photo
    profile_photo = request.files.get("profilePhoto")

    # verify the profile photo was included in the request
    if profile_photo is None:
        return jsonify({
            "msg": "profilePhoto is a required argument",
            "data": None
        }), 400

    # remove the background of the profile photo
    image_without_background = remove_image_background(profile_photo)

    # upload the profile photo cloudinary
    uploaded_image = cloudinary_service.upload_image_with_detection(
        image_without_background)

    # crop the image stored in cloudinary and change the background color
    cropped_image = cloudinary_service.crop_image_with_detection(
        uploaded_image["public_id"],
        uploaded_image["height"],
        uploaded_image["width"]
    )

    # return the profile URL back to the user
    return jsonify({
        "msg": "successfully generated profile photo",
        "data": {
            "profilePhoto": cropped_image
        }
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
