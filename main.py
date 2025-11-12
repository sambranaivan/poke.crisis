from base import portrait_url
from attacks import make_attack
from stats import make_stats
from powers import make_sp
import argparse
import json
from html import escape
import pyperclip


def build_template(chara: str, mcp: int) -> str:
    template_path = "mcp_template.html" if mcp else "template.html"

    with open(template_path) as template_file:
        template = template_file.read()

    with open("json/" + chara + ".json") as data_file:
        data = json.load(data_file)

    attack_html = '''<div class="mt-8 ml-7 px-2 py-1 w-213 h-[46rem] flex flex-col z-20">'''
    for attack in data["Attacks"]:
        attack_html += make_attack(attack, mcp) + '''<div class="flex flex-shrink h-[20px]"></div>'''
    template = template.replace("@HealtyAttacks", attack_html)

    template = template.replace("@yield_stats", make_stats(data, mcp))
    template = template.replace("@yield_inyured", make_stats(data, mcp))

    superpower_html = ""
    for superpower in data["Superpowers"]:
        superpower_html += make_sp(superpower) + '''<div class="flex flex-shrink h-[20px]"></div>'''
    superpower_html += '''</div>'''
    template = template.replace("@yield_superpowers", superpower_html)

    template = template.replace("#potrait#", portrait_url + data["Name"] + ".png")

    attack_html = '''<div class="mt-8 ml-7 px-2 py-1 w-213 h-[46rem] flex flex-col z-20">'''
    for attack in data["Attacks"]:
        attack_html += make_attack(attack, mcp) + '''<div class="flex flex-shrink h-[20px]"></div>'''
    for attack in data["Injured Side"]["Attacks"]:
        attack_html += make_attack(attack, mcp) + '''<div class="flex flex-shrink h-[20px]"></div>'''
    template = template.replace("@injured_attacks", attack_html)

    superpower_html = ""
    for superpower in data["Superpowers"]:
        superpower_html += make_sp(superpower) + '''<div class="flex flex-shrink h-[20px]"></div>'''
    for superpower in data["Injured Side"]["Superpowers"]:
        superpower_html += make_sp(superpower) + '''<div class="flex flex-shrink h-[20px]"></div>'''
    superpower_html += '''</div>'''
    template = template.replace("@injured_sp", superpower_html)

    return template


parser = argparse.ArgumentParser(description="Generate character HTML output.")
parser.add_argument("--chara", type=str, default="Chikorita", help="Character name that matches the JSON file.")

args = parser.parse_args()
chara = args.chara

generated_templates = {}
for mcp in (0, 1):
    template = build_template(chara, mcp)
    generated_templates[mcp] = template
    with open(f"results/{chara}_{'mcp' if mcp else 'poke'}.html", "w") as result_file:
        result_file.write(template)

pyperclip.copy(generated_templates[1])

# print(generated_templates[0])
# print(generated_templates[1])
# """
# var script = document.createElement('script');
# script.src = "https://ajax.googleapis.com/ajax/libs/jquery/1.6.3/jquery.min.js";
# document.getElementsByTagName('head')[0].appendChild(script);
# $(".stat-card-inner").html("")
# """