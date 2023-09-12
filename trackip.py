#!/usr/bin/env python3

import requests
import sys
from optparse import OptionParser
import os
from colorama import Fore as color
import shutil

G = color.GREEN
Y = color.YELLOW
RESET = color.RESET
def banner():
    width = shutil.get_terminal_size().columns
    banner1 = f"{Y}████████╗██████╗░░█████╗░░█████╗░██╗░░██╗██╗██████╗░"
    banner2 =     "╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██║██╔══██╗"
    banner3 =     "░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░██║██████╔╝"
    banner4 =     "░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██║██╔═══╝░"
    banner5 =     "░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗██║██║░░░░░"
    banner6 =     " ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░ "
    print(banner1.center(width))
    print(banner2.center(width))
    print(banner2.center(width))
    print(banner4.center(width))
    print(banner5.center(width))
#    cent = banner.center(width)
#    print(cent)
    auth = f"{G}Author: Freddy Phoenix Mills"
    vers = "Version: 1.0"
    mail = "Email: phoenixgibson007@gmail.com{RESET}"
    auth1 = auth #.center(width)
    vers1 = vers #.center(width)
    mail1 = mail #.center(width)
    print(auth.center(width))
    print(vers.center(width))
    print(mail.center(width))

app_name=sys.argv[0]
parser = OptionParser()
parser.add_option("-i", "--address", dest="address", help="Ip address to track amd lookup")
parser.add_option(f"-s", "--setup", dest="setup", help="Setup " + app_name)
#parser.add_option(f"-h", "--help", dest="help", help="Show the usage of {sys.argv[0]}")
parser.add_option(f"-u", "--update", dest="update", help="Update " + app_name)
(options, args) = parser.parse_args()
width = shutil.get_terminal_size().columns
#def setup():

def print_location_data(location_data):
    for key, value in location_data.items():
        print(f"{G}{key}: {value}".center(width))

def tracker():
    ip_address = options.address
    reply = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
	 	"Target Ip-Address" : ip_address,
                "Target Metwork" : reply.get("network\n-"),
	        "version" : reply.get("version"),
	        "City" : reply.get("city"),
   	        "Region of IP" : reply.get("region"),
    	        "Region code" : reply.get("region_code"),
	        "Ip Country" : reply.get("country"),
	        "Coumtry Name" : reply.get("country_name"),
	        "Ip Country Code" : reply.get("country_code"),
	        "ISO3" : reply.get("country_code_iso3"),
	        "Ip country Capital" : reply.get("country_capital"),
	        "Tld" : reply.get("country_tld"),
	        "Continent code of Ip" : reply.get("continent_code"),
	        "Country is in Europe" : reply.get("in_eu"),
	        "Ip location postal code" : reply.get("postal"),
	        "Ip Location Latitude" : reply.get(str("latitude")),
	        "Ip Locatiom Longitud" : reply.get(str("longitude")),
	        "Ip timezone" : reply.get("timezone"),
	        "UTC offset" : reply.get("utc_offset"),
	        "Ip country calling code" : reply.get("country_calling_code"),
	        "Currency" : reply.get("currency"),
	        "Currency Name" : reply.get("currency_name"),
	        "Languages" : reply.get("languages"),
	        "Country Area" : reply.get("country_area"),
	        "Country Population" : reply.get("country_population"),
	        "Asn" : reply.get("asn"),
	        "Org" : reply.get("org"),
		}
    latitude = reply.get("latitude")
    global lat
    lat = str(latitude)
    longitude = reply.get("longitude")
    global long
    long = str(longitude)
    global url
    url = "https://google.com/maps/place/" + lat +  "," + long + "/@" + lat
    #    return location_data#def update():
    print_location_data(location_data)

def update():
    os.system("rm -rf ../TrackIP")
    os.system("git vclone https://github.com/Anonphoenix007/TrackIP")
    os.system("cd TrackIP")
    print(color.GREEN + "Update successful" + ckolor.RED)

def install():
    os.syatem("pip3 install colorama requests")

if options.update:
   update()
if options.setup:
   install()
if options.address:
   banner()
   tracker()
#argus = sys.argv[1]
#if argus != "-u" or "-h" or "-i":
#   print(color.BLUE + "No argument supplied,run acript with --help to view the available flags" + color.RESET)
