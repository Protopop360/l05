# scientists = ("Альберт", "Диофант", "Максвелл")
# main="Cobol"
# langs = "Java", "Assember", "Scratch", main
# print(langs)
# main = "C++"
# print(langs)
# langs = "Java", "Assember", "Scratch", main
# print(langs)
# print(langs[1])
# x, y, z=scientists
# print(scientists)
# print(y)
# a, b, c, d, e, f= 1, 2, 3, 4, 5, 6
# print(a,b,c,d,e,f)
# a=3
# b=5
# a,b=b,a
# print(a,b)
saeed= {}
print(saeed)
writers = {"Рей Бредбери", "Джордж Оруэлл", \
"Жуль Верн", "Эрих Мария Ремарк", ""}
print(writers)
antiutop={"Оксана","Рей Бредбери" , "Джордж Оруэлл", "Замятин"}
print(writers & antiutop)#пересечение
print(writers | antiutop)#объединение
print(antiutop-writers)#вычитание 1 из 2
print(writers-antiutop)#вычитание 2 из 1
print(antiutop^writers)#все элементы без общих

director = {
    "Спилберг": ("Парк Юрского периода","Челюсти","Список Шиндлера"),
    "Нолан": ("Дюнкерк", "Престиж", "Начало"),
    "Бондарчук":("Притяжение")
}
print(director)
print(director["Нолан"])
director["Бондарчук"]=["Мусор", "Шлак"]#присвоили значения шлока для ключа
print(director)
director[5]= 12345
director[True] = "Матильда"
print(director)
director[("Билл Гейтс", "Марк Цукерберг" )] = "Айтишки"
print(director["Билл Гейтс"])