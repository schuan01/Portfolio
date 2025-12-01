from flask import render_template
from flask import Blueprint

pages_bp = Blueprint('pages', __name__)

@pages_bp.route('/blog')
def blog():
    data = {
        'headTitle': 'BLog',
        'title': 'Blog',
        'subTitle': 'Blog',
    }
    return render_template("pages/blog.html",**data)

@pages_bp.route('/blog-details', methods=['GET', 'POST'])
def blogDetails():
    form = CommentForm()
    if form.validate_on_submit():
        flash('Your comment has been posted!', 'success')
        return redirect(url_for('pages.blogDetails'))
    data = {
        'headTitle': 'Blog Details',
        'breadcrumb': 'false',
        'form': form,
    }
    return render_template("pages/blogDetails.html", **data)

@pages_bp.route('/404')
def pageError():
    data = {
        'headTitle': '404',
        'breadcrumb': 'false',
        'footer': 'footer2',
    }
    return render_template("pages/pageError.html",**data)

@pages_bp.route('/portfolio')
def portfolio():
    data = {
        'headTitle': 'Portfolio',
        'title': 'Portfolio',
        'subTitle': 'Portfolio',
    }
    return render_template("pages/portfolio.html",**data)

@pages_bp.route('/portfolio-details')
def portfolioDetails():
    data = {
        'headTitle': 'Service',
        'title': 'List Style',
        'subTitle': 'List Style',
        'breadcrumb': 'false',
    }
    return render_template("pages/portfolioDetails.html",**data)
