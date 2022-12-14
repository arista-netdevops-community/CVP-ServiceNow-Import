"""Simple example to add nodes to Service now"""
import os
import pysnow
import requests
from urllib3.exceptions import InsecureRequestWarning
from dotenv import load_dotenv
from data import arista_networks, device_model, node_entry

load_dotenv()

INSTANCE = os.getenv("INSTANCE")
USER = os.getenv("SNOW_USER")
PASSWORD = os.getenv("SNOW_PASSWORD")
CVP_HOST = os.getenv("CVP_HOST")
CVP_TOKEN = os.getenv("CVP_TOKEN")


c = pysnow.Client(instance=INSTANCE, user=USER, password=PASSWORD)

# Suppress the warnings from urllib3
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
# Get CVP devices
headers = {"Authorization": f"Bearer {CVP_TOKEN}"}
dev = requests.get(
    url=f"{CVP_HOST}/cvpservice/inventory/devices?provisioned=false",
    headers=headers,
    verify=False,
    timeout=10,
)

devices = dev.json()

# build query for Arista Networks
qb = pysnow.QueryBuilder().field("name").equals("Arista Networks")

# Get all companies
companies = c.resource(api_path="/table/core_company")

# Query on Arista Networks
response = companies.get(query=qb)

# Set manufacturer from creation or update
if response.all():
    result = companies.update(query=qb, payload=arista_networks)
    manu = result.all()[0]
else:
    result = companies.create(payload=arista_networks)
    manu = result.all()[0]


### Get model category
qb = pysnow.QueryBuilder().field("name").equals("Network Gear")
category = c.resource(api_path="/table/cmdb_model_category")
response = category.get(query=qb)
cat = response.all()[0]


# Looping over devices and checking model existence
for device in devices:
    model_name = device["modelName"]
    qb = pysnow.QueryBuilder().field("name").equals(model_name)
    products = c.resource(api_path="/table/cmdb_hardware_product_model")
    response = products.get(query=qb)
    payload = device_model(model_name, manu["sys_id"], cat["sys_id"])

    # Create model if it does not exist
    if response.all():
        product_model = response.all()[0]
    else:
        result = products.create(payload=payload)
        product_model = result.all()[0]
        print(f"creating model {device['modelName']}")

    # Creating the actual devices!
    qb = pysnow.QueryBuilder().field("serial_number").equals(device["serialNumber"])
    device_search = c.resource(api_path="/table/cmdb_ci_netgear")
    response = device_search.get(query=qb)
    if response.all():
        print(f"{device['hostname']} exists")
    else:
        node = node_entry(
            device["hostname"],
            device["modelName"],
            device["version"],
            device["systemMacAddress"],
            device["serialNumber"],
            device["ipAddress"],
            manu["sys_id"],
            product_model["sys_id"],
        )
        products = c.resource(api_path="/table/cmdb_ci_netgear")
        products.create(payload=node)
        print(f"Created node: {device['hostname']}")
