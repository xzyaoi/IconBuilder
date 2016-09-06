#coding:utf-8

import os
import sys
import time
import glob
import click
from PIL import Image

class IconBuilder:
    def __init__(self,picpath):
        self.picpath=picpath
    def pic_walker(self,path):
        target=[]
        for files in glob.glob(path + "/*.png"):
            filepath,filename = os.path.split(files)  # todo: mark
            target.append(filename)
        return target
    def pic_resizer(self,picname,n_w,n_h):
        img=Image.open(picname)
        w,h=img.size
        target=img.resize((int(n_w),int(n_h)),Image.ANTIALIAS)
        return target
    def make_folder(self):
        foldername=self.picpath+'/'+'resized'
        print 'new imgs will be saved to '+foldername
        if not os.path.isdir(foldername):
            os.mkdir(foldername)
        return foldername
    def save_pic(self,target,folder,pixel,name):
        img=target
        target.save(folder+'/'+name+'@'+str(pixel)+'.png')

    def run_auto(self,pixels,name):
        imglist=self.pic_walker(self.picpath)
        self.make_folder()
        for img in imglist:
            imgfile=self.picpath+'/'+img
            for each in pixels:
                self.save_pic(self.pic_resizer(imgfile,each,each),self.picpath+'/resized',each,name)
@click.command()
@click.option('--filename',prompt='Your desired resolutions files',help='Your desired resolutions files')
@click.option('--name',prompt='New Logo files name',help='New Logo Files Name')
def main(filename,name):
    '''A Simple & Useful Tool for Logo Resizer'''
    cwd=os.getcwd()
    print cwd
    ib=IconBuilder(cwd)
    f=open(filename)
    line=f.readline()
    pixels=[]
    while line:
        pixels.append(int(line))
        line=f.readline()
    f.close()
    ib.run_auto(pixels,name)

if __name__ == '__main__':
    sys.exit(int(main() or 0))