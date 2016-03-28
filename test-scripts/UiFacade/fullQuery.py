import os.path
import android
import time
from string import join

cur_dir = os.path.dirname(os.path.realpath(__file__)) + "/"

def getXML(filename):
    fin = open(cur_dir + filename, "r")
    lines = fin.readlines()
    fin.close()
    return join(lines)

droid = android.Android()

xml = getXML("layout.xml")

droid.fullShow(xml)

query = droid.fullQuery()

time.sleep(2)

droid.fullDismiss()

print query.result
