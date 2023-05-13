import numpy as np
import pandas as pd

df = pd.read_excel('5Gdata.xlsx')
Num_rows = len(df.iloc[:, 0])
xcoor = []
ycoor = []
blockindexing = []

for i in range(Num_rows):
    x = df.iloc[i,0]
    y = df.iloc[i,1]
    xcoor.append(x)
    ycoor.append(y)

for j in range(Num_rows):
    # row 1
    if   (xcoor[j]>835350 and xcoor[j]<835496 and ycoor[j]>817220 and ycoor[j]<817392):
        block = 1
    elif (xcoor[j]>835496 and xcoor[j]<835642 and ycoor[j]>817220 and ycoor[j]<817392):
        block = 2
    elif (xcoor[j]>835642 and xcoor[j]<835788 and ycoor[j]>817220 and ycoor[j]<817392):
        block = 3
    elif (xcoor[j]>835788 and xcoor[j]<835934 and ycoor[j]>817220 and ycoor[j]<817392):
        block = 4
    elif (xcoor[j]>835934 and xcoor[j]<836080 and ycoor[j]>817220 and ycoor[j]<817392):
        block = 5
    elif (xcoor[j]>836080 and xcoor[j]<836230 and ycoor[j]>817220 and ycoor[j]<817392):
        block = 6

    # row 2
    elif (xcoor[j]>835350 and xcoor[j]<835496 and ycoor[j]>817391 and ycoor[j]<817564):
        block = 7
    elif (xcoor[j]>835496 and xcoor[j]<835642 and ycoor[j]>817391 and ycoor[j]<817564):
        block = 8
    elif (xcoor[j]>835642 and xcoor[j]<835788 and ycoor[j]>817391 and ycoor[j]<817564):
        block = 9
    elif (xcoor[j]>835788 and xcoor[j]<835934 and ycoor[j]>817391 and ycoor[j]<817564):
        block = 10
    elif (xcoor[j]>835934 and xcoor[j]<836080 and ycoor[j]>817391 and ycoor[j]<817564):
        block = 11
    elif (xcoor[j]>836080 and xcoor[j]<836230 and ycoor[j]>817391 and ycoor[j]<817564):
        block = 12

    # row 3
    elif (xcoor[j]>835350 and xcoor[j]<835496 and ycoor[j]>817563 and ycoor[j]<817736):
        block = 13
    elif (xcoor[j]>835496 and xcoor[j]<835642 and ycoor[j]>817563 and ycoor[j]<817736):
        block = 14
    elif (xcoor[j]>835642 and xcoor[j]<835788 and ycoor[j]>817563 and ycoor[j]<817736):
        block = 15
    elif (xcoor[j]>835788 and xcoor[j]<835934 and ycoor[j]>817563 and ycoor[j]<817736):
        block = 16
    elif (xcoor[j]>835934 and xcoor[j]<836080 and ycoor[j]>817563 and ycoor[j]<817736):
        block = 17
    elif (xcoor[j]>836080 and xcoor[j]<836230 and ycoor[j]>817563 and ycoor[j]<817736):
        block = 18

    # row 4
    elif (xcoor[j]>835350 and xcoor[j]<835496 and ycoor[j]>817735 and ycoor[j]<817908):
        block = 19
    elif (xcoor[j]>835496 and xcoor[j]<835642 and ycoor[j]>817735 and ycoor[j]<817908):
        block = 20
    elif (xcoor[j]>835642 and xcoor[j]<835788 and ycoor[j]>817735 and ycoor[j]<817908):
        block = 21
    elif (xcoor[j]>835788 and xcoor[j]<835934 and ycoor[j]>817735 and ycoor[j]<817908):
        block = 22
    elif (xcoor[j]>835934 and xcoor[j]<836080 and ycoor[j]>817735 and ycoor[j]<817908):
        block = 23
    elif (xcoor[j]>836080 and xcoor[j]<836230 and ycoor[j]>817735 and ycoor[j]<817908):
        block = 24

    # row 5
    elif (xcoor[j]>835350 and xcoor[j]<835496 and ycoor[j]>817907 and ycoor[j]<818080):
        block = 25
    elif (xcoor[j]>835496 and xcoor[j]<835642 and ycoor[j]>817907 and ycoor[j]<818080):
        block = 26
    elif (xcoor[j]>835642 and xcoor[j]<835788 and ycoor[j]>817907 and ycoor[j]<818080):
        block = 27
    elif (xcoor[j]>835788 and xcoor[j]<835934 and ycoor[j]>817907 and ycoor[j]<818080):
        block = 28
    elif (xcoor[j]>835934 and xcoor[j]<836080 and ycoor[j]>817907 and ycoor[j]<818080):
        block = 29
    elif (xcoor[j]>836080 and xcoor[j]<836230 and ycoor[j]>817907 and ycoor[j]<818080):
        block = 30

    # row 6
    elif (xcoor[j]>835350 and xcoor[j]<835496 and ycoor[j]>818079 and ycoor[j]<818252):
        block = 31
    elif (xcoor[j]>835496 and xcoor[j]<835642 and ycoor[j]>818079 and ycoor[j]<818252):
        block = 32
    elif (xcoor[j]>835642 and xcoor[j]<835788 and ycoor[j]>818079 and ycoor[j]<818252):
        block = 33
    elif (xcoor[j]>835788 and xcoor[j]<835934 and ycoor[j]>818079 and ycoor[j]<818252):
        block = 34
    elif (xcoor[j]>835934 and xcoor[j]<836080 and ycoor[j]>818079 and ycoor[j]<818252):
        block = 35
    elif (xcoor[j]>836080 and xcoor[j]<836230 and ycoor[j]>818079 and ycoor[j]<818252):
        block = 36

    blockindexing.append(block)

with open("group.txt", 'w') as f:
    for i in blockindexing:
        f.write(str(i)+'\n')