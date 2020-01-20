import requests
import os
import re

# All Stock Symbols => OPEN FILE
file = open('symbols', encoding='utf-8')

# Parsing 'file' to make it Readable
symbols = [x.replace("\u200c", "").split(",") for x in file]

# Getting Last element of each symbol (which is the link) for further use
link_list = [re.findall("[0-9]{11,20}", x[-1])[0] for x in symbols]
#                                              ^ -> SHIT GOT REAL

# Name list (to zip with link list)
namaad_far_list = [n[6] for n in symbols]
namaad_eng_list = [n[4] for n in symbols]

# **********************************************************************************************************************
# DOWNLOADER:
# **********************************************************************************************************************
base_url = "http://tsetmc.ir/tsev2/data/Export-txt.aspx?t=i&i="

# Test
# print(namaad_far_list)
# print(namaad_eng_list)
# print(link_list)

dl_list = [list(a) for a in zip(namaad_eng_list, namaad_far_list, link_list)]

for i in dl_list:
    if not os.path.isdir("\\bazaar\\{}".format(i[1])):
        os.makedirs("\\bazaar\\{}".format(i[1]))
    url = (base_url + i[2])
    if not os.path.exists("\\bazaar\\{0}\\{1}.csv".format(i[1], i[0])):
        data = requests.get(url).content
        with open("\\bazaar\\{0}\\{1}.csv".format(i[1], i[0]), "wb") as f:
            f.write(data)
        print("{} Data Downloaded ...".format(i[0]))

print("Downloading Finished!")
