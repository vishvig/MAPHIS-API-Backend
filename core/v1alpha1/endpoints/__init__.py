from core import *
from utils import *

this_version = 'v1alpha1'
# this_version = os.path.abspath(os.getcwd()).split('/')[-2]
# this_version_module = importlib.import_module(f'core.{this_version}')


def api(module):
    return os.path.join(f'/{this_version}', module)
