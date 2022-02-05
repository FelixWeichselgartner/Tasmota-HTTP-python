from Tasmota import Tasmota
from time import sleep

ipv4 = "192.168.178.194"
dev = Tasmota(ipv4)
print(dev.get_name())
print(dev.get_power_monitoring_attribute('Voltage'))
