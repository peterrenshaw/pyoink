#!/usr/bin/env python3
# ~*~ encoding: utf-8 ~*~


#=====
# name: py.py
# date: 2018NOV07
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


VERSION = "0.2.2"
PROG_NAME = "PYOINK"
DESTINATION = "/Users/pr/Music"
ITAG_VID_TYPE = "18"             # this gives .mp4,360


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
            title = title.replace(" ","-")
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
            print("* download <{fs} bytes>".format(fs=stream.filesize,))
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
