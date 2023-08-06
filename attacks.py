import json
f = open('icons.json')
icon = json.load(f)



def make_attack(data):
    # HTML template
    html_template = '''<div class="w-full flex flex-col cursor-pointer">
    <div class="flex flex-row items-center pr-5">
        <div class="pill-with-badge relative flex flex-row h-11 w-full flex-1"><span
                class="bg-black rounded-full z-10 w-11 h-11">
                <div class="h-full text-white flex flex-col justify-center align-center w-11 text-3xl"><img
                        src="#tipo#"
                        class="rounded-full w-11"></div>
            </span>
            <div class="flex flex-col align-center -ml-3 self-center w-full"><span
                    class="pill bg-black py-1 text-white font-bold font-face-agency-fb-bold h-[2.1rem] whitespace-nowrap rounded-r-full w-full pl-5 pr-4 leading-6.5 text-2.5xl"><span
                        class="whitespace-pre"><span class="leading-6.5 text-2.5xl">#N#</span><span
                            class="tracking-wider leading-5 text-xl">#NAME#</span></span></span></div>
        </div><img src="https://www.jarvis-protocol.com/assets/images/1f242578030fb793b602.png"
            class="w-9 h-9 ml-2"><span class="font-face-noto-sans-condensed-bold text-1.5xl ml-px w-6">#RANGE#</span><img
            src="https://www.jarvis-protocol.com/assets/images/81ea86310cbf035f4605.png" class="w-9 h-9 ml-1"><span
            class="font-face-noto-sans-condensed-bold text-1.5xl ml-px w-6">#STRENGTH#</span><img
            src="https://www.jarvis-protocol.com/assets/images/f0ea0a964b55961f664a.png" class="w-9 h-9 ml-1"><span
            class="font-face-noto-sans-condensed-bold text-1.5xl ml-px">#COST#</span>
    </div>
    <div data-component="attack-content" class="font-face-noto-sans-condensed min-h-0.5 [word-spacing:-1px] text-xl">
        <div class="h-[2px] shrink"></div>
        <ul class="list-disc ml-7 mt-[-2px]">
            <li data-component="special-rule"
                class="pl-2 mb-1 last:mb-0 [word-spacing:-0.5px] leading-[1.3rem] text-xl"><span><span>#description#
                    </span></span></li>
        </ul>
    </div>
</div>'''

 

    # Replace the placeholders with the corresponding values from the JSON

    replaced_html = html_template.replace("#N#", str((data["Name"][0]).upper()))
    replaced_html = replaced_html.replace("#NAME#", str((data["Name"][1:]).upper()))
    replaced_html = replaced_html.replace("#RANGE#", str(data["Range"]))
    replaced_html = replaced_html.replace("#STRENGTH#", str(data["Strength"]))
    replaced_html = replaced_html.replace("#COST#", str(data["Power Cost"]))
    replaced_html = replaced_html.replace("#description#", str(data["Effect"]))
    replaced_html = replaced_html.replace("#tipo#",  icon[data["Type"]]  )
    # print(data["NAME"][0])
    return replaced_html

# Example usage


