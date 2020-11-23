from src.examples import Persona
import json

def to_json(python_object):
    if isinstance(python_object, Persona.Persona):
        return {
            '__class__': 'Persona.Persona',
            '__value__': {
                'nombre': python_object.nombre,
                'skills': python_object.skills
            }
        }
    raise TypeError(repr(python_object) + ' is not JSON serializable')


data = {
    "personas": [
        Persona.Persona("Lucas", ["Python", "C++", "JS"]),
        Persona.Persona("Juan", ["Java", "C#"])
    ]
}

print(data)

with open('person2.json', 'w', encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2, default=to_json)


def from_json(json_object):
    if '__class__' in json_object:
        if json_object['__class__'] == 'Persona.Persona':
            return Persona.Persona(**json_object['__value__'])
    return json_object


with open('person2.json', encoding="utf-8") as file:
    data = json.load(file, object_hook=from_json)

    for persona in data["personas"]:
        print(persona)