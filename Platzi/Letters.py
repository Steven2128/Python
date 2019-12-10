def run():
    letters= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r",
    "s","t","u","v","x","y","z"]
    text = str(input("Ingresa un texto: "))
    msg=""
    i=0 
    for i in letters:
        if text.find(i)>=0:
            count_letters = text.count(i)
            msg += str(i)+str(count_letters)
    print(msg)

if __name__ == "__main__":
    run()
