# Walk Maps

## How to run

1. Compile darknet code that is provided, for your platform by running `cd darknet; make -j4` 
2. Download yolov3  weights
3. Run `python3.7 process.py` to generate all the points in points.nzp format of all persons in the video at 5fps.  
4. Run `python3.7 heatmap.py` to generate the heatmap.
4. Run `python3.7 getbg.py` to get the background from the video.  
5. Run `python3.7 merge.py` to overlay the heat map onto the background image. 