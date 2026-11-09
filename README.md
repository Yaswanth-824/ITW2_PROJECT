# School Management Portal

A Django coursework project with a public school website and separate student and teacher views. Students can see course information, assignments and grades. Teachers can manage attendance, assignments and grades.

## Run locally

Use Python 3.11 or 3.12. Run the following from the repository root in a Unix shell.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
export DJANGO_SECRET_KEY="$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/. Keep the signing key outside Git and reuse it between local sessions if you need existing sessions to stay valid.

## Code map

- `project_ITW_sem3/` holds project settings and routes.
- `Main/` contains shared profiles and account functionality.
- `student/` and `teacher/` hold role-specific models and views.
- `templates/` and `static/` contain the Django templates and frontend assets.

The templates use Django routes and context. The current frontend needs Django to render its pages.
