import json
from base import icon_url
f = open('icons.json')
icon = json.load(f)



def make_sp(data):
    # HTML template
    try:
         cost = data["Cost"]
    except:
         cost = False
    if cost >0 :
        html_template = '''<div class="w-full flex flex-col cursor-pointer">
            <div class="flex flex-row">
                <div class="pill-with-badge relative flex flex-row h-11 w-full flex-1"><span
                        class="bg-black rounded-full z-10 w-11 h-11">
                        <div class="h-full text-white flex flex-col justify-center align-center w-11 text-3xl"><img
                                src="#icon#"
                                class="rounded-full w-11"></div>
                    </span>
                    <div class="flex flex-col align-center -ml-3 self-center w-full"><span
                            class="pill bg-black py-1 text-white font-bold font-face-agency-fb-bold h-[2.1rem] whitespace-nowrap rounded-r-full w-full pl-4 pr-4 leading-6.5 text-2.5xl"><span
                                class="whitespace-pre"><span class="leading-6.5 text-2.5xl">#S#</span><span
                                    class="tracking-wider leading-5 text-xl">#NAME#</span></span></span></div>
                </div>
                <div class="flex flex-row items-center mr-1 h-11">
                    <div class="flex flex-row bg-black rounded-full ml-1 items-center pr-[0.4rem] h-9"><img
                            src="https://www.jarvis-protocol.com/assets/images/f0ea0a964b55961f664a.png" class="w-9 h-9"><span
                            class="font-face-noto-sans-condensed-bold text-white text-1.5xl ml-2.5">#COST#</span></div>
                </div>
            </div>
            <div class="h-[4px] shrink"></div>
            <div data-component="superpower-content"
                class="font-face-noto-sans-condensed mt-[-4px] [word-spacing:-0.5px] ml-[2.7rem] text-xl leading-[1.3rem]">
                <span>#EFFECT#</span></div>
        </div>'''
    else:
        html_template = '''<div class="w-full flex flex-col cursor-pointer">
            <div class="flex flex-row">
                <div class="pill-with-badge relative flex flex-row h-11 w-full flex-1"><span
                        class="bg-black rounded-full z-10 w-11 h-11">
                        <div class="h-full text-white flex flex-col justify-center align-center w-11 text-3xl"><img
                                src="#icon#"
                                class="rounded-full w-11"></div>
                    </span>
                    <div class="flex flex-col align-center -ml-3 self-center w-full"><span
                            class="pill bg-black py-1 text-white font-bold font-face-agency-fb-bold h-[2.1rem] whitespace-nowrap rounded-r-full w-full pl-4 pr-4 leading-6.5 text-2.5xl"><span
                                class="whitespace-pre"><span class="leading-6.5 text-2.5xl">#S#</span><span
                                    class="tracking-wider leading-5 text-xl">#NAME#</span></span></span></div>
                </div>
              
            </div>
            <div class="h-[4px] shrink"></div>
            <div data-component="superpower-content"
                class="font-face-noto-sans-condensed mt-[-4px] [word-spacing:-0.5px] ml-[2.7rem] text-xl leading-[1.3rem]">
                <span>#EFFECT#</span></div>
        </div>'''

 

    # Replace the placeholders with the corresponding values from the JSON
    replaced_html = html_template.replace("#S#", str((data["Name"][0]).upper()))
    replaced_html = replaced_html.replace("#NAME#", str((data["Name"][1:]).upper()))
    if cost >0 :
        replaced_html = replaced_html.replace("#COST#", str(data["Cost"]))

    replaced_html = replaced_html.replace("#EFFECT#", str(data["Effect"]))
    replaced_html = replaced_html.replace("#icon#", icon_url+icon[data["Type"]])
    # print(data["NAME"][0])
    return replaced_html

# Example usage


