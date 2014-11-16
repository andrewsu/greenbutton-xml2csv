import xml.etree.ElementTree as ET
import datetime
import sys

if( len(sys.argv) < 2 ):
   print "USAGE: python "+sys.argv[0]+" <inputfile> (<...>)"
   sys.exit()


for file in sys.argv[1:]:
   tree = ET.parse(file)
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
   
