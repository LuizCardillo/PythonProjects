import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

weatherNotifier = ToastNotifier()

def getData(url):
    data = requests.get(url)

    return data.text

htmlData = getData("https://weather.com/en-IN/weather/today/l/10d1572387a11118e42f6b8182334a205b8a6a3259e356628044cc98419089d0")

soup = BeautifulSoup(htmlData, 'html.parser')

currentTemp = soup.find_all("span",  
                             class_="CurrentConditions--tempValue--zUBSz")
currentTempMinMax = soup.find_all("div",  
                             class_="CurrentConditions--tempHiLoValue--Og9IG") 

  
temp = str(currentTemp)
tempMinMax = str(currentTempMinMax)    

print(tempMinMax)
print(tempMinMax[113:115])
print(tempMinMax[237:239])

  
result = "Temperatura " + temp[92:94] + "°C \n" + "Temp. Max: "+ tempMinMax[113:115] + "°C " + "Temp. Min: " + tempMinMax[237:239] + "°C \n"

weatherNotifier.show_toast("Weather update", result, duration = 10)
