from urllib.request import *

def loadData(url):
    #open file from git
    datafile = urlopen(url)
    dataRecords = datafile.read().decode("utf-8").split("\n")
    #get keys from first line
    keys = dataRecords[0].split(',')
    for i in range(len(keys)):
        keys[i]="".join(keys[i].split("\""))
    data=[]
    #convert records to dicts, ignoring keys
    for line in dataRecords[1:]:
        record = {}
        values = line.split("\",\"")
        for i in range(len(keys)):
            if (i<len(values)):
                record[keys[i]]="".join(values[i].split('\"'))
            else:
                record[keys[i]]=""
        data.append(record)
    return data

def yearlyFishing(data):
    yearTotals={}
    for record in data:
        if record['SPECIES']=='All aquatic organisms':
            val = "".join(record['Value'].split(" "))
            if val!=':' and val!='':
                val=float(val)
                if yearTotals.get(record['TIME']):
                    yearTotals[record['TIME']]+=val
                else:
                    yearTotals[record['TIME']] = val
    return yearTotals

def bySpeciesData(data):
    fishTotals={}
    for record in data:
        if record['SPECIES']!='All aquatic organisms':
            val = "".join(record['Value'].split(" "))
            if val!=':' and val!='':
                val=float(val)
                if fishTotals.get(record['SPECIES']):
                    fishTotals[record['SPECIES']]+=val
                else:
                    fishTotals[record['SPECIES']] = val
    return fishTotals

fishingData = loadData('https://raw.githubusercontent.com/KiTeoki/greenhack/master/data/fish_ca_m_Data.csv')
yearlyTotals = yearlyFishing(fishingData)
perFishData = bySpeciesData(fishingData)
#moreYearsDataSet = loadData('https://raw.githubusercontent.com/KiTeoki/greenhack/master/data/fish_ca_m_Data.csv')