cities = ["Самара", "Москва", "Санкт-Петербург",
            "Анапа", "Новосибирск", "Екатеринбург",
            "Архангельск", "Краснодар","Александровск"]
new_cities = list([city for city in cities if city[0]=="А" and len(city)>=7])
u_cities = list([city for city in cities if len(city)==len(set(city.lower()))])
print(u_cities)