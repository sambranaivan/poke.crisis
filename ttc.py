import json
import os
import argparse
from base import portrait_url

# Base URL for TTC art (same repo structure)
ttc_art_url = "https://raw.githubusercontent.com/sambranaivan/poke.crisis/master/ttc_art/"

def build_ttc_template(ttc_name: str) -> str:
    template_path = "ttc_template.html"

    with open(template_path, encoding='utf-8') as template_file:
        template = template_file.read()

    json_path = os.path.join("ttc", f"{ttc_name}.json")
    with open(json_path, encoding='utf-8') as data_file:
        data = json.load(data_file)

    # Replace card name
    template = template.replace("@CardName", data["Name"].upper())
    
    # Replace affiliation
    template = template.replace("@Affiliation", data["Affiliation"].upper())
    
    # Replace cost
    template = template.replace("@Cost", str(data["Cost"]))
    
    # Replace card type
    template = template.replace("@CardType", data["Type"].upper())
    
    # Build effect list
    effect_html = ""
    for effect in data["Effect"]:
        effect_html += f'<div class="mb-1">• {effect}</div>\n'
    template = template.replace("@EffectList", effect_html)
    
    # Replace restriction
    template = template.replace("@Restriction", data["Restriction"])
    
    # Replace identity
    template = template.replace("@Identity", data["Identity"])
    
    # Replace art URL
    art_file = data.get("Art", "tt01.png")
    template = template.replace("#art#", ttc_art_url + art_file)

    return template

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Team Tactic Card HTML output.")
    parser.add_argument("--ttc", type=str, required=True, help="TTC filename (without .json).")

    args = parser.parse_args()
    ttc_file = args.ttc

    template = build_ttc_template(ttc_file)
    
    output_path = f"results/{ttc_file}_ttc.html"
    with open(output_path, "w", encoding='utf-8') as result_file:
        result_file.write(template)
    
    print(f"Team Tactic Card generated at: {output_path}")
