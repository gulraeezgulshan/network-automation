from jinja2 import Environment, FileSystemLoader
ENV = Environment(loader=FileSystemLoader('.'))
from devices import devices

template = ENV.get_template("template.j2")
output = template.render(devices=devices)
print(output)

with open("initial_configuration.txt", 'w') as f:
    f.writelines(output)



