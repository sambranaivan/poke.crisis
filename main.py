from base import portrait_url
from attacks import make_attack
from stats import make_stats
from powers import make_sp
import json
from html import escape
import pyperclip

template = open('template.html')
template = template.read()
f = open('json/Mega Gengar.json')
data = json.load(f)




######BLOQUE DE ATAQUES

attack_html  = '''<div class="mt-8 ml-7 px-2 py-1 w-213 h-[46rem] flex flex-col z-20">'''

for attack in data["Attacks"]:
    attack_html += make_attack(attack)+'''<div class="flex flex-shrink h-[20px]"></div>'''


template = template.replace("@HealtyAttacks",attack_html)

######BLOQUE DE STATS
template = template.replace("@yield_stats",make_stats(data))

######BLOQUE DE STATS HERIDO
template = template.replace("@yield_inyured",make_stats(data))

######BLOQUE DE HABILIDARES

superpower_html = ""
for super in data['Superpowers']:
    superpower_html += make_sp(super)+'''<div class="flex flex-shrink h-[20px]"></div>'''
superpower_html += '''</div>'''

template = template.replace("@yield_superpowers",superpower_html)


####### PORTRAIT
port = (data["Name"]).replace(" ","%20")
template = template.replace("#potrait#",portrait_url+data["Name"]+".png")

################INJURED SIDE
######BLOQUE DE ATAQUES

attack_html  = '''<div class="mt-8 ml-7 px-2 py-1 w-213 h-[46rem] flex flex-col z-20">'''

for attack in data["Attacks"]:
    attack_html += make_attack(attack)+'''<div class="flex flex-shrink h-[20px]"></div>'''
##suma el nuevo ataque
for attack in data["Injured Side"]["Attacks"]:
    attack_html += make_attack(attack)+'''<div class="flex flex-shrink h-[20px]"></div>'''

template = template.replace("@injured_attacks",attack_html)

######BLOQUE DE HABILIDARES

superpower_html = ""
for super in data['Superpowers']:
    superpower_html += make_sp(super)+'''<div class="flex flex-shrink h-[20px]"></div>'''

for super in data["Injured Side"]['Superpowers']:
    superpower_html += make_sp(super)+'''<div class="flex flex-shrink h-[20px]"></div>'''

superpower_html += '''</div>'''

template = template.replace("@injured_sp",superpower_html)


#FIN

h = open("results.html", "w")
pyperclip.copy(template)
h.write(template)
h.close()

# print(template)
"""
var script = document.createElement('script');
script.src = "https://ajax.googleapis.com/ajax/libs/jquery/1.6.3/jquery.min.js";
document.getElementsByTagName('head')[0].appendChild(script);
$(".stat-card-inner").html("")
"""