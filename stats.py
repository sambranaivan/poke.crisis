def make_stats(data):
    html_template = '''<div class="mt-8 ml-6 w-67 h-[220px] z-20">
                <div class="font-face-agency-fb-black-condensed text-center" style="font-size: 35px; line-height: 35px; font-weight: bold; letter-spacing: 3px;">#NAME#</div>
                <div class="font-face-noto-sans-condensed text-center tracking-widest flex flex-wrap justify-center" style="font-size: 20px; line-height: 22px;"><span class="whitespace-pre"><span class="leading-4 tracking-normal mr-px text-xl">A</span><span class="tracking-wider leading-3 text-base"></span></span></div>
                <div class="flex flex-row justify-between mt-4">
                    <div class="pill-with-badge relative flex flex-row h-11"><span class="bg-black rounded-full z-10">
                            <div class="h-full text-white flex flex-col justify-center align-center w-11 text-2xl"><img src="https://www.jarvis-protocol.com/assets/images/e9d295985efdd834e3c7.png" class="rounded-full w-11 border-solid border-2 border-black"></div>
                        </span>
                        <div class="flex flex-col align-center -ml-3 self-center"><span class="pill bg-black py-1 text-white font-bold font-face-noto-sans-condensed-bold whitespace-nowrap rounded-r-full w-13 text-center pl-4 pr-4 leading-5 text-2xl"><span class="whitespace-pre"><span class="leading-5 text-2xl">#WEAK#</span></span></span></div>
                    </div>
                    <div class="pill-with-badge relative flex flex-row h-11"><span class="bg-black rounded-full z-10">
                            <div class="h-full text-white flex flex-col justify-center align-center w-11 text-2xl"><img src="https://www.jarvis-protocol.com/assets/images/0107812b0ce2a706b9eb.png" class="rounded-full w-11 border-solid border-2 border-black"></div>
                        </span>
                        <div class="flex flex-col align-center -ml-3 self-center"><span class="pill bg-black py-1 text-white font-bold font-face-noto-sans-condensed-bold whitespace-nowrap rounded-r-full w-13 text-center pl-4 pr-4 leading-5 text-2xl"><span class="whitespace-pre"><span class="leading-5 text-2xl">#NORMAL#</span></span></span></div>
                    </div>
                    <div class="pill-with-badge relative flex flex-row h-11"><span class="bg-black rounded-full z-10">
                            <div class="h-full text-white flex flex-col justify-center align-center w-11 text-2xl"><img src="https://www.jarvis-protocol.com/assets/images/74cda4cceec102296947.png" class="rounded-full w-11 border-solid border-2 border-black"></div>
                        </span>
                        <div class="flex flex-col align-center -ml-3 self-center"><span class="pill bg-black py-1 text-white font-bold font-face-noto-sans-condensed-bold whitespace-nowrap rounded-r-full w-13 text-center pl-4 pr-4 leading-5 text-2xl"><span class="whitespace-pre"><span class="leading-5 text-2xl">#RESISTANCE#</span></span></span></div>
                    </div>
                </div>
                <div class="flex flex-row mx-6 justify-around my-1">
                    <div class="pill-with-badge relative flex flex-row h-11"><span class="bg-black rounded-full z-10">
                            <div class="h-full text-white flex flex-col justify-center align-center w-11 text-2xl"><img src="https://www.jarvis-protocol.com/assets/images/b0259d18324c1b47f7f4.png" class="rounded-full w-11 border-solid border-2 border-black"></div>
                        </span>
                        <div class="flex flex-col align-center -ml-3 self-center"><span class="pill bg-black py-1 text-white font-bold font-face-noto-sans-condensed-bold whitespace-nowrap rounded-r-full w-13 text-center pl-4 pr-4 leading-5 text-2xl"><span class="whitespace-pre"><span class="leading-5 text-2xl">#STAMINA#</span></span></span></div>
                    </div>
                    <div class="pill-with-badge relative flex flex-row h-11"><span class="bg-black rounded-full z-10">
                            <div class="h-full text-white flex flex-col justify-center align-center w-11 text-2xl"><img src="https://www.jarvis-protocol.com/assets/images/02e15e0cacfb89a6849d.png" class="rounded-full w-11 border-solid border-2 border-black"></div>
                        </span>
                        <div class="flex flex-col align-center -ml-3 self-center"><span class="pill bg-black py-1 text-white font-bold font-face-noto-sans-condensed-bold whitespace-nowrap rounded-r-full w-13 text-center pl-4 pr-4 leading-5 text-2xl"><span class="whitespace-pre"><span class="leading-5 text-2xl">#THREAT#</span></span></span></div>
                    </div>
                </div>
                <div class="flex flex-row mx-6 justify-around">
                    <div class="pill-with-badge relative flex flex-row h-11"><span class="bg-black rounded-full z-10">
                            <div class="h-full text-white flex flex-col justify-center align-center w-11 text-2xl"><img src="https://www.jarvis-protocol.com/assets/images/3de72b61afe75cc3059a.png" class="rounded-full w-11 border-solid border-2 border-black"></div>
                        </span>
                        <div class="flex flex-col align-center -ml-3 self-center"><span class="pill bg-black py-1 text-white font-bold font-face-noto-sans-condensed-bold whitespace-nowrap rounded-r-full w-13 text-center pl-4 pr-4 leading-5 text-2xl"><span class="whitespace-pre"><span class="leading-5 text-2xl">#SIZE#</span></span></span></div>
                    </div>
                    <div class="pill-with-badge relative flex flex-row h-11"><span class="bg-black rounded-full z-10">
                            <div class="h-full text-white flex flex-col justify-center align-center w-11 text-2xl"><img src="https://www.jarvis-protocol.com/assets/images/218cf667347923fafe90.png" class="rounded-full w-11 border-solid border-2 border-black"></div>
                        </span>
                        <div class="flex flex-col align-center -ml-3 self-center"><span class="pill bg-black py-1 text-white font-bold font-face-noto-sans-condensed-bold whitespace-nowrap rounded-r-full w-13 text-center pl-4 pr-4 leading-5 text-2xl"><span class="whitespace-pre"><span class="leading-5 text-2xl">#MOVE#</span></span></span></div>
                    </div>
                </div>
            </div>'''
    # Replace the placeholders with the corresponding values from the JSON
    replaced_html = html_template.replace("#NAME#",str(data["Name"]))
    replaced_html = replaced_html.replace("#WEAK#",str(data["Weak Defense"]))
    replaced_html = replaced_html.replace("#NORMAL#",str(data["Defense"]))
    replaced_html = replaced_html.replace("#RESISTANCE#",str(data["Resistanse Defense"]))
    replaced_html = replaced_html.replace("#STAMINA#",str(data["Stamina"]))
    replaced_html = replaced_html.replace("#THREAT#",str(data["Threat Level"]))
    replaced_html = replaced_html.replace("#SIZE#",str(data["Size"]))
    replaced_html = replaced_html.replace("#MOVE#",str(data["Movement"]))

    # print(data["NAME"][0])
    return replaced_html
