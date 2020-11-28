#!/usr/bin/python2

import phonenumbers
 from phonenumbers import geocoder, carrier
print ("\033[1;32m Hacker \033[0m")
os.system("figlet Black.1")
num = input("number : ")
phoneNumber = phonenumbers.parse("+"+num)
Carrier = carrier.name_for_number(phoneNumber, 'en')
country = geocoder.country_name_for_number(phoneNumber, "en")
state = geocoder.description_for_number(phoneNumber, 'en')
print("carrier = "+Carrier)
print("Country = "+country)
print("state = "+state)