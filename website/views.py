from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# url_prefix in init.py is what determines
# what goes before what is inside these parentheses
@views.route('/')
def home():
    return render_template('home.html')
    # header 1 HTML "Test" is the header

# defined a blueprint and specified the routes (URLs) that belong to it





