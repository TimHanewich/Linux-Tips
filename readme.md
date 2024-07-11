# Capturing Images through a USB Webcam on a Linux Distro
This is just a simple tutorial.

## Update/Upgrade
```
sudo apt-get update
sudo apt-get upgrade
```

## List USB devices
```
lsusb
```

Example output:
```
Bus 001 Device 002: ID 046d:0825 Logitech, Inc. Webcam C270
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

You can see my webcam listed above.

## Capturing Images
We will use [fswebcam](https://github.com/fsphil/fswebcam), a lightweight utility for capturing images.

To install fswebcam:
```
sudo apt-get install fswebcam
```

To capture an image and store it in the current directory, as the name "image.jpg":
```
fswebcam image.jpg
```

### No Banner
To capure an image without the "banner" at the bottom that contains the time stamp, simply pass `--no-banner` into the command:

```
fswebcam --no-banner image.jpg
```

### Resolutions
To specify a resolution to capture in, use the `-r` option:
```
fswebcam -r 640x480 image.jpg
```

As a side note, the resolutions I've determined my [Logitech C270 webcam](https://www.logitech.com/assets/31702/2/c270620-002802003403gsamr.pdf) can capture in:
- 160x120
- 352x288 (default)

## Uploading Images
Obviously, you can't view the image from the command line/SSH. A simple way to "upload" this I've found is to use [curl](https://www.geeksforgeeks.org/curl-command-in-linux-with-examples/) to make a POST request to an endpoint with the image as the body.

[webhook.site](https://webhook.site/) is a great online utility that lets you open up a unique endpoint that you can call to from anywhere in the world, and then see those HTTP requests come in. Navigate to the site, get a unique URL, and call to it via a POST request with the body being the image:

```
 curl -X POST https://webhook.site/8c69d025-e960-488a-8c3d-f85ae7d77f30 -H "Content-Type: image/jpeg" --data-binary @image.jpg
```

And now that image should be seen as the body of the latest POST request!

![post](https://i.imgur.com/e7ueYc6.png)

## How to capture images through Python
You can use the `subprocess` module in Python to execute a command line prompt. For example:

```
import subprocess
command = "fswebcam --no-banner -r 160x120 image.jpg"
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print(result.stdout) # print standard output
print(result.stderr) # print standard error
```

`stdout` is for standard output, `stderr` is for standard error. But I noticed, even when the command succeeded, it still sometimes puts it in stderr. Probably good to combine both and evaluate the combination to be safe.