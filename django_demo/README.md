# Django Blog Demo

Tiny Django app showing models, admin, migrations, and a public list view.

https://github.com/Drew-Woodz/flask-django-showcase

## Features

- `Post` model with title, body, timestamp

- Django admin to add/edit posts

- Public view that lists posts newest first

## Project layout

```text

django_demo/
├── manage.py
├── mysite/
│ ├── settings.py
│ ├── urls.py
│ └── ...
└── blog/
├── admin.py
├── models.py
├── views.py
└── templates/
└── blog/
└── post_list.html

```


## Setup

```bash

# from repo root, ensure venv is active
cd django_demo
pip install -r requirements.txt

# migrate database and create admin user
python manage.py migrate
python manage.py createsuperuser

# run
python manage.py runserver

```

Open http://127.0.0.1:8000
 for the list and http://127.0.0.1:8000/admin
 for the admin.

Notes

ORM: Post.objects.all() uses Django’s query API

Migrations: makemigrations then migrate handle schema changes

Next ideas

Add a detail page with path("post/<int:id>/", views.post_detail)

Add tests with pytest-django or manage.py test

Deploy to Render or PythonAnywhere


## License

MIT

