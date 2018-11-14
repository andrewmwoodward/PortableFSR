# Portable Force Sensor Stimulator
A portable device utilizing an Arduino Nano and Raspberry Pi Zero to record force sensor data from inside the sole of a shoe.
This data will then be analyzed to determine whether the user is losing balance or not centering their balance and the device
will provide cutaneous stimulation to correct the positioning. 

## Current Progress
The device can now collect FSR data through the analog inputs of the Arduino and communicate to a Raspberry Pi Zero where the data is stored into txt
files. Each file is a one minute collection period. This data will be used as testing data to help determine when the stimulus should be sent. The next step is
to collect this data and work on the analysis method that should be utilized. 
