import json
import os
import shutil

# Config Path
json_file_path = 'C:\\Users\\Tea\\\Downloads\\svg_icons.json'
# Folder Path
icons_folder = 'C:\\Users\\Tea\\Documents\icons'

if not os.path.exists(icons_folder):
    os.makedirs(icons_folder)


def create_svg_file(glyph_data, folder):
    svg_content = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {glyph["svg"]["width"]} {glyph["svg"]["width"]}">' f'<path d="{glyph["svg"]["path"]}"/>' '</svg>'

    file_path = os.path.join(folder, f'{glyph["css"]}.svg')

    with open(file_path, 'w') as svg_file:
        svg_file.write(svg_content)
        print(f'SVG {glyph["css"]} has been created.')

with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

for glyph in data['glyphs']:
    create_svg_file(glyph, icons_folder)

print("All icons have been processed and saved.")

shutil.make_archive(icons_folder, 'zip', icons_folder)

print("The icons folder has been archived.")