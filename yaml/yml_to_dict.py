#!/usr/bin/env python
# @author      : ash (nevernew@mail.ru)
# @created     : 13/08/2019
# @description : Parse yml to dict

import yaml

y = yaml.load(open("example.yml"), Loader=yaml.SafeLoader)

print(y)
print(type(y))



