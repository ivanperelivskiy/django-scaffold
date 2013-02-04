
import os
import sys


if __name__ == '__main__':
    sys.path.insert(0, os.path.abspath(
                    os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'src')))

    sys.path.insert(0, os.path.abspath(
                    os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'src', '{{ project_name }}')))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          '{{ project_name }}.system.conf.prod')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)