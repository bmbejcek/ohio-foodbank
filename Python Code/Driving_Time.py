import simplejson
import urllib
import csv

r = open('tract.csv')
readCSV = csv.reader(r)

w = open('distances.csv', 'w')
writeCSV = csv.writer(w)
        
tract = []
lat = []
lon = []

for row in readCSV:
	tract.append(row[0])
	lat.append(row[1])
	lon.append(row[2])
	
dest_lat = [41.072567, 41.567075, 39.113295, 39.882520, 41.411751, 41.128741, 39.924966, 39.536818, 39.327884, 39.748312, 41.660098, 40.729743]
dest_lon = [-81.536353, -81.572558, -84.513663, -83.049774, -82.280330, -80.706277, -83.799540, -82.392169, -84.516127, -84.209972, -83.544621, -84.080825]

for i in range(1000, 2951):
	times = []
	for x in range(0,12):
		url = "http://router.project-osrm.org/viaroute?loc="+str(lat[i])+ "," +str(lon[i]) + "&loc=" +str(dest_lat[x]) + "," +str(dest_lon[x])
		result = simplejson.load(urllib.urlopen(url))
		result = str(result)
		result = result.split("'total_time': ")
		result = str(result[1])
		result = result.split(",")
		result = int(result[0])
		times.append(result)
	writeCSV.writerow([min(times)])
	print(str(i+1) + " of 2950")