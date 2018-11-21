1. command line
./qoeCalc.py -c (json folder path)
  arguments.py
  - determine args.
  coefficients.py
  - determine coefficients (based on codec in the future).
  resfr.py
  - determin resolution and framerate based on bitrate.

Note 1: 
The code generates O21, O22, and O46 csvs in out folder.  
If a csv exists in out folder, code removes the csv and then generates the csv.  

Note 2:
The code cannot take into account user manupulations such as seek becasue log does not contain manupulations.
When a chunk with the same index was re-sent, the code ignores chunks with earlier timestamp.
Therefore, even when user actually changes a viewing position with seek bar, the code ignores.

Note 3:
The code cannot estimate quality based on the actual viewing position.
In addition, buffering timing of viewing position is not taken into account, i.e., buffering timing is generated when buffer is empty..

1.1. output files
The code generates four csvs:
(input file name)_ O21.csv
(input file name)_ O22.csv
(input file name)_ O46.csv
(input file name)_ buff.csv

1.2.1 O21.csv
numofChunk,chunkNo,index,startTime,aBR,duration,second,O21

1.2.2 O22.csv
numofChunk,chunkNo,index,startTime,vBR,vRS,vFR,duration,second,O22

1.2.3 O46.csv
O21Len,O22Len,duration,missing,numofBuff,totalBuffLen,avgBuffInt,O35,O46

1.2.4 buff.csv
currentTime,duration

