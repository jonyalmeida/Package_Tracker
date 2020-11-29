from flask import Flask, render_template
from .config import Configuration
from .app.shipping_form import ShippingForm
from flask_migrate import Migrate
from .models import db

# app initialization and configuration
app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return '<h4>Package Tracker</h4>'


@app.route('/new_package', methods=['POST', 'GET'])
def new_package():
    form = ShippingForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('shipping_request.html', form=form)
