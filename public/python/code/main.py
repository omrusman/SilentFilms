from trimming import videotrimming
from facedetector import*
from facealign import*
from frames_to_video import*
from mouthroi import*

videotrimming(input="makeup.mp4")
facedetector(invideo="./trim/5.mp4")
facealign()
cropivideo(dir_path="facealign")
mouthroi()
cropivideo(dir_path="mouth_roi")
