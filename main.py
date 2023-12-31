import datetime
import pandas
import argparse
import os
from math import isnan
from dotenv import load_dotenv
from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape



def get_declination_year(age):
    residue = age % 10

    if residue == 1 and age % 100 != 11:
        return f'{age} год'

    if residue in [2, 3, 4] and not (age % 100 in [12, 13, 14]):
        return f'{age} года'

    return f'{age} лет'


def get_all_wine(path_xlsx_file):
    excel_data_df = pandas.read_excel(f'{path_xlsx_file}')
    all_wine_info = excel_data_df.to_dict(orient='records')

    categories_wine = defaultdict(list)
    for category in all_wine_info:
        for characteristic in category:
            if type(category[characteristic]) == float and isnan(category[characteristic]):
                category[characteristic] = '' 
        categories_wine[category['Категория']].append(category)
    
    return categories_wine 


if __name__ == '__main__':
    load_dotenv()
    path_to_file = os.environ['PATH_TO_FILE']
    current_year = datetime.datetime.now().year
    winery_age = current_year - 1920

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', 
                        type=str,
                        default=path_to_file, 
                        help='Путь до таблицы с данными')
    args = parser.parse_args()

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    wine_categories = get_all_wine(args.path)
    rendered_page = template.render(
        categories_wine=wine_categories,
        winery_age=get_declination_year(winery_age)
    )

    with open('index.html', 'w', encoding='utf8') as file:
        file.write(rendered_page)

    server = HTTPServer(('127.0.0.1', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()