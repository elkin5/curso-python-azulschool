class Persona:
    def __init__(self, nombre, skills):
        self.nombre = nombre
        self.skills = skills

    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)

    def to_json(object):
        if isinstance(object, Persona):
            return {
                '__class__': 'Persona.Persona',
                '__value__': {
                    'nombre': object.nombre,
                    'skills': object.skills
                }
            }
        raise TypeError(repr(object) + ' is not JSON serializable')

    def from_json(object):
        if '__class__' in object:
            if object['__class__'] == 'Persona.Persona':
                return Persona.Persona(**object['__value__'])
        return object