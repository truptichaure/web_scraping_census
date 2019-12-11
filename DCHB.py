#!/bin/python

# Download Census india data from http://www.censusindia.gov.in/2011census/dchb/DCHB.html


"""
#  urls

for(i=4;i<50;i++){
   console.log($('table#xxxx tbody tr:nth-child('+i+') td:nth-child(6) a').href);
}


http://www.censusindia.gov.in/2011census/dchb/Andaman_Nicobar_Islands_tables.html
http://www.censusindia.gov.in/2011census/dchb/Ap.html
http://www.censusindia.gov.in/2011census/dchb/Arunachal_Pradeshtables.html
http://www.censusindia.gov.in/2011census/dchb/AssamTables.html
http://www.censusindia.gov.in/2011census/dchb/Bihar_tables.html
http://www.censusindia.gov.in/2011census/dchb/0401-Chandigarh.zip
http://www.censusindia.gov.in/2011census/dchb/Chhattisgarh_tables.html
http://www.censusindia.gov.in/2011census/dchb/2601-Dadra_&_Nagar_Haveli.zip
http://www.censusindia.gov.in/2011census/dchb/Daman_Diu_tables.html
http://www.censusindia.gov.in/2011census/dchb/goatables.html
http://www.censusindia.gov.in/2011census/dchb/Gujarat_tables.html
http://www.censusindia.gov.in/2011census/dchb/Haryana_tables.html
http://www.censusindia.gov.in/2011census/dchb/Himachal_Pradeshtables.html
http://www.censusindia.gov.in/2011census/dchb/Jamu_&kasmirTables.html
http://www.censusindia.gov.in/2011census/dchb/Jharkhand_tables.html
http://www.censusindia.gov.in/2011census/dchb/Karnataka_tables.html
http://www.censusindia.gov.in/2011census/dchb/KerlaTables.html
http://www.censusindia.gov.in/2011census/dchb/3101-Lakshadweep.zip
http://www.censusindia.gov.in/2011census/dchb/MPTables.html
http://www.censusindia.gov.in/2011census/dchb/Maharashtratables.html
http://www.censusindia.gov.in/2011census/dchb/DCHB_ManipurTables.html
http://www.censusindia.gov.in/2011census/dchb/Meghalayazip.html
http://www.censusindia.gov.in/2011census/dchb/MIZORAMtables.html
http://www.censusindia.gov.in/2011census/dchb/NagalandTables.html
http://www.censusindia.gov.in/2011census/dchb/DelhiTables.html
http://www.censusindia.gov.in/2011census/dchb/Odishatables.html
http://www.censusindia.gov.in/2011census/dchb/Puducherry_tables.html
http://www.censusindia.gov.in/2011census/dchb/Punjab_tables.html
http://www.censusindia.gov.in/2011census/dchb/Rajastantables.html
http://www.censusindia.gov.in/2011census/dchb/Sikkim_tables.html
http://www.censusindia.gov.in/2011census/dchb/TM.html
http://www.censusindia.gov.in/2011census/dchb/Tipura_tables.html
http://www.censusindia.gov.in/2011census/dchb/UPtables.html
http://www.censusindia.gov.in/2011census/dchb/Uttarakhand_tables.html
http://www.censusindia.gov.in/2011census/dchb/wb_table.html
"""
import os
from bs4 import BeautifulSoup
import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

if __name__ == "__main__":
    BASE_URL = "http://www.censusindia.gov.in/2011census/dchb/DCHB.html"
    BASE_URL_DIR = "http://www.censusindia.gov.in/2011census/dchb/"
    details_urls = []
    """
    # This block is not working 
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    trs = soup.find_all('td', attrs={'bgcolor':"#D3D3D3"})
    for tr in trs:
        a_link = tr.find('a')
        if a_link:
            try:
                if '.html' in a_link['href']:
                    label = a_link['href'].replace(".html","")
                    details_urls.append({label: "%s%s" % (BASE_URL_DIR, a_link['href'])})
            except Exception as e:
                pass
    print(details_urls)
    """

    base_urls = [
        "http://www.censusindia.gov.in/2011census/dchb/Andaman_Nicobar_Islands_tables.html",
        "http://www.censusindia.gov.in/2011census/dchb/Ap.html",
        "http://www.censusindia.gov.in/2011census/dchb/Arunachal_Pradeshtables.html",
        "http://www.censusindia.gov.in/2011census/dchb/AssamTables.html",
        "http://www.censusindia.gov.in/2011census/dchb/Bihar_tables.html",
        "http://www.censusindia.gov.in/2011census/dchb/0401-Chandigarh.zip",
        "http://www.censusindia.gov.in/2011census/dchb/Chhattisgarh_tables.html",
        "http://www.censusindia.gov.in/2011census/dchb/2601-Dadra_&_Nagar_Haveli.zip",
        "http://www.censusindia.gov.in/2011census/dchb/Daman_Diu_tables.html",
        "http://www.censusindia.gov.in/2011census/dchb/goatables.html",
        "http://www.censusindia.gov.in/2011census/dchb/Gujarat_tables.html",
        "http://www.censusindia.gov.in/2011census/dchb/Haryana_tables.html",
        "http://www.censusindia.gov.in/2011census/dchb/Himachal_Pradeshtables.html",
        "http://www.censusindia.gov.in/2011census/dchb/Jamu_&kasmirTables.html",
        "http://www.censusindia.gov.in/2011census/dchb/Jharkhand_tables.html",
        "http://www.censusindia.gov.in/2011census/dchb/Karnataka_tables.html",
        "http://www.censusindia.gov.in/2011census/dchb/KerlaTables.html",
        "http://www.censusindia.gov.in/2011census/dchb/3101-Lakshadweep.zip",
        "http://www.censusindia.gov.in/2011census/dchb/MPTables.html",
        "http://www.censusindia.gov.in/2011census/dchb/Maharashtratables.html",
        "http://www.censusindia.gov.in/2011census/dchb/DCHB_ManipurTables.html",
        "http://www.censusindia.gov.in/2011census/dchb/Meghalayazip.html",
        "http://www.censusindia.gov.in/2011census/dchb/MIZORAMtables.html",
        "http://www.censusindia.gov.in/2011census/dchb/NagalandTables.html",
        "http://www.censusindia.gov.in/2011census/dchb/DelhiTables.html",
        "http://www.censusindia.gov.in/2011census/dchb/Odishatables.html",
        "http://www.censusindia.gov.in/2011census/dchb/Puducherry_tables.html",
        "http://www.censusindia.gov.in/2011census/dchb/Punjab_tables.html",
        "http://www.censusindia.gov.in/2011census/dchb/Rajastantables.html",
        "http://www.censusindia.gov.in/2011census/dchb/Sikkim_tables.html",
        "http://www.censusindia.gov.in/2011census/dchb/TM.html",
        "http://www.censusindia.gov.in/2011census/dchb/Tipura_tables.html",
        "http://www.censusindia.gov.in/2011census/dchb/UPtables.html",
        "http://www.censusindia.gov.in/2011census/dchb/Uttarakhand_tables.html",
        "http://www.censusindia.gov.in/2011census/dchb/wb_table.html"
    ]
    details_urls = [{item.split("/")[-1].replace(".html", ""): item} for item in base_urls]

    zip_file_urls = dict.fromkeys([tuple(d)[0] for d in details_urls])
    # print(zip_file_urls)
    for item in details_urls:
        (key, url), = item.items()
        print(key)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        all_trs = soup.find_all('tr', attrs={'class': 'gridviwalternateitem'})
        for tr in all_trs:
            for a_link in (tr.find_all("a")):
                if '.zip' in a_link['href']:
                    if zip_file_urls[key]:
                        # print(a_link['href'])
                        # print(zip_file_urls)
                        zip_file_urls[key].append("%s%s" % (BASE_URL_DIR, a_link['href']))
                    else:
                        zip_file_urls[key] = ["%s%s" % (BASE_URL_DIR, a_link['href'])]

    print(zip_file_urls)

    for key, zip_urls in zip_file_urls.items():
        if not zip_urls:
            continue
        print(key)
        try:
            os.mkdir(key)
        except:
            pass
        os.chdir(key)
        for u in zip_urls:
            # fc = requests.get(document_final_url)
            local_file_name = u.split("/")[-1]
            if not os.path.exists(os.path.join('.',local_file_name)):
                print(u)
                s = requests.Session()
                retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
                s.mount('http://', HTTPAdapter(max_retries=retries))
                fc = s.get(u, timeout=60)
                print("downloading %s/%s" % (key, local_file_name))
                with open("%s" % local_file_name, "wb") as output:
                    output.write(fc.content)
        os.chdir("..")
