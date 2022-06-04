from xml.etree import ElementTree as ET
import yaml

with open("rares.yml", "r", encoding="utf8") as ymlfile:
    config = yaml.load(ymlfile, Loader=yaml.FullLoader)

html = ET.Element('html')
head = ET.Element('head')
stylesheet = ET.Element('link', attrib={'rel': 'stylesheet', 'href': "style.css"})
head.append(stylesheet)
wowheadScript = ET.Element('script')
wowheadScript.text = 'const whTooltips = {colorLinks: true, iconizeLinks: true, renameLinks: true};'
wowheadScript2 = ET.Element('script', attrib={'src': "https://wow.zamimg.com/widgets/power.js"})
head.append(wowheadScript)
head.append(wowheadScript2)
title = ET.Element('title')
title.text = "Publik's Mount Tracking"
head.append(title)
html.append(head)
body = ET.Element('body')
html.append(body)

shadowlandsHeader = ET.Element('h1')
shadowlandsHeader.text = "Shadowlands"
necrolordHeader = ET.Element('h1')
necrolordHeader.text = "Necrolord"
nightFaeHeader = ET.Element('h1')
nightFaeHeader.text = "Night Fae"
venthyrHeader = ET.Element('h1')
venthyrHeader.text = "Venthyr"
kyrianHeader = ET.Element('h1')
kyrianHeader.text = "Kyrian"

headers = [shadowlandsHeader, necrolordHeader, nightFaeHeader, kyrianHeader, venthyrHeader]

for header in headers:
    body.append(header)
    table = ET.Element('table', attrib={'class': 'foo'})
    body.append(table)
    headerRow = ET.Element('tr')
    nameHeader = ET.Element('th')
    nameHeader.text = "Rare Name"
    mountHeader = ET.Element('th')
    mountHeader.text = "Mount"
    headerRow.append(nameHeader)
    headerRow.append(mountHeader)
    table.append(headerRow)

    for rare in config["rares"][header.text.lower().replace(" ", "")]:
        tr = ET.Element('tr')
        table.append(tr)
        rareName = ET.Element('td')
        input = ET.Element('input', attrib={'type': 'checkbox', 'id': rare["name"]})
        label = ET.Element('label', atrrib={'for': rare["name"]})
        label.text = rare["name"]
        rareName.append(input)
        rareName.append(label)

        rareMount = ET.Element('td')
        url = "https://www.wowhead.com/item=" + str(rare["mountId"])
        rareMountLink = ET.Element('a', href=url)
        rareMountLink.text = rare["mount"]
        rareMount.append(rareMountLink)

        tr.append(rareName)
        tr.append(rareMount)


ET.ElementTree(html).write("index.html", encoding='unicode', method='html')