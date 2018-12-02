### pyoink

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
