from PIL import ImageDraw
from PIL import Image
from PIL import ImageFont
from PIL import ImageColor

import pandas as pd

import os
import json

config = json.load(open('config.json'))

def drawImage(data):
    print("Generating file for: " + data[0])

    # font
    fontConfig = config['font_config']
    font = ImageFont.truetype(fontConfig['font_path'], fontConfig['font_size'])


    # load templates
    templates = []
    for template in config['templates']:
        templates.append(Image.open(config['template_path'] + template + config['template_format']))
    # generate image
    
    for index, name in enumerate(data):
        label = config['labels'][index]
        for i, y in enumerate(config['templates']):
            if(y == label['template']):
                drawer = ImageDraw.Draw(templates[i])
                drawer.text((label['position_x'], label['position_y']), f"{name}", font=font, fill=ImageColor.getrgb(fontConfig['color']))

    
    templates[0].save(os.path.join(config['output_dir'], data[0] + config['output_format']),save_all=True, append_images=templates[1:])

    print("File generated for: " + data[0] + config['output_format'] + "\n ======================")


def start():
    data = pd.read_excel(config['data_path'])
    for i in data.values:
        drawImage(i)

    

