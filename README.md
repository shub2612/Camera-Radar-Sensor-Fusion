# Camera-Radar-Sensor-Fusion
This repository was made for a scientific research project in my University. Here an application of fusing camera and Radar sensor data is shown to calculate the distance of an object.
# Radiate dataset >>> https://github.com/marcelsheeny/radiate_sdk
#Data download for dataset >>>> https://www.dropbox.com/sh/f8amohzfxigq8ed/AADMrrNK9jmkfJ02yDsgNg9Za?dl=0
The major backbone of this study is the Radiate dataset which contains extensive recordings of the data captured in various environment and driving conditions. A brief description about this dataset is found in section 2.
The subsequent sections of the report contains how first the objects are detected in the Camera images using pre-trained YoloV3 network and then how this information is used along with the Radar data to calculate the distance to the object detected. Finally an evaluation of the results is made which shows that the algorithm described in this report works with a mean deviation of 0.9m.  
