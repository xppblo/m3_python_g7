from string import Template

aves_template = Template('''<h2>$nombre_espanol</h2>
                            <h2>$nombre_ingles</h2>
                            <img src="$imagen_url" alt="">
                         ''')

html_template = Template('''<!DOCTYPE html>
                            <html>
                            <head>
                            <title>Aves Chile</title>
                            </head>
                            <body>

                            <h1>Aves de chile</h1>

                            $body

                            </body>
                            </html>
                        ''')
