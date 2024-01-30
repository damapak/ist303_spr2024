<h1 style="text-align: center;">Flask Exercise: Part 2</h1>

<p style="text-align: center;">David Kallemeyn</p>
<p style="text-align: center;">Last Revised January 2024</p>

Due: PDF with screenshot \
Assignment type: Individual

#### INSTRUCTIONS
Continue developing a basic app in Flask by adding html templating and login functionality.

1) Start with the directory you created for Part 1. Create two new folders inside your _App_ directory: _static_ and _templates_
2) In the _templates_ folder, create a file named "login.html". Add html code to create your template. You can find the login template at: https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/#add-a-template-for-the-login-page

3) Update the import line in your existing _hello.py_ file so that it reads: \
`from flask import Flask , render_template , redirect , url_for , request`

4) Then, add the following code to your existing _hello.py_ file (after the existing code):
```
# Route for handling the login page logic (user: admin, pw: admin)
@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    if request.form['username'] != 'admin' or request.form['password'] != 'admin':
      error = 'Invalid Credentials. Please try again.'
    else:
      return redirect(url_for('welcome'))
  return render_template('login.html', error=error)
```
The above code creates a /login route and that the only acceptable user name and passwor are "admin".

5) Now we need something to do upon successful login. We will setup a /welcome route to display a message upon successful login. Add the following code to your existing _hello.py_ file:
```
@app.route("/welcome")
def welcome():
  error = None
  return render_template('welcome.html', error=error)
```
6) In your _templates_ folder, create another html file called "welcome.html". Add your desired html templating, such as a message to display. You can use the login.html file to see how to display messages or search the web for a basic html file.
7) Activate your virtual environment (from your _App_ directory): 
    - windows: \
    `./venv/Scripts/Activate`
    - linux/mac: \
    `source venv/bin/activate`

8) Start your app: \
`flask --app hello.py run`

9) You should see a message that your server is running on an http address. Navigate to http://localhost:5000/login

- > Be sure to screenshot your login page, the welcome page, and the login page with invalid credentials entered to include with the submission.

10) Stop the app server with `ctrl + c`, then deactivate your virtual environment by typing `deactivate`

