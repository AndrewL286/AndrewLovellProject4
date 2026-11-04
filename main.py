from nicegui import ui
mass_metros = []
ohio_metros = []
try:
    text_file = open('RentPerSquareFootAug2026 (2).csv', 'r', encoding='utf-8')
    lines = text_file.readlines()
    for line in lines[2:]:
        line = line.strip()
        if line == "":
            continue
        parts = line.split(';')
        if len(parts) < 5:
            continue
        name = parts[0]
        val_str = parts[2]
        year_ago_str = parts[4]
        if val_str == "" or year_ago_str == "":
            continue
        try:
            value = float(val_str)
            year_ago = float(year_ago_str)
        except ValueError:
            continue
        if ", MA" in name and len(mass_metros) < 8:
            mass_metros.append([name, value, year_ago])
        elif ", OH" in name and len(ohio_metros) < 8:
            ohio_metros.append([name, value, year_ago])
except FileNotFoundError:
    print("No Data")
#Lines 4-29 are going there both MA and OH to find all metros and data for them.
(ui.label("Massachusetts Metros").style("font-size: 130%; font-weight: bold; margin-top: 10px;"))
svg_width = 850
svg_height = 320
ma = f'<svg width="{svg_width}" height="{svg_height}" style="background: #ffffff; border: 1px solid #ddd; border-radius: 6px;">'
ma += '<line x1="220" y1="20" x2="220" y2="280" stroke="black" stroke-width="2"/>'
ma += '<line x1="220" y1="280" x2="820" y2="280" stroke="black" stroke-width="2"/>'

ma_max = 1
for item in mass_metros:
    if item[1] > ma_max:
        ma_max = item[1]

for part in range(len(mass_metros)):
    name = mass_metros[part][0]
    value = mass_metros[part][1]
    year_ago = mass_metros[part][2]
    y_pos = 30 + (part * 30)
    bar_width = (value / ma_max) * 550
    if value > year_ago:
        color = "green"
    else:
        color = "red"
    ma += f'<text x="210" y="{y_pos + 18}" text-anchor="end" font-size="12" fill="#333">{name}</text>'
    ma += f'<rect x="220" y="{y_pos}" width="{bar_width}" height="22" fill="{color}" rx="3" />'
    ma += f'<text x="{225 + bar_width}" y="{y_pos + 16}" font-size="12" font-weight="bold" fill="#333">${value:.0f}</text>'
#Lines 31-55 are building the graph for the MA metros.
ma += '</svg>'
ui.html(ma)
ui.label("Ohio Metros").style("font-size: 130%; font-weight: bold; margin-top: 20px;")
oh = f'<svg width="{svg_width}" height="{svg_height}" style="background: #ffffff; border: 1px solid #ddd; border-radius: 6px;">'
oh += '<line x1="220" y1="20" x2="220" y2="280" stroke="black" stroke-width="2"/>'
oh += '<line x1="220" y1="280" x2="820" y2="280" stroke="black" stroke-width="2"/>'

oh_max = 1
for item in ohio_metros:
    if item[1] > oh_max:
        oh_max = item[1]
for part in range(len(ohio_metros)):
    name = ohio_metros[part][0]
    value = ohio_metros[part][1]
    year_ago = ohio_metros[part][2]
    y_pos = 30 + (part * 30)
    bar_width = (value / oh_max) * 550
    if value > year_ago:
        color = "green"
    else:
        color = "red"
    oh += f'<text x="210" y="{y_pos + 18}" text-anchor="end" font-size="12" fill="#333">{name}</text>'
    oh += f'<rect x="220" y="{y_pos}" width="{bar_width}" height="22" fill="{color}" rx="3"/>'
    oh += f'<text x="{225 + bar_width}" y="{y_pos + 16}" font-size="12" font-weight="bold" fill="#333">${value:.0f}</text>'
#Lines 57-80 is building the graph for OH metros.
oh += '</svg>'
ui.html(oh)
ui.run()