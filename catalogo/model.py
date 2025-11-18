class Composition:
    def __init__(self, autor_list_id, composition_id, title, publication_year, publisher, catalog_id, isbn_number):
        self.autors_id = autor_list_id  # list of author ids
        self.composition_id = composition_id  # int or str
        self.title = title  # str
        self.publication_year = publication_year  # int
        self.publisher = publisher  # str
        self.catalog_id = catalog_id  # list or id
        self.isbn_number = isbn_number  # str

    def to_dict(self):
        return {
            'autors_id': self.autors_id,
            'composition_id': self.composition_id,
            'title': self.title,
            'catalog_details': self.catalog_id,
            'publication_year': self.publication_year,
            'publisher': self.publisher,
            'isbn_number': self.isbn_number
        }

class Autor:
    def __init__(self, autor_id, name):
        self.autor_id = autor_id  # int
        self.name = name  # str

    def to_dict(self):
        return {
            'autor_id': self.autor_id,
            'name': self.name
        }

class Copies:
    def __init__(self, copy_id, composition_id, availability_status):
        self.copy_id = copy_id  # int
        self.composition_id = composition_id  # int
        self.availability_status = availability_status  # str (e.g., 'available', 'loaned', etc.)

    def to_dict(self):
        return {
            'copy_id': self.copy_id,
            'composition_id': self.composition_id,
            'availability_status': self.availability_status
        }

class Catalog_Details:
    def __init__(self, catalog_id, themes, languages):
        self.catalog_id = catalog_id  # int
        self.themes = themes  # list of str
        self.languages = languages # list of str

    def to_dict(self):
        return {
            'catalog_id': self.catalog_id,
            'themes': self.themes,
            'languages': self.languages
        }