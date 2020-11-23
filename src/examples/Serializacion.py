# Serializacion propia de python
import pickle
from src.examples import Persona

data = {"personas": []}

p1 = Persona.Persona("Lucas", [])
p2 = Persona.Persona("Juan", [])

p1.add_skill("Python")
p2.add_skill("Java")

data["personas"].append(p1)
data["personas"].append(p2)

with open('personas.pickle', 'wb') as file:
    pickle.dump(data, file)

print(data)

# Deserializacion python
with open('personas.pickle', 'rb') as file:
    data = pickle.load(file)

    for persona in data["personas"]:
        print(persona.nombre, persona.skills)

# Serializacion Json
import json

listP = []
p1 = Persona.Persona("Lucas", [])
p1.add_skill("Python")
p1.add_skill("C++")
p1.add_skill("JS")
p2 = Persona.Persona("Juan", [])
p2.add_skill("Java")
p2.add_skill("C#")
listP.append(p1)
listP.append(p2)

data = {
    "personas": listP
}

print(data)

with open('personas.json', 'w', encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2, default=Persona.Persona.to_json)

# Deserializacion JSON
def from_json(json_object):
    if '__class__' in json_object:
        if json_object['__class__'] == 'Persona.Persona':
            return Persona.Persona(**json_object['__value__'])
    return json_object


with open('personas.json', encoding="utf-8") as file:
    data = json.load(file, object_hook=from_json)

    for persona in data["personas"]:
        print(persona)