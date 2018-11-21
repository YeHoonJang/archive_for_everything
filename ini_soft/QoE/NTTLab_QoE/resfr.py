#!/usr/bin/python
######### Last updated: May. 29 2018 #########
#res-fr.py

import sys

def resfr(vBR):
  
  if vBR >= 11000000:
    res = 2160
    fr = 30
  elif vBR >= 7000000:
    res = 1080
    fr = 30
  elif vBR >= 3500000:
    res = 720
    fr = 30
  elif vBR >= 2400000:
    res = 576
    fr = 30
  elif vBR >= 1400000:
    res = 432
    fr = 30
  elif vBR >= 900000:
    res = 360
    fr = 30
  else:
    res = 144
    fr = 15
 
  #print vBR, res, fr

  return (res, fr)

