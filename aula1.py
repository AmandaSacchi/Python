# # full_name = "Amanda"
# # birth_year = input ("Qual ano voce nasceu?")
# # year = 2019
# # print(year - int(birth_year))
# # lbs = input ("Quantas lbs voce quer converter? => ")
# # kg = int (lbs) * 0.45
# # print (int(kg))
# ----------------------------------------------------------------
# # name = "Ana Julia"
# # print(name[1:5]) #Printa somente as posições 1-5
# # print(len(name)) #Mostra o numero de caracteres
# # print(name.find("a")) #Encontra quantos as tem (é sensivel a maiusculas e minusculas)
# # print(name.replace("Ana", "Maria")) #Substitui ana por maria
# ----------------------------------------------------------------
# # course = "Estação Hack do Facebook"
# # print("Hack" in course)
# ----------------------------------------------------------------
# # summer = True
# # winter = False

# # if summer:
# #     print("Use protetor")
# # else:
# #     print("Suave")
# # elif winter: #Elseif é uma mini condição
# #     print("Poe casaco")
# ----------------------------------------------------------------
# # green_bank = True
# # criminal = False
# # money = True


# # if green_bank and money and not criminal: 
# #     print ("Tudo ok!")
# # else:
# #     print ("Deu ruim!")

# ----------------------------------------------------------------
# # i=0
# # while i < 5:
# #     print (i)
# #     i = i+1
# # print (".")

number = 9
i=0
while i<3:
    tentativa = int (input("Qual o numero?"))
    if tentativa == number:
        input ("Acertou")
        break
    else : 
        print ("Tente novamente")
    i = i+1
