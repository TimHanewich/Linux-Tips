import subprocess
import requests

def capture() -> None:
    """Makes a command line command to capture an image using fswebcam"""
    cmd = "fswebcam --no-banner -r 160x120 img.jpg"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

def upload(path:str = "./img.jpg", url:str = "https://webhook.site/40394d10-c02b-4ff4-b80e-14a09ea7f935") -> None:
    """Uploads a picture via a POST request."""
    f = open(path, "rb")
    files = {"file": ("img.jpg", f, "image/jpeg")}
    response = requests.post(url, files=files)
    if response.status_code != 200:
        print("POST returned status code '" + str(response.status_code) + "'!")


