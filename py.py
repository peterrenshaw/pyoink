#!/usr/bin/env python3
# ~*~ encoding: utf-8 ~*~


#=====
# name: py.py
# date: 2018OCT11
#       2016OCT21
# prog: pr
# srcs: <https://github.com/nficano/pytube>
# desc: command line downloader for youtube
#       updated the API in 2018, so this needs to be re-written
#       to work with the new API.
#=====


import os
import sys
from optparse import OptionParser


from pytube import YouTube
from pprint import pprint


VERSION = "0.2"
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
                for option in youtub.streams.all():
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
