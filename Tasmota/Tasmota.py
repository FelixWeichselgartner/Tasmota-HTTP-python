# one Tasmota device

import requests
from lxml import html


class Tasmota:
    def __init__(self, ipv4):
        self.ipv4 = ipv4
        self.url = f'http://{self.ipv4}/'

    def _get_from_xpath(self, x):
        r = requests.get(self.url + '')
        tree = html.fromstring(r.content)
        c = tree.xpath(f'{x}/text()')
        return c

    def get_name(self):
        text = self._get_from_xpath('/html/body/div/div[1]/h3')[0]
        return str(text)

    def check_output(self, number):
        r = requests.get(self.url + f'cm?cmnd=Power{number}%20')
        return r.content

    def set_output(self, number, state):
        r = requests.get(self.url + f'cm?cmnd=Power{number}%20{state}')
        return r.content
