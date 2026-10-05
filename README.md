# Django URL Shortener

A simple URL Shortener web application developed using Python and Django.

The application converts long URLs into short URLs and redirects users to the original URL when the shortened URL is visited.

## Features

- Enter a long URL
- Generate a random 10-character short URL
- Store URLs in a SQLite database
- Display all shortened URLs
- Redirect users from the short URL to the original URL
- URL validation using Django Forms

## Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS

## Project Structure

```text
URLShortener/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── url/
│   ├── migrations/
│   ├── templates/
│   │   └── index.html
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
└── README.md