countries = {
"mexico": 122,
"colombia": 49,
"argentina": 43,
"chile": 18,
"peru": 31,
"china": 1380,
"india": 1331,
"estados unidos": 325,
"brasil": 207,
"japon": 126,
"alemania": 82,
"francia": 64,
"espana": 46
}
while True:
    country = str(input("Escribe el nombre de un pais: ")).lower()

    try:
        print("La poblacion de "+str(country)+" es: "+str(countries[country])+" millones")
    except KeyError:
        print("No tenemos el dato de la poblacion de "+str(country))