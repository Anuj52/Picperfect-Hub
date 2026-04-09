# PicPerfect-Hub Django Project

Welcome to PicPerfectHub, an online platform dedicated to selling high-quality photographs.

## About

PicPerfectHub is designed to provide users with a seamless experience in discovering, purchasing, and downloading high-quality photographs for various purposes. Whether you're a photographer looking to showcase your work or a customer searching for the perfect image, PicPerfectHub aims to meet your needs.

## Requirements

- [asgiref==3.6.0](https://pypi.org/project/asgiref/3.6.0/)
- [Django==4.1.7](https://www.djangoproject.com/)
- [Pillow==9.4.0](https://python-pillow.org/)
- [sqlparse==0.4.3](https://pypi.org/project/sqlparse/0.4.3/)
- [tzdata==2022.7](https://pypi.org/project/tzdata/2022.7/)

## Installation

To get started with PicPerfectHub locally, follow these steps:

1. Clone the repository: `git clone https://github.com/Anuj52/Picperfect-Hub.git`
2. Navigate to the project directory: `cd Picperfect-Hub`
3. (Recommended) Create + activate a virtual environment:
   - Windows PowerShell: `python -m venv .venv` then `.venv\Scripts\Activate.ps1`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install dependencies: `python -m pip install -r requirements.txt`
5. Apply migrations: `python manage.py migrate`
6. (Optional) Create an admin user: `python manage.py createsuperuser`
7. Start the Django server: `python manage.py runserver`

## Environment variables (production)

When deploying with `DEBUG=False`, set at least:

- `DJANGO_SECRET_KEY` (required)
- `DJANGO_ALLOWED_HOSTS` (comma-separated, e.g. `example.com,.vercel.app`)
- `DJANGO_DEBUG=0`


