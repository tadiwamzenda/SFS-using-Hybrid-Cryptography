
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'registration.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Ensure its installed and "
            "on your PYTHONPATH environment variable?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
