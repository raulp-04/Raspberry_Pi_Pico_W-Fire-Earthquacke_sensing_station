def html_too_hot():
    return """<!DOCTYPE html>
<html>
<head>
    <title>Monitorizare RPi Pico W</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body {
            background-color: red;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 40px;
        }
        h1 {
            font-size: 2em;
        }
    </style>
</head>
<body>
    <h1>THERE IS A FIRE</h1>
</body>
</html>"""

def html_earthquake():
    return """<!DOCTYPE html>
<html>
<head>
    <title>Monitorizare RPi Pico W</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body {
            background-color: orange;
            color: black;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 40px;
        }
        h1 {
            font-size: 2em;
        }
    </style>
</head>
<body>
    <h1>EARTHQUAKE DETECTED</h1>
</body>
</html>"""

def generate_html(temp, hum, is_vibration):
    if temp > 40:
        return html_too_hot()
    elif is_vibration:
        return html_earthquake()
    else:
        return f"""<!DOCTYPE html>
<html>
<head>
    <title>Monitorizare RPi Pico W</title>
    <meta http-equiv="refresh" content="2">
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            color: #333;
            text-align: center;
            padding: 40px;
        }}
        h1 {{
            color: #0066cc;
            margin-bottom: 30px;
        }}
        p {{
            font-size: 1.5em;
            margin: 20px 0;
            background-color: #ffffff;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.1);
            display: inline-block;
        }}
    </style>
</head>
<body>
    <h1>Date de la senzori</h1>
    <p>Temperatura: {temp}C</p>
    <p>Umiditate: {hum}%</p>
</body>
</html>"""