from attacks import make_attack
from stats import make_stats
from powers import make_sp
import json


template = open('template.html')
template = template.read()
f = open('data.json')
data = json.load(f)





attack_html  = '''<div class="mt-8 ml-7 px-2 py-1 w-213 h-[46rem] flex flex-col z-20">'''

for attack in data["Attacks"]:
    attack_html += make_attack(attack)+'''<div class="flex flex-shrink h-[20px]"></div>'''
# attack_html += '''</div>'''

template = template.replace("@HealtyAttacks",attack_html)


template = template.replace("@yield_stats",make_stats(data))
template = template.replace("@yield_inyured",make_stats(data))

superpower_html = ""
for super in data['Superpowers']:
    superpower_html += make_sp(super)+'''<div class="flex flex-shrink h-[20px]"></div>'''
superpower_html += '''</div>'''

template = template.replace("@yield_superpowers",superpower_html)

h = open("results.html", "w")

h.write(template)
h.close()

# print(template)