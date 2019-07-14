
from app import blog
import os

#blog.run()
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    blog.run(host='0.0.0.0', port=port)