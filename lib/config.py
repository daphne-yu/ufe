#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# UNATTENDED FFMPEG ENCODER
# https://github.com/supermasita/ufe
# 

# Core root
core_root = "/var/www/html/ufe/"
# Absolute path to folder where original videos are copied
original = "/var/www/html/ufe/video_original/"
# Absolute path to folder where encoded videos are created
encoded = "/var/www/html/ufe/video_encoded/"
# Absolute path to temporal folder (no trailing slash)
tmppath = "/var/tmp"

# Tolerance from last access to a video in video_origin
# Used by "ufe-add" to determine if video can be added for encoding
timedif_to = 10

# This host's name in db table "servers"
server_name = "encoder01"

# DB credentials
db_host = "localhost"
db_user = "root"
db_pass = ""
db_database = "ufe"

# Absolute name of binaries
ffmpeg_bin = "/usr/bin/ffmpeg"

# Create JSON? (True or False)
create_video_json = True

# Dimensions for thumbnail created by create_thumbnail function
# (pixels, integer)
thumbnail_width = 600 
thumbnail_height = 338
