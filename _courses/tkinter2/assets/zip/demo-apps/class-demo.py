
# CLASSES ###########################

class Person:

    first_name = None
    last_name = None
    phone = None
    instagram = None

    def __init__(self, first_name, last_name=None, phone=None, instagram=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.instagram = instagram

    def __str__(self):
        template = 'Person: {} {} {} {}'
        output = template.format(self.first_name, self.last_name, self.phone, self.instagram)
        return output

    def get_name(self):
        return self.first_name + ' ' + self.last_name



# FUNCTIONALITY #########################

marge = Person("Marge")
print(marge)

homer = Person("Homer", "Simpson")
print(homer)

bart = Person("Bart", "Simpson", "555-0123")
print(bart)

lisa = Person("Lisa", "Simpson", instagram="treehugger42")
print(lisa)