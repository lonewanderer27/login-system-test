from flask import render_template, Blueprint

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
def blog():
    return render_template('index.html')