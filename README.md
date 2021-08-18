
# Boardroom One Hackathon Submission

This repo contains a Python microservice responsible for generating user profile photos on the Boardroom One platform.


## Demo

Live Demo (Frontend + Backend) - <https://boardroomone-python.herokuapp.com>

## Tech Stack

**Client:** HTML, CSS, JavaScript, Bootstrap

**Server:** Python, Flask

**Services:** Cloudinary, Remove.bg


## API Reference

#### Create Profile Photo

```http
POST /profile/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `profilePhoto` | `file` | **Required**. Profile photo to transform |

Accepts an image uploaded via HTTP and returns a headshot-extracted, black background version of the picture.


## Run Locally

Clone the project

```bash
git clone https://github.com/LordGhostX/boardroomone-hackathon
```

Go to the project directory

```bash
cd boardroomone-hackathon
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start the Server

```bash
python server.py
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file.

`CLOUDINARY_CLOUD_NAME`

`CLOUDINARY_API_KEY`

`CLOUDINARY_API_SECRET`

`REMOVE_BG_API_KEY`


## Optimizations

* Outsourcing the tasks of facial landmark detection, image processing, and background removal processes to external services, reducing the overall load the API bears.

## FAQ

#### How does it work?

* When the API receives the image from the user, it sends a request to remove.bg API to separate the user image from the background.
* Then, it uses Cloudinary `Advanced Facial Attributes Detection` addon and some mathematical tricks to intelligently extract the headshot of the user from the given image.
* After this, some post-processing, like changing the background color, is done to get the desired result.


## Authors

- [@LordGhostX](https://www.github.com/@LordGhostX)
