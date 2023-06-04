import os
import sys

from dotenv import load_dotenv


def _load_env_params():
    """Load environment parameters from env file"""
    dotenv_path = os.path.join(os.path.dirname(__file__), '../env/.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        raise FileNotFoundError(f'error: file {dotenv_path=} not found!')


def main():
    """Run administrative tasks."""

    _load_env_params()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
