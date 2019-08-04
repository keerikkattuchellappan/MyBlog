from app import blog

@blog.route('/')
@blog.route('/index')
def index():
    return "Hello, Chellappan!"
