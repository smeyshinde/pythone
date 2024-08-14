import requests
import json
api_key='32d1c1746fba5e65dd8b5fd38a278ebb'
city='sangli'
url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
respones=requests.get(url)
if respones.status_code == 200:
 data=respones.json()
 print(json.dumps(data,indent=4))
 with open("weather data.json","w") as file:
  json.dump(data,file)
else:
  print(f"Error: {respones.status_code}")





import requests
import json
api_key='32d1c1746fba5e65dd8b5fd38a278ebb'
city='sangli'
url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
respones=requests.get(url)
data=respones.json()
print(json.dumps(data,indent=2))






from sklearn import SimpleImputer
import numpy
imp=SimpleImputer(missing_values=np.nan,shategy='mean')
imp.fit(X)

 
 