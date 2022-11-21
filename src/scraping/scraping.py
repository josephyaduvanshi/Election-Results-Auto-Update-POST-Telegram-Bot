import re
import requests
from lxml import etree
from bs4 import BeautifulSoup


class ScrapingMethods:

    @staticmethod
    def get_data_by_class_name(url: str, class_name: str):
        response = requests.get(url)
        print("called")
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.findAll(class_=class_name)

    @staticmethod
    def get_data_by_tag_name(url: str, tag_name: str):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup.findAll(tag_name))
        return soup.findAll(tag_name)

    @staticmethod
    def get_data_by_id(url: str, id: str):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.findAll(id=id)

    @staticmethod
    def get_data_by_css_selector(url: str, css_selector: str):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.select(css_selector)

    @staticmethod
    def get_data_by_xpath(url: str, xpath: str):
        response = requests.get(url)
        tree = etree.HTML(response.content)
        return tree.xpath(xpath)

    @staticmethod
    def get_data_by_regex(url: str, regex: str):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.findAll(text=re.compile(regex))

    @staticmethod
    def get_data_by_regex_group(url: str, regex: str):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.findAll(text=re.compile(regex))

    @staticmethod
    def extract_data_by_regex(data, first: str, last: str):
        regex = f'{first}(.*?){last}'
        return re.findall(regex, data)

    @staticmethod
    def extract_data_by_class_name_from_string(string: str, class_name: str):
        soup = BeautifulSoup(string, 'html.parser')
        return soup.findAll(class_=class_name)

    @staticmethod
    def clean_candidate_type(data):
        g = ScrapingMethods.extract_data_by_class_name_from_string(str(data), "candidate-party-name")
        h = g.__str__().replace('<div class="candidate-party-name">', '')
        i = re.sub('<[^>]*>', '', h).replace('  ', '').replace('\'', '').replace('[', '').replace(']', '').replace("\n",
                                                                                                                   "")
        p = i.split(',')
        return p
