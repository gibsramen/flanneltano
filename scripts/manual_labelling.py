import glob
import os

import numpy as np
import pandas as pd
from PIL import Image
from PIL.ImageTk import PhotoImage
from tkinter import Tk, Label

root = Tk()
l = Label(root)
l.pack()

jpg_files = glob.glob("../data/album_reviews/*/*.jpg")
num_files = len(jpg_files)

melon_dict = dict()
print("Type 'exit' to stop")

outfile = "../data/manual_labels.tsv"
with open(outfile, "r+") as f:
    data = f.read().splitlines()

albums = set([x.split("\t")[0] for x in data])
missing_albums = set(jpg_files).difference(albums)
n = len(albums)

print(f"----Labelled {n} samples out of {num_files}----")
with open(outfile, "a") as f:
    while missing_albums:
        n += 1
        r = np.random.choice(tuple(missing_albums))
        img = PhotoImage(file=r)
        l.config(image=img)
        label = input(f"{n}/{num_files} Type: ")
        if label == "exit":
            break
        f.write(f"{r}\t{label}\n")
        missing_albums.remove(r)
