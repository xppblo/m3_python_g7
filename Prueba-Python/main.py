from api_get import get_aves
from template import aves_template, html_template

aves_info = get_aves()

def aves_chile():
    aves_html = ''
    for aves in aves_info:
        aves_chile = aves_template.substitute(nombre_espanol = aves['name']['spanish'],nombre_ingles = aves['name']['english'],imagen_url = aves['images']['main'])
        aves_html += aves_chile
    
    html = html_template.substitute(body = aves_html)
    
    with open('Prueba-Python/aves_chile.html', 'w', encoding="utf-8") as f:
        f.write(html)

aves_chile()
