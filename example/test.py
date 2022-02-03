from Tasmota.Tasmota import Tasmota
from time import sleep

ipv4 = "192.168.178.191"
dev = Tasmota(ipv4)
print(dev.get_name())
print(dev.check_output(2))
print(dev.set_output(2, 'on'))
sleep(10)
print(dev.set_output(2, 'off'))
