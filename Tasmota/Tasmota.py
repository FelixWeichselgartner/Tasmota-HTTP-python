# one Tasmota device
# Doc: https://tasmota.github.io/docs/Commands/#management

import requests
from lxml import html
import json


class Tasmota:
    def __init__(self, ipv4):
        self.ipv4 = ipv4
        self.url = f'http://{self.ipv4}/'
        self.stream_open = False

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

    def get_stream_url(self):
        if not self.stream_open:
            r = requests.get(self.url)
            self.stream_open = True
        return f'http://{self.ipv4}:81/stream'

    def get_power_monitoring_attribute(self, attribute):
        """
        possible attributes are:
        Total, Yesterday, Today, Power, ApparentPower, ReactivePower, Factor, Voltage, Current
        """
        
        if 'Monitoring' in self.get_name():
            r = requests.get(self.url + f'cm?cmnd=Status%208')
            text = str(r.content)
            j = json.loads(text[2:-1])
            return j['StatusSNS']['ENERGY'][attribute]
        else:
            print('power monitoring not supported for this device')
            return None
