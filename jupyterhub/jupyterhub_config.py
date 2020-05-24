import os

c = get_config()

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.container_image = os.environ['DOCKER_NOTEBOOK_IMAGE']

# Networking
network_name = os.environ['DOCKER_NETWORK_NAME']
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = network_name
c.DockerSpawner.extra_host_config = { 'network_mode': network_name }

## User containers will access hub by container name on the Docker network
c.JupyterHub.hub_ip = 'bdc-jupyterhub'
c.JupyterHub.hub_port = 8080

# c.JupyterHub.services = [
#     {
#         'name': 'cull_idle',
#         'admin': True,
#         'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
#     },
# ]

# mapping rules
# c.Spawner.default_url = '/bdc/lab'

# auth
# https://oauthenticator.readthedocs.io/en/latest/getting-started.html#gitlab-setup
# http://tljh.jupyter.org/en/latest/howto/auth/google.html
from oauthenticator.google import GoogleOAuthenticator
c.JupyterHub.authenticator_class = GoogleOAuthenticator

c.JupyterHub.authenticator_class.client_id = "61086726892-0lqd6s4lka472ct2aqljb5fsgrdpsv6s.apps.googleusercontent.com"
c.JupyterHub.authenticator_class.client_secret = "o-O0tJunve8wKr3P7bw_8L6O"
c.JupyterHub.authenticator_class.oauth_callback_url = "http://localhost:8000/hub/oauth_callback"
