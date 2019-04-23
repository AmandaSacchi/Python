# full_name = "Amanda"
# birth_year = input ("Qual ano voce nasceu?")
# year = 2019
# print(year - int(birth_year))
# lbs = input ("Quantas lbs voce quer converter? => ")
# kg = int (lbs) * 0.45
# print (int(kg))
# ----------------------------------------------------------------
# name = "Ana Julia"
# print(name[1:5]) #Printa somente as posições 1-5
# print(len(name)) #Mostra o numero de caracteres
# print(name.find("a")) #Encontra quantos as tem (é sensivel a maiusculas e minusculas)
# print(name.replace("Ana", "Maria")) #Substitui ana por maria
# ----------------------------------------------------------------
# course = "Estação Hack do Facebook"
# print("Hack" in course)
# ----------------------------------------------------------------
# summer = True
# winter = False
# if summer:
#     print("Use protetor")
# else:
#     print("Suave")
# elif winter: #Elseif é uma mini condição
#     print("Poe casaco")
# ----------------------------------------------------------------
# green_bank = True
# criminal = False
# money = True


# if green_bank and money and not criminal: 
#     print ("Tudo ok!")
# else:
#     print ("Deu ruim!")
# ----------------------------------------------------------------
#i=0
# while i < 5:
#     print (i)
#     i = i+1
# print (".")

# number = 9
# i=0
# while i<3:
#     tentativa = int (input("Qual o numero?"))
#     if tentativa == number:
#         input ("Acertou")
#         break
#     else : 
#         print ("Tente novamente")
#     i = i+1
# num = [1,2,3,4,5,6]
# num.append(6)
# num.insert(0,1)
# i = 0
# while i<len(num):
#     if int (num[i]) == int(num)
#     num.remove(num[i])
# i = i + 1

# nova_lista = []
# for number in num:
#     if number not in nova_lista:
#         nova_lista.append(number)
# #curso = ("Mat", "Geo", "Por") => Isso é uma tupla ou tuple, os itens da lista não podem ser alterados, são constantes

# pessoa = {
#     "name": "Hayane",
#     "Age" : 26,
#     "Address" : "Sao Bernardo",
#     "Skills" : ["Python", "Java", "C", "Cobol"]
# }
# print(pessoa["name"])
# print(pessoa["address"])


maior=0
i=0
lista = [1,3,6,50,30,11]
while i<len(lista): # ou for i in lista (vai percorrer todos da lista)
    if lista[i] > maior:
        maior = lista[i]
    i = i + 1    
print (maior)

faltas = input("Quantas faltas?")
media = input ("Qual sua média?")
if int(faltas) <=2 and int(media)>=6 :
    print("Passou")
else :
    print("Reprovou")    
