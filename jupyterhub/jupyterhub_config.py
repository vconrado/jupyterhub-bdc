# JupyterHub configuration
# based on: https://github.com/defeo/jupyterhub-docker
#           https://github.com/jupyterhub/jupyterhub-deploy-docker
import os

## Authenticator
# https://oauthenticator.readthedocs.io/en/latest/getting-started.html#gitlab-setup
# http://tljh.jupyter.org/en/latest/howto/auth/google.html
from oauthenticator.google import GoogleOAuthenticator
c.JupyterHub.authenticator_class = GoogleOAuthenticator

c.JupyterHub.authenticator_class.client_id = os.environ['GOOGLE_CLIENTID']
c.JupyterHub.authenticator_class.client_secret = os.environ['GOOGLE_CLIENT_SECRET']
c.JupyterHub.authenticator_class.oauth_callback_url = os.environ['GOOGLE_OAUTH_CALLBACK_URL']

## Docker spawner
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_CONTAINER']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
# See https://github.com/jupyterhub/dockerspawner/blob/master/examples/oauth/jupyterhub_config.py
c.JupyterHub.hub_ip = os.environ['HUB_IP']

## user data persistence
## see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan'
c.DockerSpawner.notebook_dir = notebook_dir
## ToDo: Define persistence per user
# c.DockerSpawner.volumes = { "jupyterhub-user-{username}": notebook_dir }
c.DockerSpawner.volumes = { "/data": {"bind": '/home/jovyan/work/shared', "mode": "ro"} }

# Server usage
c.Spawner.cpu_limit = 1
c.Spawner.mem_limit = '2G'

## Services
c.JupyterHub.services = [
    {
        'name': 'cull_idle',
        'admin': True,
        'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
    },
]
