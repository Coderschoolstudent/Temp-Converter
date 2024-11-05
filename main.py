

import requests
print()
print("Hello there! This is Temp Converter; this program will use your input of any city in the world and tell you the temperature in 3 different units: fahrenheit, celsius, and kelvin. Enjoy!")
print()
while True:
    try:
        
        city = input("what city do you want to know the weather of? ")
        url1 = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid=d7ee37159ae7d162eee1c2d53c1e53d0"
        response = requests.get(url1)
        #print(response)

        #response = requests.get(url)

        if response.status_code == 200:
            #information gained from api is converted amd saved in a variable called data 
            data = response.json()
            #pulling latitude and longitude from data (list), save in 2 separate
            latitude = data[0]["lat"]
            longitude = data[0]["lon"]
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=d7ee37159ae7d162eee1c2d53c1e53d0"
            response = requests.get(url)
            #print(response)


        if response.status_code == 200:
            data = response.json()
            #print(data["weather"][0]["main"])
            #print(data["main"]["temp"])
            temp1 = int(data["main"]["temp"])
            b = "kelvin"


        #user_input = input("what is the scale? one word answers"_)
        #list1 = user_input.split(",")
        #temp1 = int(list1[1])
        #b = list1[2].strip()
        #b = user_input.strip()

    except:
        print("something went wrong. please check your spelling.")
    


    else:

        def fahrenheit(t, scale):

            if scale == "celsius":
                f = (t*2)+32
                
            if scale == "kelvin":
            #(K − 273.15) * 1.8 + 32
                f = (t- 273.15) * 1.8 + 32

                f = round(f,2)
            
            if scale == "fahrenheit":
                f = t

            return str(f)+ " degrees fahrenheit"


        def celsius(t, scale):

            if scale == "fahrenheit":
                c = (t-32)/2

            if scale == "kelvin":
            #C = K - 273.15.
                c = (t- 273.15)

                c = round(c,2)

            if scale == "celsius":
                c = t

            #if

                
            return str(c)+" degrees celsius"


        def kelvin(t, scale):

            #Kelvin = Celsius + 273.15.
            if scale== "celsius":
                k = t + 273.15

            if scale == "fahrenheit":
                #K = (F − 32) × 5 ⁄ 9 + 273.15
                k = (t-32)*5 / 9 + 273.15

                k = round(k,2)

            if scale == "kelvin":
                k = t

            return str(k)+" degrees kelvin"



        conversion1 = fahrenheit(temp1, b)
        conversion2 = celsius(temp1, b)
        conversion3 = kelvin(temp1, b)
        print(conversion1+", "+conversion2+", "+conversion3+".")

        break







