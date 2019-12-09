def run():
    letters= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r",
    "s","t","u","v","x","y","z"]
    count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    text = str(input("Ingresa un texto: "))
    msg=""
    i=0 
    for i in letters:
        print( text.find(i))
    
    for j in count:
        print(j.)

        
        
    

    


        


"""
if text.find("a") >=0:
    msg +="a"+str(text.count("a"))
else:
    msg += "0"
if  text.find("b") >=0:
    msg+="b"+str(text.count("b"))
else:
    msg += "0"
if  text.find("c") >=0:
    msg +="c"+str(text.count("c"))
else:
    msg += "0"
if  text.find("d") >=0:
    msg +="d"+str(text.count("d"))
else:
    msg += "0"

print(msg)
"""
if __name__ == "__main__":
    run()
