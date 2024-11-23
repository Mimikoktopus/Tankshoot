
import requests
city = "Eichstaett"
countryCode = "de"
apiKey = "de385b1aa1c0a67843254d21af6dc54a"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{countryCode}&appid={apiKey}"
try:
    reponse = requests.get(url)
    if reponse.status_coded == 200:
        posts = reponse.json()
        print (posts)
    else:
        print("error:",reponse.status_code)
except:
    print("neeeeee")