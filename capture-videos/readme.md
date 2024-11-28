# Capturing Videos with a Webcam on a Linux Device
**ffmpeg** can be used to record a video, like this for example:

Example of starting a video recording, with no time limit (waits for manual disruption)
```
ffmpeg -f v4l2 -video_size 640x480 -i /dev/video0 output.mp4
```


Example of starting a video recording, but with a 30 second time limit (records for 30 seconds and then stops)
```
ffmpeg -f v4l2 -video_size 640x480 -i /dev/video0 -t 00:00:30 output.mp4
```