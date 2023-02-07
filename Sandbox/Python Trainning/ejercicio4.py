""" 4. Que son las expresiones regulares en Python? """
import re

p= re.compile (r'\bfoo\b')
texto =  """ bar foo bar
foo barbarfoo
foofoo foo bar
"""
fa = patron.findall(texto)

print(f"Las expresiones regulares (llamadas RE, o regex, o patrones de regex) son esencialmente en un lenguaje de programación \n diminuto y altamente especializado incrustado dentro de Python y disponible a través del módulo re. ")
print(f"Ejemplo --> p= re.compile (r'\bfoo\b') \n fa = patron.findall(texto) = {fa}")
    