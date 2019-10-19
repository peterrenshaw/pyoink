
                         _       __  
      ____  __  ______  (_)___  / /__
     / __ \/ / / / __ \/ / __ \/ //_/
    / /_/ / /_/ / /_/ / / / / / ,<   
   / .___/\__, /\____/_/_/ /_/_/|_|  
  /_/    /____/  
                    


#### pyoink

2019OCT19
* improvements to reporting stream
* failed
- re-installed, failed
- reset old code, compiled... works


2018DEC11
* usage CLI options

```
 opt	description
 ====================================
 -u	grab a youtube URL at -u URL
 -t	save the TITLE as string supplied
 -l	log the results

 ./py.py -u https://www.youtube.com/watch?v=RANDOM_ID 
         -t "title of video"                          
         -l                                            
```

2018DEC10
* added logging capability using -l (log) option

* here is the log, as you see I need to filter for itag.

```
{
    "datetime": 1544421982.0,
    "filepath": "./pyoink.json",
    "itag": "18",
    "options": [
        "<Stream: itag=\"22\" mime_type=\"video/mp4\" res=\"720p\" fps=\"30fps\" vcodec=\"avc1.64001F\" acodec=\"mp4a.40.2\">",
        "<Stream: itag=\"43\" mime_type=\"video/webm\" res=\"360p\" fps=\"30fps\" vcodec=\"vp8.0\" acodec=\"vorbis\">",
        "<Stream: itag=\"18\" mime_type=\"video/mp4\" res=\"360p\" fps=\"30fps\" vcodec=\"avc1.42001E\" acodec=\"mp4a.40.2\">",
        "<Stream: itag=\"36\" mime_type=\"video/3gpp\" res=\"240p\" fps=\"30fps\" vcodec=\"mp4v.20.3\" acodec=\"mp4a.40.2\">",
        "<Stream: itag=\"17\" mime_type=\"video/3gpp\" res=\"144p\" fps=\"30fps\" vcodec=\"mp4v.20.3\" acodec=\"mp4a.40.2\">",
        "<Stream: itag=\"137\" mime_type=\"video/mp4\" res=\"1080p\" fps=\"30fps\" vcodec=\"avc1.640028\">",
        "<Stream: itag=\"248\" mime_type=\"video/webm\" res=\"1080p\" fps=\"30fps\" vcodec=\"vp9\">",
        "<Stream: itag=\"136\" mime_type=\"video/mp4\" res=\"720p\" fps=\"30fps\" vcodec=\"avc1.4d401f\">",
        "<Stream: itag=\"247\" mime_type=\"video/webm\" res=\"720p\" fps=\"30fps\" vcodec=\"vp9\">",
        "<Stream: itag=\"135\" mime_type=\"video/mp4\" res=\"480p\" fps=\"30fps\" vcodec=\"avc1.4d401e\">",
        "<Stream: itag=\"244\" mime_type=\"video/webm\" res=\"480p\" fps=\"30fps\" vcodec=\"vp9\">",
        "<Stream: itag=\"134\" mime_type=\"video/mp4\" res=\"360p\" fps=\"30fps\" vcodec=\"avc1.4d401e\">",
        "<Stream: itag=\"243\" mime_type=\"video/webm\" res=\"360p\" fps=\"30fps\" vcodec=\"vp9\">",
        "<Stream: itag=\"133\" mime_type=\"video/mp4\" res=\"240p\" fps=\"30fps\" vcodec=\"avc1.4d4015\">",
        "<Stream: itag=\"242\" mime_type=\"video/webm\" res=\"240p\" fps=\"30fps\" vcodec=\"vp9\">",
        "<Stream: itag=\"160\" mime_type=\"video/mp4\" res=\"144p\" fps=\"30fps\" vcodec=\"avc1.4d400c\">",
        "<Stream: itag=\"278\" mime_type=\"video/webm\" res=\"144p\" fps=\"30fps\" vcodec=\"vp9\">",
        "<Stream: itag=\"140\" mime_type=\"audio/mp4\" abr=\"128kbps\" acodec=\"mp4a.40.2\">",
        "<Stream: itag=\"171\" mime_type=\"audio/webm\" abr=\"128kbps\" acodec=\"vorbis\">"
    ],
    "title": "compuphile quick sort",
    "url": "https://www.youtube.com/watch?v=XE4VP_8Y0BU"
}
```

* git pull, okay. why?


2018DEC03
* broke again

```
  File "./py.py", line 57, in main
    youtube = YouTube(url)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pytube-9.3.4-py3.5.egg/pytube/__main__.py", line 88, in __init__
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pytube-9.3.4-py3.5.egg/pytube/__main__.py", line 97, in prefetch_init
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pytube-9.3.4-py3.5.egg/pytube/__main__.py", line 133, in init
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pytube-9.3.4-py3.5.egg/pytube/mixins.py", line 49, in apply_signature
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pytube-9.3.4-py3.5.egg/pytube/cipher.py", line 250, in get_signature
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pytube-9.3.4-py3.5.egg/pytube/cipher.py", line 69, in get_transform_plan
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pytube-9.3.4-py3.5.egg/pytube/cipher.py", line 45, in get_initial_function_name
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pytube-9.3.4-py3.5.egg/pytube/helpers.py", line 41, in regex_search
pytube.exceptions.RegexMatchError: regex pattern (yt\.akamaized\.net/\)\s*\|\|\s*.*?\s*c\s*&&\s*d\.set\([^,]+\s*,\s*(?P<sig>[a-zA-Z0-9$]+)\() had zero matches
```

2018NOV20
* fixed as per this comment <https://github.com/nficano/pytube/issues/333#issuecomment-436479121>
2018NOV07
* Oh-no: broken, posted problem at <https://github.com/nficano/pytube/issues/333#issuecomment-436479121>

2018OCT11
* broke, updated pytube and really broke.
- quickly hacked up another CLI to use.


2016OCT22 and earlier

* A 2hr hack to pull down youtube videos using pytube

    <https://github.com/nficano/pytube>
