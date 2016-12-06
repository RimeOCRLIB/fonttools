#! /usr/bin/env python

#generate font namelist for use in FontForge


from __future__ import print_function, division, absolute_import
from fontTools.misc.py23 import *
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables import _c_m_a_p


def writeText(text,path):
    with open(path, "w") as text_file:
        text_file.write(unicode(text))

def main():
    font=TTFont("C:\path\yourFont.ttf")
    cmapTable = font["cmap"]
    cmap=cmapTable.getcmap(0,3)
    text=""
    for code  in cmap.cmap:
        #print (hex(code)+" "+cmap.cmap[code])
        text+=hex(code)+" "+cmap.cmap[code]+"\n"
        
    path="C:\path\yourFont.nam"
    writeText(text,path)
    print ("done")

if __name__ == "__main__":
    main()
