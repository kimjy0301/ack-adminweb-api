activate_this = (
    "C:/Users/KimJiYong/.virtualenvs/ACK_Python-wYgVXe1N/Scripts/activate_this.py"
)
exec(open(activate_this).read(), dict(__file__=activate_this))

import os
import sys
import site
from django.core.wsgi import get_wsgi_application


# Add the site-packages of the chosen virtualenv to work with
site.addsitedir("C:/Users/KimJiYong/.virtualenvs/ACK_Python-wYgVXe1N/Lib/site-packages")

# Add the app's directory to the PYTHONPATH
sys.path.append("C:/Work/ACK_Python")
sys.path.append("C:/Work/ACK_Python/config")

os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()
