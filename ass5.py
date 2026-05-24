# import random
# l=["rock","paper","scissor"]
# while True:
#     c=int(input("enter the choice :1- to play , 2-don't want to play "))
#     if c==1:
#         uscore=0
#         cscore=0
#         for i in range(1,6):
#             uch=input("Enter the choice ")
#             cch=random.choice(l)
            
#             print("computer choice",cch)
#             if(uch=="rock" or uch=="scissor" or uch=="paper"):
#                 if(uch==cch):
#                     uscore+=1
#                     cscore+=1
#                     print("Match draw")
#                 elif((uch=="rock" and cch=="scissor") or (uch=="paper" and cch=="rock") or (uch=="scissor" and cch=="paper")):
#                     uscore+=1
#                     print("you win")
#                 elif((cch=="rock" and uch=="scissor") or (cch=="paper" and uch=="rock") or (cch=="scissor" and uch=="paper")):
#                     cscore+=1
#                     print("computer win")
#             else:
             
#                print("enter correct choice")
#         print("\n final result")
#         print(f"User Score{uscore} \n Computer Score{cscore}")
#         if(uscore==cscore):
#             print("Match Draw")
#         elif(uscore>cscore):
#             print("You Win")
#         else:
#             print("Computer win")
#     elif c==2:
#         print("not played")
#         break
#     else:
#         print("invalid choice")
    



# import requests

# def weather_data(city):
#  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2955237a9d1df74ae332d498630fae44&units=metric"
#  try:
#      response = requests.get(url)
#      response.raise_for_status()
#      data=response.json()
#      print("\n------Weather Report------\n")
#      print("City:" , city)
#      print(f"Temperature :{data['main']['temp']}C")
#      print(f"Humidity :{data['main']['humidity']}C")
#      print(f"Feels Like:{data["main"]["feels_like"]}C")
#      print(f"Pressur:{data["main"]["pressure"]}hma")
#      print(f"wind speed :{data["wind"]["speed"]}m/s")
#      print(f"Visibility : {data["visibility"]/1000}km") 

#  except requests.exception.RequestsException as e:
#     print(e)

# city = input("Enter city Name:")
# weather_data(city)    

# 3) Search for more free API's generate your and call them to fetch data. Display some data in your program.

import requests

def news_data():
    url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=dac22c9e0829401cafe62ec084a48360"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        print("Top Business News Headlines:\n")

        for article in data["articles"][:5]:

            print("Title:", article["title"])
            print("Author:", article["author"])
            print("Source:", article["source"]["name"])
            print("Published At:", article["publishedAt"])
            print("Description:", article["description"])
            print("-" * 60)

    except requests.exceptions.RequestException as e:
        print("Error:", e)

news_data()


