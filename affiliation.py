import json
import os
import argparse
from base import portrait_url

def build_affiliation_template(aff_name: str, vertical: bool = False) -> str:
    template_path = "affiliation_template_vertical.html" if vertical else "affiliation_template.html"

    with open(template_path, encoding='utf-8') as template_file:
        template = template_file.read()

    json_path = os.path.join("affiliations", f"{aff_name}.json")
    with open(json_path, encoding='utf-8') as data_file:
        data = json.load(data_file)

    template = template.replace("@AffiliationName", data["Affiliation"].upper())
    
    pokemon_list_html = ""
    for pokemon in data["Affiliated Pokemon"]:
        pokemon_list_html += f"<div>• {pokemon}</div>\n"
    template = template.replace("@PokemonList", pokemon_list_html)

    template = template.replace("@FlavorText", data["footer"]["flavor_text"])
    template = template.replace("@RuleText", data["footer"]["rule_text"])
    
    # Use the local portrait if it exists, otherwise use the base URL
    portrait_path = data.get("Portrait", f"{data['Affiliation']}.png")
    template = template.replace("#portrait#", portrait_url + portrait_path)

    return template

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate affiliation HTML output.")
    parser.add_argument("--aff", type=str, default="misty", help="Affiliation filename (without .json).")
    parser.add_argument("--vertical", action="store_true", help="Generate vertical card format.")

    args = parser.parse_args()
    aff_file = args.aff

    template = build_affiliation_template(aff_file, args.vertical)
    
    suffix = "_affiliation_vertical.html" if args.vertical else "_affiliation.html"
    output_path = f"results/{aff_file}{suffix}"
    with open(output_path, "w", encoding='utf-8') as result_file:
        result_file.write(template)
    
    print(f"Affiliation card generated at: {output_path}")
