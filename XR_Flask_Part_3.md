<h1 style="text-align: center;">Flask Exercise: Part 3</h1>

<p style="text-align: center;">David Kallemeyn</p>
<p style="text-align: center;">Last Revised January 2024</p>

Due: PDF with screenshots \
Assignment type: Individual \
Points: 40

#### USEFUL COMMANDS
As always, be sure to activate your virtual environment once you navigate to your project directory in the terminal:
  - windows: `./venv/Scripts/Activate`
  - linux/mac: `source venv/bin/activate`

How to run a flask app from the terminal:
```
flask --app FILENAME.py run
```

#### INSTRUCTIONS
Continue developing a basic app in Flask by adding a database connection and blog posting functionality.

You do not need to take screenshots as you go along. The screenshots needed can be done at the end of the project and are outlined at the end of the assignment in the Wrap-up section.



1) Start with the directory you used for Parts 1 and 2. Inside your project directory (likely named _App_), you should have the following directories:  _venv_, _static_ and _templates_. You should also have the _hello.py_ file in the main projcet directory. Rename your _hello.py_ file to **_main.py_.**

2) Reconfigure your default route to point to an index.html file. Do this by updating the default route ("/") in _main.py_ so that is reads:
```
@app.route('/')
def index():
    return render_template('index.html')
```
<div style="page-break-after: always;"></div>

3) In your templates folder, create a _index.html_ file and add the following text to the file:
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>MyBlog</title>
</head>
<body>
  <h1>Welcome to My Blog</h1>
</body>
</html>
```

4) Utilize css styling and a base.html as a template for your pages:
- navigate to your _static_ directory (which should be empty) and create a _css_ directory.
- in the _css_ directory, create a _stlye.css_ file that contains the following:
```
h1 {
  border: 2px #eee solid;
  color: brown;
  text-align: center;
  padding: 10px;
}
```
- in your templates directory, create a _base.html_ and place the following code in it (this one is long, you may want to use the XR_Flask_Part_3.md file on the course github repository or locate the code at the tutorial url provided later in this document to copy/paste it effectively):
```
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>{% block title %} {% endblock %}</title>
  </head>
  <body>
    <nav class="navbar navbar-expand-md navbar-light bg-light">
        <a class="navbar-brand" href="{{ url_for('index')}}">MyBlog</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
            <li class="nav-item active">
                <a class="nav-link" href="#">About</a>
            </li>
            </ul>
        </div>
    </nav>
    <div class="container">
        {% block content %} {% endblock %}
    </div>

  </body>
</html>
```
- replace the contents of your _index.html_ with:
```
{% extends 'base.html' %}

{% block content %}
    <h1>{% block title %} Welcome to My Blog {% endblock %}</h1>
{% endblock %}
```

## Proceed with the tutorial found at the url below, beginning with step 4:
### https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

### Note the following:
- when they mention the _flask_blog_ directory, the are referring to the main project directory, likely named _App_ if you are using the same directories as parts 1 and 2 of the assignment.
- whenever the tutorial mentions _app.py_, you are working in **_main.py_**. The code will be the same unless noted below.

### The following notes refer to the steps as numbered in the tutorial website. Use the adjustments below.

### Step 5
- you do not need to add `from werkzeug.exceptions import abort` to the main.py imports section. You can instead add abort to the list of Flask imports. So your imports will look like:
```
import sqlite3
from flask import Flask , render_template , redirect , url_for , request, abort
```

### Wrap-up and Submission
Once you have completed the tutorial, take screenshots of your app in the browser at the following pages:
- the default route that displays all the blog posts
- the new post screen (the /create route)
- a detailed view of a single post that you added (a numbered route, e.g. /3)
- the edit screen of a post with the warning message you see when attempting to delete a post displayed

You do not need to submit any more than what is listed above. You do not, for example, need to submit any screenshots of your code.

Your project directory should now look similar to the following (you do not need to screenshot yours): 

<img src="../projects/flask/rsc/dir.png" width="130"/>


Note that the _login.html_ and _welcome.html_ are left over from prior parts of the project, and are not currently utilized. In the _main.py_ script, the "login" and "welcome" routes are not accessed in any of the navigation (they would have to be manually typed to see them.)

> 3 points extra credit will be awarded if you can configure your blog to require a login prior to accessing any of the other functionality. Submit screenshot of your code or the code file for verification.
