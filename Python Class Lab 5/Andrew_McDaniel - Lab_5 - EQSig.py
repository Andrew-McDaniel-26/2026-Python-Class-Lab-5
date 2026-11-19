# Andrew Mcdaniel
# python 2026 
# lab 5 - 11/19/26

import json
import urllib.request
import statistics

# the url for the erthquake data and the code neccesary to read that data
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson"
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())

#sorts the data
sig_list = []
for quake in data["features"]:
    sig = quake["properties"].get("sig")
    if sig is not None:
        sig_list.append(sig)



#sets up the diffrent variables for the mathmatics and the solves for the result
min_sig = min(sig_list)
max_sig = max(sig_list)
mean_sig = statistics.mean(sig_list)
median_sig = statistics.median(sig_list)
stdev_sig = statistics.stdev(sig_list)
modes_sig = statistics.multimode(sig_list)

#prints out the diffrent results out to tree decimals
print(f"the minimum sig is : {min_sig:.3f}")
print(f"the maximum sig is : {max_sig:.3f}")
print(f"the mean sig is : {mean_sig:.3f}")
print(f"the median sig is : {median_sig:.3f}")
print(f"the standered deviation sig is : {stdev_sig:.3f}")

#prints out the mode/s for the sig data
listed_modes = ", ".join(f"{m:.3f}" for m in modes_sig)
print(f"The mode(s) of sig is / are {listed_modes}")