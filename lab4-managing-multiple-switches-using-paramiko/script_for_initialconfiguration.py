from jinja2 import Environment, FileSystemLoader
ENV = Environment(loader=FileSystemLoader('.'))
from devices import switches

template = ENV.get_template("template.j2")
output = template.render(switches=switches)
print(output)

with open("initial_configuration_switch.txt", 'w') as f:
    f.writelines(output)



