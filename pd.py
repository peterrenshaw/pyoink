#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~


#+++++++ BROKEN +++++++++
# THIS CODE IS BROKEN
# DO NOT USE 
# LEFT FOR HISTORICAL REASONS
#+++++++ BROKEN +++++++++

#=====
# name: pd.py
# date: 2016OCT21
# prog: pr
# srcs: <https://github.com/nficano/pytube>
# desc: command line downloader for youtube
#=====


from optparse import OptionParser


from pytube import YouTube
from pprint import pprint


DESTINATION = "/Users/pr/Music"



#======
# main: cli entry point
#======
def main():
    usage = "usage %prog -u -t"
    parser = OptionParser(usage)
    parser.add_option("-u", "--url", dest="url", help="url to download")
    parser.add_option("-t", "--title", dest="title", help="title of file")
    options, args = parser.parse_args()


    if options.url: 
        print("url: {}".format(options.url))
 
        if options.title:
            print("title {}".format(options.title))
            title = options.title.replace(" ","-")
            
            youtube = YouTube(options.url)
            youtube.set_filename(title)

            video = youtube.get("mp4","360p")
            video.download(DESTINATION)
 
            print("{}".format(title))


if __name__ == "__main__":
    main()




# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
