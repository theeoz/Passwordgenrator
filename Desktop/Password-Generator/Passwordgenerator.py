import random
import string

normal = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
strong = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*?<>.\}{"
verystrong = "ỡŵĕřtўŭĭŏρăšɗfğɦĵƙlžҳčνƅňqωєятуυισραѕ∂ƒgнנкℓzχcνвη1234567890!@#$%&*?"
def id_generator(size=15, chars=normal):
    return ''.join(random.choice(chars) for _ in range(size))


def id_generator2(size=15, chars=strong):
    return ''.join(random.choice(chars) for _ in range(size))


def id_generator3(size=15, chars=verystrong):
    return ''.join(random.choice(chars) for _ in range(size))



def menu() :
        banner()
        print("""
        Please Choose Type Of Password : 
        1) Normal
        2) Strong
        3) Very Strong
        """)
        choose = input(">>")
        if choose == "1":
            print("Your Password Is : {0}".format(id_generator()))
        elif choose == "2" :
            print("Your Password Is : {0}".format(id_generator2()))
        elif choose == "3" :
            print("Your Password Is : {0}".format(id_generator3()))

def banner() :
    print("""
       ______ _______ _______ _______ ________ _______ ______ _____                                           __                 
      |   __ \   _   |     __|     __|  |  |  |       |   __ \     \     .-----.-----.-----.-----.----.---.-.|  |_.-----.----.   
      |    __/       |__     |__     |  |  |  |   -   |      <  --  |    |  _  |  -__|     |  -__|   _|  _  ||   _|  _  |   _|  
      |___|  |___|___|_______|_______|________|_______|___|__|_____/     |___  |_____|__|__|_____|__| |___._||____|_____|__|     
                     v1.0                                                |_____|                                                 
      Coded By : The Oz || Instagram : @oz_coder



""")


menu()







