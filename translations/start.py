import os
import shutil
import json
from translation import Translation

def read_languages(filename = "languages.txt"):
    lang_list = []
    with open(filename) as languages_file:
        for language in languages_file:
            lang_list.append(language.strip())
    return lang_list

def create_folder_tree(package_group):
    try:
        shutil.rmtree("target")
    except FileNotFoundError: pass
    os.makedirs("target\\jcr_root\\" + package_group)
    os.makedirs("target\\META-INF\\vault")

def read_params(filename = "params.json"):
    with open(filename) as param_file:
        return json.load(param_file)

def generate_nodes(translations, template_path = "templates\\node_template.txt"):
    with open(template_path) as node_template_file:
        node_template = node_template_file.read()
        nodes = ""
        for node in translations.translations:
            nodes += generate_node(node, node_template)
        return nodes

def generate_node(translation, template):
    node = template.format(name = translation.get("name", translation.get("key")),
        key = translation.get("key"), message = translation.get("message"))
    return node

def ganerate_translation_for_countries(package_group, node, langs, template = "templates\\parent_node.txt"):
    with open(template) as template_file:
        template_str = template_file.read()
    for lang in langs:
        with open("target\\jcr_root\\" + package_group + "\\" + lang + ".xml", "w") as file:
            file.write(template_str.format(language = lang, nodes = node))

def generate_package_info(translations, template = "templates\\package_properties.txt"):
    with open(template) as template_file:
        template_str = template_file.read()
    with open("target\\META-INF\\vault\\properties.xml", "w") as file:
        file.write(template_str.format(package_name = translations.package_name, package_group = translations.package_group))

def generate_filters(translations, languages, template = "templates\\filter_template.txt"):
    with open(template) as template_file:
        template_str = template_file.read()
    filters_body = ""
    for lang in languages:
        for translate in translations.translations:
            filters_body += '<filter root="{0}/{1}/{2}" mode="update"/>\n'.format(
                translations.package_group.replace(".", "/"), lang, translate.get("name", translate.get("key")))
    with open("target\\META-INF\\vault\\filter.xml", "w") as file:
        file.write(template_str.format(filters = filters_body))

def main():
    languages = read_languages()
    translations = Translation(read_params())
    create_folder_tree(translations.package_group.replace(".", "\\"))

    nodes = generate_nodes(translations)

    ganerate_translation_for_countries(translations.package_group.replace(".", "\\"), nodes, languages)
    generate_package_info(translations)
    generate_filters(translations, languages)

main()
