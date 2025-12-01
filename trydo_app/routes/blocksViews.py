from flask import render_template
from flask import Blueprint

blocks_bp = Blueprint('blocks', __name__)

@blocks_bp.route('/accordion')
def accordion():
    data = {
        'headTitle': 'Tab & Accordion',
        'title': 'Tab & Accordion',
        'subTitle': 'Tab & Accordion',
        'footer': 'footer2',
    }
    return render_template("blocks/accordion.html",**data)

@blocks_bp.route('/brand')
def brand():
    data = {
        'headTitle': 'Brand',
        'title': 'Brand',
        'subTitle': 'Brand',
    }
    return render_template("blocks/brand.html",**data)

@blocks_bp.route('/button')
def button():
    data = {
        'headTitle': 'Button',
        'title': 'Button',
        'subTitle': 'Button',
    }
    return render_template("blocks/button.html",**data)

@blocks_bp.route('/columns')
def columns():
    data = {
        'headTitle': 'Columns',
        'title': 'Columns',
        'subTitle': 'Columns',
    }
    return render_template("blocks/columns.html",**data)

@blocks_bp.route('/contact-form', methods=['GET', 'POST'])
def contactForm():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Your message has been sent!', 'success')
        return redirect(url_for('blocks.contactForm'))
    data = {
        'headTitle': 'Contact Form',
        'title': 'Contact Form',
        'subTitle': 'Contact Form',
        'form': form,
    }
    return render_template("blocks/contactForm.html", **data)

@blocks_bp.route('/counterup')
def counterup():
    data = {
        'headTitle': 'Counter',
        'title': 'Counter',
        'subTitle': 'Counter',
    }
    return render_template("blocks/counterup.html",**data)

@blocks_bp.route('/gallery')
def gallery():
    data = {
        'headTitle': 'Gallery',
        'title': 'Gallery',
        'subTitle': 'Gallery',
    }
    return render_template("blocks/gallery.html",**data)

@blocks_bp.route('/liststyle')
def liststyle():
    data = {
        'headTitle': 'List Style',
        'title': 'List Style',
        'subTitle': 'List Style',
    }
    return render_template("blocks/liststyle.html",**data)

@blocks_bp.route('/pricing-plan')
def pricingPlan():
    data = {
        'headTitle': 'Pricing Plan',
        'title': 'Pricing Plan',
        'subTitle': 'Pricing Plan',
    }
    return render_template("blocks/pricingPlan.html",**data)

@blocks_bp.route('/progressbar')
def progressbar():
    data = {
        'headTitle': 'Progress Bar',
        'title': 'Progress Bar',
        'subTitle': 'Progress Bar',
    }
    return render_template("blocks/progressbar.html",**data)

@blocks_bp.route('/team')
def team():
    data = {
        'headTitle': 'Team',
        'title': 'Team',
        'subTitle': 'Team',
    }
    return render_template("blocks/team.html",**data)

@blocks_bp.route('/testimonial')
def testimonial():
    data = {
        'headTitle': 'Testimonial',
        'title': 'Testimonial',
        'subTitle': 'Testimonial',
    }
    return render_template("blocks/testimonial.html",**data)

@blocks_bp.route('/video-popup')
def videoPopup():
    data = {
        'headTitle': 'Video Popup',
        'title': 'Video Popup',
        'subTitle': 'Video Popup',
    }
    return render_template("blocks/videoPopup.html",**data)
