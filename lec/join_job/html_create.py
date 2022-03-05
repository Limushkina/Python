from calc.view import view_data
from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view

def create(devise = 1):
    style = 'style = "front-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '    <p {}>Temperature: {} c</p>\n'\
        .format(style, temperature_view(devise))
    html += '    <p {}>Wind_speed: {} m/s/</p>\n'\
        .format(style, wind_speed_view(devise))
    html += '    <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, pressure_view(devise))
    html += '    </body>\n</html>'

