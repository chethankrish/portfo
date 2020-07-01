from flask import Flask
from flask import render_template, url_for, request, redirect
import csv

app = Flask ( __name__ )


@app.route ( '/' )
def my_home():
    return render_template ( 'index.html' )


@app.route ( '/<string:page_name>' )
def html_page(page_name):
    return render_template ( page_name )


def write_to_db(data):
    with open ( 'database.csv', newline='', mode= 'a' ) as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        rows = [email, subject, message]
        csvwriter = csv.writer ( database )
        csvwriter.writerows ( [rows] )


@app.route ( '/submit_form', methods=['POST', 'GET'] )
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict ()
        write_to_db ( data )
        return redirect ( '/thankyou.html' )


