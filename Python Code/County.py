import simplejson
import urllib
import csv

r = open('county.csv')
readCSV = csv.reader(r)

w = open('distances.csv', 'w')
writeCSV = csv.writer(w)

w2 = open('distances2.csv', 'w')
writeCSV2 = csv.writer(w2)
        
lat = []
lon = []

for row in readCSV:
	lat.append(row[4])
	lon.append(row[5])
	
dest_lat = [41.072567, 41.567075, 39.113295, 39.882520, 41.411751, 41.128741, 39.924966, 39.536818, 39.327884, 39.748312, 41.660098, 40.729743]
dest_lon = [-81.536353, -81.572558, -84.513663, -83.049774, -82.280330, -80.706277, -83.799540, -82.392169, -84.516127, -84.209972, -83.544621, -84.080825]

for i in range(0, 88):
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
	writeCSV2.writerow([times.index(min(times))])
	print(str(i+1) + " of 90")