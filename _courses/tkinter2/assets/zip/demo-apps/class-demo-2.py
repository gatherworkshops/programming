
# CLASSES ###########################

class Person:

    first_name = None
    last_name = None
    phone = None
    instagram = None

    def __init__(self, first, last, phone=None, instagram=None):
        self.first_name = first
        self.last_name = last
        self.phone = phone
        self.instagram = instagram

    def __str__(self):
        template = 'Person: {} {} {} {}'
        output = template.format(
            self.first_name, 
            self.last_name, 
            self.phone or "None", 
            self.instagram or "None"
        )
        return output

    def get_name(self):
        return first_name + ' ' last_name





# FUNCTIONALITY #####################

marge = Person("Marge", "Simpson", "555-7890")
print(marge)

homer = Person("Homer", "Simpson")
print(homer)

bart = Person("Bart", "Simpson", "0226789023", "eatmyshorts")
print(bart)

lisa = Person("Lisa", "Simpson", instagram="treehugger42")
print(lisa)
print(lisa.get_name())

