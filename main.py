import phonenumbers
import folium
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
number="put your number here"
pepnumber=phonenumbers.parse(number)
location=geocoder.description_for_number(pepnumber,"en")
print(location)

service_pro=phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,"en"))

key="get your api key from openCage"
geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
print(results)

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']

print(lat,lng)

myMap=folium.Map(location=[lat,lng],Zoom_start=9)

folium.Marker([lat,lng],popup=location).add_to(myMap)

myMap.save("myLocation.html")
