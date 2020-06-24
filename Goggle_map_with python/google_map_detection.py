from gmplot import gmplot
gmap=gmplot.GoogleMapPlotter(28.689169,77.324448,17)

gmap.coloricon ='http://www.googlemapsmaker.com/v1/%s/'

gmap.marker(28.526736,77.144444,'yellow')
gmap.draw("C:\\Users\\USER\\Desktop\\mymap.html")