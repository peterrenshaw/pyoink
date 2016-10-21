#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~


#=====
# name: pyd.py
# date: 2016OCT21
# prog: pr
# desc: youtube python downloader
#=====


from pytube import YouTube
from pprint import pprint

y = YouTube("https://www.youtube.com/watch?v=HmbBL0a_pgI")
pprint(y.get_videos())
print(y.filename)
y.set_filename('mcneil-white-rose')
pprint(y.filter('mp4', '360p'))

video = y.get('mp4','360p')
video.download('/Users/pr/Music')


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
