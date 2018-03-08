import os
from django.apps import apps
from django.core.management.base import BaseCommand, CommandError

User = apps.get_model('user', 'User')



def try_except(original_function):
    def new_function(*args, **kwargs):
        try:
            original_function(*args, **kwargs)
        except Exception as ex:
            print(ex)
    return new_function


class Command(BaseCommand):
    help = 'create super user'

    def add_arguments(self, parser):
        parser.add_argument('user', nargs='+', type=str)


    def handle(self, *args, **kwargs):
        self.create(**kwargs)

    @try_except
    def create(self, **kwargs):
        params = kwargs.get('user')

        try:
            user = User.objects.create(email=params[0])
            user.set_password(params[1])
            user.make_superuser()
        except Exception as ex:
            print(ex)



