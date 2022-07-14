import os,time,shutil

bookdir = "book/"

def routine():
    pass

with open("subname.txt",'r') as f:
    a = f.read()
    subnames = a.strip().split("\n")
    routine()
