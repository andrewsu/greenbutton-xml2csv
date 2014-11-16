import xml.etree.ElementTree as ET
import datetime
import sys


tree = ET.parse('data/SDGE_Electric_60_Minute_11-01-2012_10-31-2013_20141115231229344.xml')
root = tree.getroot()

for child in root:
   if( child.tag != '{http://www.w3.org/2005/Atom}entry'):
      continue
   if( len(child.findall('{http://www.w3.org/2005/Atom}title')) == 0):
      continue
   if( child.find('{http://www.w3.org/2005/Atom}title').text != 'Energy Usage'):
      continue
   for reading in child.findall('.//{http://naesb.org/espi}IntervalReading'):
      timestart = reading.find('./{http://naesb.org/espi}timePeriod/{http://naesb.org/espi}start').text
      timestartStr = datetime.datetime.fromtimestamp(int(timestart)).strftime('%Y-%m-%d %H:%M:%S')
      value = reading.find('{http://naesb.org/espi}value').text
      print timestartStr+","+ value

