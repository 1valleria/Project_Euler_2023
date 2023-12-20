#import os
#os.system("pip install phonenumbers")
#os.system("pip install opencage")
#os.system("pip install folium")
number = "+447859606537"

import phonenumbers
import opencage
import folium
from phonenumbers import geocoder


key = 'feeaaabdcf094d30b144b145dc8a02b7'

check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number,"en")
print(number_location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)

query = str(number_location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location = [lat,lng], zoom_start=9)
folium.Marker([lat,lng],popup=number_location).add_to(myMap)

myMap.save("mylocation.html")