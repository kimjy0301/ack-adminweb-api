import os
import sys
import site
from django.core.wsgi import get_wsgi_application


# Pipenv 가상환경 경로 = "C:/Users/User/.virtualenvs/ack-adminweb-api-cTDx-PNN

activate_this = (
    "C:/Users/User/.virtualenvs/ack-adminweb-api-cTDx-PNN/Scripts/activate_this.py"
)
exec(open(activate_this).read(), dict(__file__=activate_this))


# Add the site-packages of the chosen virtualenv to work with
site.addsitedir(
    "C:/Users/User/.virtualenvs/ack-adminweb-api-cTDx-PNN/Lib/site-packages"
)

# Add the app's directory to the PYTHONPATH 프로젝트경로 추가
sys.path.append("C:/Work/ACK_Python")
sys.path.append("C:/Work/ACK_Python/config")

os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()
