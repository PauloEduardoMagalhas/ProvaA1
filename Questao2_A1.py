import re
def Letraporx(texto):
    textodiferente=re.sub('[aeiouAEIOU]','x',texto)
    return textodiferente