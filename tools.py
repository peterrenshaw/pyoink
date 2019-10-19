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
# name: tools.py
# date: 2018NOV07
# prog: pr
# desc: useful tools to work with
#       
# uses: ast <https://docs.python.org/3.5/library/ast.html>
#========


import os
import sys
import json
import datetime
from ast import literal_eval
from optparse import OptionParser


#--------
# description: file tools
#--------
def str2py(data):
    """
    ==== WARNING: DANGEROUS ==== 
    convert unfiltered input string from CLI to python executable code
    documentation suggests otherwise, does this work against malicious users?
    <https://docs.python.org/3/library/ast.html?highlight=ast#ast.literal_eval>
    ==== WARNING: DANGEROUS ==== 
    """
    if data:
        try: 
            pd = literal_eval(data)
        except SyntaxError as err:
            sys.stderr.write("Syntax Error: str2py data supplied not converted using str2py.\nError is <{}>\n".format(err))
            sys.stderr.write("Warning: <{}>\n".format(data))
            sys.stderr.write("Suggestion: error in string supplied needs to be corrected and valid.\n")
            sys.exit(1)
        else:
            pass
        return pd
    else:
        return None
def py2json(data, is_pretty=False):
    """convert py structure to json"""
    if is_pretty:
        jd  = json.dumps(data, 
                         ensure_ascii=True, 
                         indent=4,
                         sort_keys=True)
    else:
       jd = json.dumps(data)
    return jd

def str2json(data, is_pretty=True):
    """given string data, convert to JSON with options"""
    # we want python structure not string
    d = str2py(data)
    if not d:
        sys.stderr.write("Error: str2json data supplied not converted using str2py.\n")
        sys.exit(1)
    else:
        if is_pretty:
           jd  = py2json(d, is_pretty=True)
        else:
           jd = py2json(d, is_pretty=False)

        return jd
def build_ext(ext, default="txt"):
    """build 3 letter ext without dots"""
    if len(ext) == 3: return ext.lower()
    else: return default.lower()
def build_fn(filename, ext="json", default_fn="stupid_forgot_filename"):
    """given a filename (assume valid), create a filename with extension"""
    if not filename:
        filename = default_fn
    return "{}.{}".format(filename, ext)    
def build_fpn(fp, fn):
    """
    given a filepath (will test valid) and a filename (assume valid), 
    build valid directory file path name
    """
    if fp:
        if os.path.isdir(fp):
            fpn = os.path.join(fp, fn)
        else:
            sys.stderr.write("Error: please supply a valid directory file path.\n\t<{}>".format(fp))
            sys.exit(1)
    else:
        fpn = fn
    return fpn
def save(fpn, data, option_save='a'):
    """given valid filepathname and data, save to file"""
    if fpn: # assume valid, pre-tested
        with open(fpn, option_save) as f:
            f.write(data)
        f.close()
        return True
    else:
        sys.stderr.write("Error: please supply a filename path.")
        sys.exit(1)
#-------- File tools --------


#======
# main: cli entry point
#======
def main():
    sys.exit(0)

if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab

