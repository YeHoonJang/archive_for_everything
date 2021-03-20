#!/usr/local/bin/python
######### Last updated: May. 29 2018 #########
#qoeCalc.py

######### Module declaration #########
import sys, getopt, os, random, time
import json
import shutil
import numpy as np
import multiprocessing as mp
import glob
from subprocess import Popen
import yaml
import re
import math
import time
import csv
import pytz
import datetime
from datetime import datetime
from datetime import timedelta
######### Module declaration end #########

######### Read pythons #########
from arguments import *
from coefficients import *
from resfr import *
################################

######### main #########
if __name__ == "__main__":
  ######### Arguments declaration #########
  argvs = sys.argv
  argc = len(argvs)

  #print argc
  jsonPath ="jsonPath"
  jsonPath = arguments(argvs, argc, jsonPath)
  #print jsonPath

  file_name = "./out/" 
  if not os.path.exists("./out/"):
    os.mkdir("./out/")
  ######### Arguments declaration #########

  ######### Obtain all JSON #########
  files = []
  if jsonPath != "folder":
    for filepath in glob.glob(jsonPath + '/' + '*'):
      files.append(filepath)
      #print filepath
  ######### Obtain all JSON #########
  
  ### Coefficients ###
  a1,a2,a3,v1,v2,v3,v4,v5,v6,v7,av1,av2,av3,av4,t1,t2,t3,t4,t5,s1,s2,s3 = coefficients()
  ### Coefficients ###

  for n in range(0, len(files)):
    ### Read JSON ###
    print n, files[n],
    base = os.path.basename(files[n])
    with open(files[n], 'r') as f:
      text = f.read().strip()
    dec = json.JSONDecoder()
    jsons = []
    while len(text) > 0:
      js, size = dec.raw_decode(text)
      jsons.append(js)
      text = text[size+1:].lstrip()
    ### Read JSON ###

    ### array ###
    aIndex = []
    aTime = []
    aBR = []
    aDur = []
    O21 = []
    vIndex = []
    vTime = []
    vBR = []
    vDur = []
    vRS = []
    vFR = []
    O22 = []
    bTime = []
    bDur = []
    ### array ###

    ### Parse parameters per key ###
    for h1 in jsons:
      if 'tracks' in h1['qoe']:
        for h2 in h1['qoe']['tracks']:
          if h2['type'] == 'audio':
            aID = h2['id']
          elif h2['type'] == 'video':
            vID = h2['id']
          else:
            oID = h2['id']
          #print h2['id'], h2['type']

      if 'startupTime' in h1['qoe']:
        bTime.append(h1['qoe']['timestamp'])
        bDur.append(h1['qoe']['startupTime'])
        contentLength = h1['qoe']['duration']

      if 'fragments' in h1['qoe']:
        for h3 in h1['qoe']['fragments']:
          if h3['trackId'] == aID:
            for j in range(1, len(aTime)-1):
              if aTime[len(aTime)-1] >= h3['startTime']:
                aIndex.pop()
                aTime.pop()
                aBR.pop()
                aDur.pop()
              else:
                break
            aIndex.append(h3['index'])
            aTime.append(h3['startTime'])
            aBR.append(h3['bitrate'])
            aDur.append(h3['duration'])
            #print 'audio', len(aTime), aTime[len(aTime)-1], aBR[len(aBR)-1], aDur[len(aDur)-1]

          elif h3['trackId'] == vID:
            for j in range(1, len(vTime)-1):
              if vTime[len(vTime)-1] >= h3['startTime']:
                #print 'XXX', j, vTime[len(vTime)-1], h3['startTime'],
                vIndex.pop()
                vTime.pop()
                vBR.pop()
                vRS.pop()
                vFR.pop()
                vDur.pop()
                #print len(vTime)
              else:
                break
            vIndex.append(h3['index'])
            vTime.append(h3['startTime'])
            vBR.append(h3['bitrate'])
            vDur.append(h3['duration'])
            res, fr = resfr(h3['bitrate']) 
            vRS.append(res)
            vFR.append(fr)
            #print 'video', len(vTime),vTime[len(vTime)-1], vBR[len(vBR)-1], vDur[len(vDur)-1]
          ### ????? ###
          else:
            for h3 in h2['fragments']:
              print 'xxx', h3['bitrate'], h3['startTime'], h3['duration']
      if 'bufferings' in h1['qoe']:
        #print "bufferings"
        for h5 in h1['qoe']['bufferings']:
          bTime.append(h5['currentTime'])
          bDur.append(h5['duration'])
          #print h5['currentTime'], h5['duration']

    ### print buff ###
    if ".json" in base:
      buffPath = "./out/" + base.replace('.json', '_buff.csv')
    else:
      buffPath = "./out/" + base + '_buff.csv'
    if os.path.exists(buffPath):
      os.remove(buffPath)
    for b in range(0, len(bTime)):
      list = []
      z = open(buffPath, "a")
      list.append(bTime[b])
      list.append(float(bDur[b]/ 1000.))
      F = csv.writer(z)
      F.writerow(list)
      z.close()
    ### print buff ###
    ### Parse parameters per key ###

    if len(aTime) == 0 or len(vTime) == 0:
      print ""
      continue

    ### O21 and O22 calc and debug log ###
    for a in range(0, len(aTime)):
      #print 'audio', a, aTime[a], aBR[a], aDur[a]
      for at in range(int(aTime[a] / 1000), int((aTime[a] + aDur[a] + 1.00000000001) / 1000)):
        O21.append((a1 + (1. - a1) / (1. + (float(aBR[a] / 1000.)/ a2) ** a3)))
        #print 'audio', a, aTime[a], aBR[a], aDur[a], at, O21[len(O21)-1]
        
        ### print O21 ###
        if ".json" in base:
          O21Path = "./out/" + base.replace('.json', '_O21.csv')
        else:
          O21Path = "./out/" + base + '_O21.csv'
        if at == int(aTime[0] / 1000) and os.path.exists(O21Path):
          os.remove(O21Path)
        list = []
        z = open(O21Path, "a")
        list.append(len(aTime))
        list.append(a)
        list.append(aIndex[a])
        list.append(aTime[a])
        list.append(aBR[a])
        list.append(aDur[a])
        list.append(at)
        list.append(O21[len(O21)-1])
        F = csv.writer(z)
        F.writerow(list)
        z.close()
        ### print O21 ###

    for v in range(0, len(vTime)):
      #print 'video', v, vTime[v], vBR[v], vDur[v]
      '''
      if vTime[v] != (vTime[v - 1] + vDur[v - 1]):
        #for vt in range(int((vTime[v-1] + vDur[v-1] + 1) / 1000.), int(vTime[v] / 1000.)):
        for vt in range(int((vTime[v-1] + vDur[v-1]) / 1000.), int(vTime[v] / 1000.)):
          O22.append(0)
          #print 'video', len(vTime), v, vTime[v], vBR[v], vDur[v], vt, O22[len(O22)-1]
      #for vt in range(int(vTime[v] / 1000), int((vTime[v] + vDur[v] + 1) / 1000)):
      '''
      for vt in range(int((vTime[v] + 1) / 1000), int((vTime[v] + vDur[v] + 1) / 1000)):
        RS = vRS[v] * vRS[v] * 16 / 9
        FR = vFR[v]
        X = 1. + 4. * (1. - math.exp(- v3 * FR)) * RS / (v2 + RS)
        Y = (v4 * RS + v6 * math.log10(v7 * FR + 1.)) / (1. - math.exp(-v5 * RS)) 
        O22.append((X + (1. - X) / (1. + (float(vBR[v] / 1000.) / Y) ** v1)))
        #print 'video', len(vTime), v, vIndex[v], vTime[v], vBR[v], vRS[v], vFR[v], vDur[v], vt, O22[len(O22)-1]

        ### print O22 ###
        if ".json" in base:
          O22Path = "./out/" + base.replace('.json', '_O22.csv')
        else:
          O22Path = "./out/" + base + '_O22.csv'
        if vt == int(vTime[0] / 1000) and os.path.exists(O22Path):
          os.remove(O22Path)
        list = []
        z = open(O22Path, "a")
        list.append(len(vTime))
        list.append(v)
        list.append(vIndex[v])
        list.append(vTime[v])
        list.append(vBR[v])
        list.append(vRS[v])
        list.append(vFR[v])
        list.append(vDur[v])
        list.append(vt)
        list.append(O22[len(O22)-1])
        F = csv.writer(z)
        F.writerow(list)
        z.close()
        ### print O22 ###
    ### O21 and O22 calc and debug log ###

    ### lost info ###
    missingO21 = O21.count(0)
    missingO22 = O22.count(0)
    ### lost info ###

    ### O34 and O35 calc ###
    ### duration ###
    if len(O21) > len(O22):
      duration = len(O22)
      missing = missingO22
    else:
      duration = len(O21)
      missing = missingO21
    ### duration ###
    
    O35_num = O35_den = 0
    lostseconds = 0

    for av in range(0, duration):
      if O21[av] > 0 and O22[av] > 0:
        tO34 = av1 + av2 * O21[av] + av3 * O22[av] + av4 * O21[av] * O22[av]
        u = float(1 + av - lostseconds) / float(duration - missing)
        w1 = t1 + t2 * math.exp(u / t3)
        w2 = t4 - t5 * tO34
        #print av, u, O21[av], O22[av], tO34, w1, w2
        O35_num += (w1 * w2 * tO34)
        O35_den += (w1 * w2)
        #print O21[av], O22[av], tO34, w1, w2, u
      else:
        lostseconds = missing
    O35 = O35_num / O35_den
    #print O35, len(O21), len(O22), duration, missing,
    ### O34 and O35 calc ###
  
    ### O46 calc ###
    totalBuffLen = numofBuff = avgBuffInt = 0
    #numofBuff = len(bDur)
    for b in range(0, len(bDur)):
      numofBuff += 1
      totalBuffLen += bDur[b]
      if len(bDur) > 1 and b > 0:
        avgBuffInt += (bTime[b] - bTime[b-1])

        # stalling in short interval, i.e., 1 second, is not counted.
        if (bTime[b] - bTime[b-1]) <= 1:
          numofBuff -= 1
          avgBuffInt -= (bTime[b] - bTime[b-1])
        #print avgBuffInt, bTime[b], bTime[b-1]
    if numofBuff > 1:
      avgBuffInt /= float(numofBuff - 1)
    
    S1 = math.exp(- float(numofBuff) / s1) 
    S2 = math.exp(- ((float(totalBuffLen) / 1000.) / float(duration)) / s2) 
    S3 = math.exp(- float(avgBuffInt / duration) / s3)
    S = S1 * S2 * S3
    O46 = 1. + (O35 - 1.) * S
    print contentLength, len(O21), len(O22), duration, missing, numofBuff, totalBuffLen, avgBuffInt, O35, O46, S1, S2, S3, S
    
    ### print O35/O46 ###
    if ".json" in base:
      O46Path = "./out/" + base.replace('.json', '_O46.csv')
    else:
      O46Path = "./out/" + base + '_O46.csv'
    if os.path.exists(O46Path):
      os.remove(O46Path)
    list = []
    z = open(O46Path, "a")
    list.append(contentLength)
    list.append(len(O21))
    list.append(len(O22))
    list.append(duration)
    list.append(missing)
    list.append(numofBuff)
    list.append(totalBuffLen)
    list.append(avgBuffInt)
    list.append(O35)
    list.append(O46)
    F = csv.writer(z)
    F.writerow(list)
    z.close()
    ### print O35/O46 ###

    ### O46 calc ###

          
