
xml = """<HostipLookupResultSet xmlns:gml="http://www.opengis.net/gml" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.0.1" xsi:noNamespaceSchemaLocation="http://www.hostip.info/api/hostip-1.0.1.xsd">
           <gml:description>This is the Hostip Lookup Service</gml:description>
           <gml:name>hostip</gml:name>
           <gml:boundedBy>
             <gml:Null>inapplicable</gml:Null>
           </gml:boundedBy>
           <gml:featureMember>
             <Hostip>
               <ip>12.215.42.19</ip>
               <gml:name>Aurora, TX</gml:name>
               <countryName>UNITED STATES</countryName>
               <countryAbbrev>US</countryAbbrev>
               <!-- Co-ordinates are available as lng,lat -->
               <ipLocation>
                 <gml:pointProperty>
                   <gml:Point srsName="http://www.opengis.net/gml/srs/epsg.xml#4326">
                     <gml:coordinates>-97.5159,33.0582</gml:coordinates>
                   </gml:Point>
                 </gml:pointProperty>
               </ipLocation>
             </Hostip>
           </gml:featureMember>
        </HostipLookupResultSet>"""

# QUIZ - implement the get_coords(xml) function that takes in an xml string 
# and returns a tuple of (lat, lon) if there are coordinates in the xml.
# Remember that you should use minidom to do this.
# Also, notice that the coordinates in the xml string are in the format:
# (lon,lat), so you will have to switch them around.

from xml.dom import minidom

def get_coords(xml):
    dom = minidom.parseString(xml)
    gml_coordinates = dom.getElementsByTagName('gml:coordinates')
    if gml_coordinates:
        element = gml_coordinates[0]
        if element:
            childNodes = element.childNodes
            if childNodes:
                if childNodes[0].nodeType == childNodes[0].TEXT_NODE:
                    coordinates = childNodes[0].data
                    if coordinates:
                        coordinatesSplit = coordinates.split(',')
                        if len(coordinatesSplit) == 2:
                            return (coordinatesSplit[1], coordinatesSplit[0])

# Udacity version
def get_coords2(xml):
    d = minidom.parseString(xml)
    coords = d.getElementsByTagName('gml:coordinates')
    if coords and coords[0].childNodes[0].nodeValue:
        lon, lat = coords[0].childNodes[0].nodeValue.split(',')
        return lat, lon

print get_coords(xml)
print get_coords2(xml)

