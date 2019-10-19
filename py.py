#!/usr/bin/env python3
# ~*~ encoding: utf-8 ~*~


#=====                    
#     ____      __  __      _       __  
#    / __ \__  _\ \/ /___  (_)___  / /__
#   / /_/ / / / /\  / __ \/ / __ \/ //_/
#  / ____/ /_/ / / / /_/ / / / / / ,<   
# /_/    \__, / /_/\____/_/_/ /_/_/|_|  
#       /____/                          
#                    
# name: py.py
# date: 2019OCT16
#       2018NOV07
#       2018OCT11
#       2016OCT21
# prog: pr
# srcs: <https://github.com/nficano/pytube>
# desc: command line downloader for youtube
#       updated the API in 2018, so this needs to be re-written
#       to work with the new API.
#
# usge: ./py.py -u https://www.youtube.com/watch?v=RANDOM_ID URL
#               -t "title of video"                          TITLE
#               -l                                           LOG 
#=====


import os
import sys
import time
from datetime import datetime
from optparse import OptionParser


from tools import save
from tools import py2json
from tools import str2json
from tools import build_fn
from tools import build_fpn
from tools import build_ext


from pytube import YouTube
from pprint import pprint


VERSION = "0.2.3"
PROG_NAME = "PYOINK"
DESTINATION = "/Users/pr/Music"
ITAG_VID_TYPE_LO = "18"            # this gives .mp4,360
ITAG_VID_TYPE_HI = "22"            # this gives .mp4,720
ITAG_VID_TYPE = ITAG_VID_TYPE_LO   # default to LO


#======
# main: cli entry point
#======
def main():
    usage = "usage %prog -u -t"
    parser = OptionParser(usage)
    parser.add_option("-u", "--url", dest="url", help="url to download")
    parser.add_option("-t", "--title", dest="title", help="title of file")
    parser.add_option("-v", "--video", dest="video", help="display video details")
    parser.add_option("-i", "--itag", dest="itag", help="set itag video display option")
    parser.add_option("-l", "--log",  dest="log", action="store_true", help="log the results to file")
    options, args = parser.parse_args()


    if options.url:
        url = options.url 
        if options.title:
            print("")
            print("{} v{} Starting...".format(PROG_NAME, VERSION))
            print("* url: <{}> ({})".format(url, len(url)))
            print("* title <'{}'>".format(options.title))


            title = options.title.strip()
            title = title.lower()           # lowercase 
            title = title.replace("-","")   # remove existing dash
            title = title.replace(" ","-")  # replace space with dash
            print("* dest <{}>/<{}>".format(DESTINATION, title))


            youtube = YouTube(url)

            # video itag option(s) to show
            if options.video: 
                print("* show video options")
                for option in youtube.streams.all():
                    print("<{}>".format(option))
                sys.exit(0)


            # set video itag option to download
            if options.itag:
                itag = options.itag
            else:
                itag = ITAG_VID_TYPE
            print("* video/sound ITAG option: <{}>".format(itag))

           
            # set for specified video and sound 
            stream = youtube.streams.get_by_itag(itag)


            # -------- start download --------
            print("* stream")
            print("- abr\t\t\t({})".format(stream.abr))
            print("- audio codec\t\t({})".format(stream.audio_codec))
            #if stream.default_filename: print("\t- default filename\t\t\t({})".format(stream.default_filename))
            print("- filesize\t\t({})".format(stream.filesize))
            print("- fps\t\t\t({})".format(stream.fps))
            print("- quality\t\t({})".format(stream.quality))
            print("- res\t\t\t({})".format(stream.res))
            print("- resolution\t\t({})".format(stream.resolution))
            print("- s\t\t\t({})".format(stream.s))
            print("- sp\t\t\t({})".format(stream.sp))
            print("- type\t\t\t({})".format(stream.type))
            print("- url\t\t\t<{}>".format(stream.url))
            print("- video codec\t\t\t({})".format(stream.video_codec))
            try:
                stream.download(output_path=DESTINATION, filename=title)
                sys.stdout.write("* ok\n")
            except KeyboardInterrupt:
                sys.exit(1)
            # -------- end download --------


            print("* url:\t\t{}\n* title:\t{}\n* filepath:\t{}".format(url, options.title.lower(), os.path.join(DESTINATION, title.strip())))

            # log details to file
            if options.log:

                # build option log data
                # extract stream by the itag
                # find explicit details of stream 
                # src: <https://python-pytube.readthedocs.io/en/latest/_modules/pytube/streams.html#Stream>
                opts = {}
                opts['filesize']=youtube.streams.get_by_itag(itag).filesize
                opts['quality']=youtube.streams.get_by_itag(itag).quality
                opts['resolution']=youtube.streams.get_by_itag(itag).resolution
                opts['includes_video_track']=youtube.streams.get_by_itag(itag).includes_video_track
                opts['subtype']=youtube.streams.get_by_itag(itag).subtype

                # file directory and filename
                fn = build_fn(PROG_NAME.lower())
                fpn = build_fpn(os.curdir, fn)

                # create data, jsonify, pretty
                t = datetime.now()
                dt = time.mktime(t.timetuple())
                data = {'url': url,
                        'filepath': fpn,
                        'title': options.title, 
                        'itag': itag, 
                        'options': opts, 
                        'datetime': dt}
                jd = py2json(data, is_pretty=True)                

                # save to file
                save(fpn, jd)
                print("* logging to file <{}>".format(fpn))


            youtube = None
            sys.exit(0)
        else:
            print("Error: you must supply a suitable TITLE")
            sys.exit(1)
    else:
        print("Error: you must supply a valid URL")
        sys.exit(1)


if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
