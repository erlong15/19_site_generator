import markdown2
import json
import argparse
from jinja2 import Template


def read_config(config_file):
    with open(config_file, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def convert2html(article):
    with open(article.replace('md', 'html'), 'w') as html_file:
        html_file.write(markdown2.markdown_path(article))


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config',
                        help='JSON config file, default - config.json',
                        required=False, default='config.json')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    config = read_config(args.config)
    for article in config['articles']:
        convert2html('articles/{}'.format(article['source']))
