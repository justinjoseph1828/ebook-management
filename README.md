# Ebook Management API

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/justinjoseph1828/ebook-management/tree/main
$ cd ebook
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ pip install virtualenv
$ python<version> -m venv <virtual-environment-name>
$ source <virtual-environment-name>/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

And the APIs can be checked using the consume.py file.
To run it do thr command "python consume.py"