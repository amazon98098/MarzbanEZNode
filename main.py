import random
import string

from hcloud import Client
from hcloud.images import Image
from hcloud.server_types import ServerType
from hcloud.locations import Location

TKCLOUD = input("Please Enter Token: ")

client = Client(
    token=TKCLOUD,  # Please paste your API token here
    application_name="my-app",
    application_version="v1.0.0",
)


def random_node_name(prefix="node"):
    import random, string
    rand = ''.join(random.choices(string.ascii_lowercase, k=3))
    return f"{prefix}-{rand}"


node_random_name = random_node_name()

for i in range(1, 11):
    # Create a server named my-server
    response = client.servers.create(
        name=node_random_name + "-0" + str(i),
        server_type=ServerType(name="cx23"),
        image=Image(name="357033020"),
        location=Location(name="fsn1")
    )

    server = response.server

# List your servers
servers = client.servers.get_all()
for server in servers:
    print(server.public_net.ipv4.ip)

