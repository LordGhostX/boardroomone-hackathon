import os
import requests


# calling the remove.bg API to remove the background of profile photos
def remove_image_background(file_resource):
    headers = {
        "X-Api-Key": os.environ.get("REMOVE_BG_API_KEY")
    }

    files = {
        "image_file": file_resource
    }

    payload = {
        "size": "auto",
        "format": "png",
        "type": "person"
    }

    response = requests.post(
        "https://api.remove.bg/v1.0/removebg", data=payload, headers=headers, files=files)

    return response.content
