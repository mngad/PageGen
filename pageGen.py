#!/usr/bin/python3

import os
from shutil import copyfile
import csv
cwd = os.getcwd()
url = 'http://fraun.ddns.net'
dirName = os.path.dirname(cwd)
print(dirName)
#template for the python files
template = """<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width" />
	<link rel="icon" type="image/png" href="/favicon.png" />
	<link rel="stylesheet" type="text/css" href="style.css" />
	<title>START</title>
</head>
<body>
	<div id="content">

		<ul id="index">
                    {links}
		</ul>

	</div>
</body>
</html>
"""
def getLinks(direc, link, lstOfFiles):
    print(direc)
    for filename in lstOfFiles:
        if os.path.isdir(direc + '/' + filename):
            link = link + '<a href="'+ url  +  direc[len(dirName):] + '/' + filename + '">' + filename + '</a><br>' + '\n'

        else:
            continue
    for filename in lstOfFiles: #cycle through files in cwd
        if os.path.isfile(direc + '/' + filename):
            if '.css' in filename:
                continue
            if '.py' in filename:
                continue
            link = link + '<a href="'+ url + direc[len(dirName):] + '/' + filename + '">' + filename + '</a><br>' + '\n'
        else:
            continue
    return link

dirList = []
for root, subdirs, files in os.walk(cwd):
    dirList.append(root)

for direc in dirList:
    link = ''
    lst = os.listdir(direc)
    link = getLinks(direc, link, lst)
    context = {                 #context for the tmplate - bits to change - filname etc.
        "links":link
    }
    indexFile = open(direc + '/index.html', 'w')
    indexFile.write(template.format(**context))
    indexFile.close()
    if os.path.isfile(direc + '/style.css'):
        continue
    else:
        copyfile(cwd + '/style.css', direc + '/style.css')
