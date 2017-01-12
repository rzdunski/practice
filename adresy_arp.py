#!/usr/bin/python

from subprocess import call, check_output
import re

bash_cmd = "sudo arp-scan -l"
result = check_output(['bash', '-c', bash_cmd])
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
pattern_re = re.compile(pattern)
ip_address = pattern_re.findall(result)

for ip in ip_address:
    print ip
