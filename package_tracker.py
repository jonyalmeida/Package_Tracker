from flask import Flask, render_template, redirect
from .config import Configuration
from .app.shipping_form import ShippingForm
from flask_migrate import Migrate
from .models import db, Package

# app initialization and configuration
app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def root_endpoint():
    packages = Package.query.all()
    return render_template('package_status.html', packages=packages)


@app.route('/new_package', methods=['POST', 'GET'])
def new_package():
    form = ShippingForm()

    if form.is_submitted():

        data = form.data

        # creates Package model instance and stores in the database
        new_package = Package(sender=data['sender_name'],
                              recipient=data['receiver_name'],
                              origin=data['origin'],
                              destination=data['destination'],
                              location=data['origin'])
        db.session.add(new_package)
        db.session.commit()

        Package.advance_all_locations()

        return redirect('/')
    return render_template('shipping_request.html', form=form)
