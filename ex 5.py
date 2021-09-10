texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''

texto = texto.lower()
texto = texto.replace(',',' ').replace('.',' ').replace(':',' ')
texto = texto.split()

def e_python(p):
    if len(p) <= 4:
        return False
    for c in p :
        if c in 'python' :
            return True
        
    return False

lista = []
for p in texto:
    if e_python(p) and len(p) > 4:
        lista.append(p)
    
print (lista)
print (len(lista))   
