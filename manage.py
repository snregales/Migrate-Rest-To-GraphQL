#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # This allows easy placement of apps within the interior
    # Migrate-Rest-To-GraphQL directory.
    current_path: str = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(current_path, "src"))

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
