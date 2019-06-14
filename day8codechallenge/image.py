#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 18:39:24 2019

@author: vikram
"""

"""
Code Challenge:
    
http://forsk.in/images/Forsk_logo_bw.png"

Download the image from the url above and store in your workking diretory with the same
name as the image name.

Do not hardcode the name of the image

"""

from os.path import basename
import urllib.request
url =  "http://forsk.in/images/Forsk_logo_bw.png"
urllib.request.urlretrieve(url, "Forsk_logo.png")


