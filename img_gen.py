def code_img(code):
    keywords = ['begin', 'end.', 'end;', 'end', 'var', 'uses', 'program']

    img = ''
    strs = code.split('\n')
    y = 20
    for i in strs:
        for j in keywords:
            if i.lower().find(j) != -1:
                i = i.lower().replace(j, f'<tspan style="font-weight: bold;">{j}</tspan>')
            
        img += f'<text class="txt1" x="10" y="{y}" fill="black" xml:space="preserve">{i}</text>'
        y += 20

    img = f'''<svg version="1.1"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    xmlns:ev="http://www.w3.org/2001/xml-events"
    width="500px" height="{y}px">
    <style>
    .txt1 {{
    font-size: 10pt;
    font-family: Courier New, monospace;
    fill: "black";
    background: "white";
    }}
    </style>'''+img+'</svg>'
    return img

def result_img(result):
    img = ''
    strs = result.split('\n')
    y = 20
    for i in strs:   
        img += f'<text class="txt" x="10" y="{y}" xml:space="preserve">{i}</text>'
        y += 20
    
    img = f'''<svg version="1.1"
    baseProfile="full"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    xmlns:ev="http://www.w3.org/2001/xml-events"
    width="570px" height="{y}px">
    <style>
    .txt {{
    font-size: 10pt;
    font-family: Courier New, monospace;
    fill: #fff;
    }}
    </style>
    <rect x="0" y="0" width="400px" height="{y}px" fill="black" />'''+img+'</svg>'
    return img
