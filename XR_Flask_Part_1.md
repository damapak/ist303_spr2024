<h1 style="text-align: center;">Flask Exercise: Part 1</h1>

<p style="text-align: center;">David Kallemeyn</p>
<p style="text-align: center;">Last Revised January 10, 2024</p>

Due: PDF with screenshot \
Assignment type: Individual

#### INSTRUCTIONS
Create a basic app in Flask by performing the following steps in order. Upload a pdf with a screenshot in canvas.

1) Create a directory named _App_ to store your application
2) Change your working directory to the _App_ directory: \
`cd App`
3) Create a virtual environment named _venv_: \
`py -m venv venv` or \
`python -m venv venv` (if no py launcher)
4) Activate your virtual environment (stay in your _App_ directory): 
    - windows: \
    `./venv/Scripts/Activate`
    - linux/mac: \
    `source venv/bin/activate`
5) Install flask in the virtual environment: \
`pip install flask`
6) Create a new file in the _App_ folder named _hello.py_ that contains the following code:

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```
7) Start your app: \
`flask --app hello.py run`

8) You should see a message that your server is running on an http address. Navigate to that address in your browser and confirm that it displays "Hello, World!" 
- > Take a screenshot of your app displaying the message in the browser to include with the submission.
10) Stop the app server with `ctrl + c`, then deactivate your virtual environment by typing `deactivate`

---
#### RESOURCES: 
You can read more details about this basic app and continue with the tutorial [here](https://flask.palletsprojects.com/en/2.3.x/quickstart/#a-minimal-application)