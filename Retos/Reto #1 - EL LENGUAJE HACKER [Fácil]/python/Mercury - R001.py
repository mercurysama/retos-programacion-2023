abcedario = {'A':'4','Á':'4','B':'I3','C':'[','D':')','E':'3','É':'3','F':'|=','G':'6','H':'#','I':'1','Í':'1','J':'_|','K':'|<','L':'|','M':'/\\/\\',
             'N':'|\|','O':'0','Ó':'0','P':'|D','Q':'(,)','R':'|2','S':'5','T':'7','U':'(_)','Ú':'(_)','V':'\\/','W':'\\/\\/','X':'><','Y':"'/",'Z':'2'}

def separar_texto(text):
    text= text.upper()
    return text.split()

def cambio(letra):
    palabra_tmp=str()
    for letra in letra:
        if letra not in abcedario:
            palabra_tmp += letra
        else:
            palabra_tmp += abcedario[letra]
    return palabra_tmp

def traducir_texto(text):
    text_tmp=[]
    for palabra in text:
        text_tmp.append( cambio(palabra))
    return text_tmp

def main(text):
    text=separar_texto(text)
    text=traducir_texto(text )
    print('  '.join(text))


main(input('Ingrese el texto a traducir:  '))