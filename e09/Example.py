import argparse
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import os
from Scraping import Scraping

def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        #Parse geo references.
        Nsec = exif['GPSInfo'][2][2] 
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1 
        else:
            Nmult = -1
        if exif['GPSInfo'][3] == 'E':
            Wmult = 1 
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}
        input()

 
def get_exif_metadata(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_gps_info(ret)
    return ret
    
def printMeta():
    
    ruta = "images"
    os.chdir(ruta)
    os.system("mkdir MetaData")
    
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))
            print ("[+] Metadata for file: %s " %(name))
            file = open("MetaData/"+name+".txt","w")
            
            try:
                exifData = {}
                exif = get_exif_metadata(name)
                for metadata in exif:
                    print ("Metadata: %s - Value: %s " %(metadata, exif[metadata])) 
                    file.write("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                file.write(os.linesep)                
                print ("\n")
            except:
                import sys, traceback
                traceback.print_exc(file=sys.stdout)
            file.close()




if __name__ == "__main__":

    description= """ Ejemplos de uso:
        + Escaneo basico:
            -link https://www.uanl.mx/"""

    parser = argparse.ArgumentParser(description='link scanning', epilog = description, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-link", metavar='LINK', dest="link", help="link to scan", required=True)

    params = parser.parse_args()

    obj_scraping = Scraping()
    obj_scraping.scrapingImages(params.link)
    printMeta()
