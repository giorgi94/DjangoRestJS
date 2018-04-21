from django.utils.translation import activate, get_language




class Routes:

    def get_db_alias(self):
        lang = get_language()
        if lang == 'ka':
            return 'default'
        if lang == 'en':
            return 'en_db'
        return None

    def db_for_read(self, model, **hints):
        return self.get_db_alias()

    def db_for_write(self, model, **hints):
        return self.get_db_alias()