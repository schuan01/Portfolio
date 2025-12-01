from flask import render_template, request, flash, redirect, url_for
from flask import Blueprint
from trydo_app.forms import ContactForm

home_bp = Blueprint('home', __name__)

@home_bp.route('/about')
def about():
    data = {
        'headTitle': 'Business',
        'footer': 'footer',
        'breadcrumb': 'False',
    }
    return render_template("home/about.html",**data)

@home_bp.route('/business')
def business():
    data = {
        'headTitle': 'Business',
        'footer': 'footer2',
        'breadcrumb': 'False',
    }
    return render_template("home/business.html",**data)


@home_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Handle form submission logic here (e.g., send email, save to db)
        flash('Your message has been sent!', 'success')
        return redirect(url_for('home.contact'))
    data = {
        'headTitle': 'Contact Us',
        'breadcrumb': 'false',
        'form': form,
    }
    return render_template("home/contact.html", **data)


@home_bp.route('/corporate-business')
def corporateBusiness():
    data = {
        'headTitle': 'Corporate Business',
        'header': 'False',
        'breadcrumb': 'False',
        'footer': 'footer2',
    }
    return render_template("home/corporateBusiness.html",**data)

@home_bp.route('/creative-agency')
def creativeAgency():
    data = {
        'headTitle': 'Creative Agency',
        'header': 'false',
        'breadcrumb': 'false',
        'footer': 'footer2',
    }
    return render_template("home/creativeAgency.html",**data)

@home_bp.route('/creative-portfolio')
def creativePortfolio():
    data = {
        'headTitle': 'Creative Portfolio',
        'breadcrumb': 'false',
        'header': 'false',
        'footer': 'footer2',
    }
    return render_template("home/creativePortfolio.html",**data)

@home_bp.route('/designer-portfolio')
def designerPortfolio():
    data = {
        'headTitle': 'Designer Portfolio',
        'header': 'false',
        'breadcrumb': 'false',
        'footer': 'footer2',
    }
    return render_template("home/designerPortfolio.html",**data)

@home_bp.route('/digital-agency')
def digitalAgency():
    data = {
        'headTitle': 'Digital Agency',
        'header': 'false',
        'breadcrumb': 'false',
        'footer': 'footer2',
    }
    return render_template("home/digitalAgency.html",**data)

@home_bp.route('/elements')
def elements():
    data = {
        'headTitle': 'Elements',
        'title': 'Elements',
        'subTitle': 'Elements',
    }
    return render_template("home/elements.html",**data)

@home_bp.route('/')
@home_bp.route('/index')
def index():
    return render_template("home/personalPortfolio.html")

@home_bp.route('/landing-creative-agency')
def landingCreativeAgency():
    data = {
        'headTitle': 'Creative Landing',
        'header': 'false',
        'breadcrumb': 'false',
    }
    return render_template("home/landingCreativeAgency.html",**data)

@home_bp.route('/landing-home-particles')
def landingHomeParticles():
    data = {
        'headTitle': 'Home Particles',
        'breadcrumb': 'false',
        'header': 'false',
        'footer': 'footer2',
    }
    return render_template("home/landingHomeParticles.html",**data)

@home_bp.route('/landing-personal-portfolio', methods=['GET', 'POST'])
def landingPersonalPortfolio():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Your message has been sent!', 'success')
        return redirect(url_for('home.landingPersonalPortfolio'))
    data = {
        'headTitle': 'Personal Portfolio Landing',
        'header': 'false',
        'footer': 'footer2',
        'breadcrumb': 'false',
        'form': form,
    }
    return render_template("home/landingPersonalPortfolio.html", **data)

@home_bp.route('/landing-personal-portfolio-02', methods=['GET', 'POST'])
def landingPersonalPortfolio02():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Your message has been sent!', 'success')
        return redirect(url_for('home.landingPersonalPortfolio02'))
    data = {
        'headTitle': 'Personal Portfolio Landing',
        'header': 'false',
        'breadcrumb': 'false',
        'footer': 'footer2',
        'form': form,
    }
    return render_template("home/landingPersonalPortfolio02.html", **data)

@home_bp.route('/main-demo')
def mainDemo():
    data = {
        'headTitle': 'Main Demo',
        'breadcrumb': 'false',
    }
    return render_template("home/mainDemo.html",**data)

@home_bp.route('/main-demo-dark')
def mainDemoDark():
    data = {
        'headTitle': 'Main Demo',
        'breadcrumb': 'false',
    }
    return render_template("home/mainDemoDark.html",**data)

@home_bp.route('/minimal-portfolio')
def minimalPortfolio():
    data = {
        'headTitle': 'Minimal Portfolio',
        'breadcrumb': 'false',
        'footer': 'footer2',
    }
    return render_template("home/minimalPortfolio.html",**data)

@home_bp.route('/paralax-home')
def paralaxHome():
    data = {
        'headTitle': 'Paralax Home',
        'breadcrumb': 'false',
    }
    return render_template("home/paralaxHome.html",**data)

@home_bp.route('/personal-portfolio', methods=['GET', 'POST'])
def personalPortfolio():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Your message has been sent!', 'success')
        return redirect(url_for('home.personalPortfolio'))
    data = {
        'headTitle': 'Personal Portfolio',
        'header': 'false',
        'footer': 'footer2',
        'breadcrumb': 'false',
        'form': form,
    }
    return render_template("home/personalPortfolio.html", **data)

@home_bp.route('/startup')
def startup():
    data = {
        'headTitle': 'Startup',
        'breadcrumb': 'false',
    }
    return render_template("home/startup.html",**data)

@home_bp.route('/studio-agency')
def studioAgency():
    data = {
        'headTitle': 'Studio Agency',
        'breadcrumb': 'false',
        'footer': 'footer2',
    }
    return render_template("home/studioAgency.html",**data)