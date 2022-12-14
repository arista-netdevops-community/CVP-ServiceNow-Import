"""Simple file for functions and data"""
arista_networks = {
    "country": "USA",
    "city": "Santa Clara",
    "stock_symbol": "ANET",
    "sys_class_name": "core_company",
    "manufacturer": "true",
    "street": "5453 Great America Pkwy",
    "vendor": "true",
    "contact": "https://www.arista.com/en/support/customer-support",
    "state": "CA",
    "zip": "95054",
    "website": "www.arista.com",
    "phone": "1 (866) 476-0000",
    "name": "Arista Networks",
    "customer": "false",
    "primary": "false",
}


def device_model(name: str, manu_value: str, category: str) -> dict:
    """Function to generate model structure"""
    model = {
        "type": "Generic",
        "sys_domain_path": "/",
        "name": name,
        "status": "In Production",
        "sys_class_name": "cmdb_hardware_product_model",
        "manufacturer": manu_value,
        "model_number": name,
        "cmdb_model_category": category,
        "asset_tracking_strategy": "leave_to_category",
    }
    return model


# We could use kwargs here but I tried to keep this simple
def node_entry(
    name: str,
    model: str,
    version: str,
    mac: str,
    serial: str,
    ip_address: str,
    vendor: str,
    product_model: str,
) -> dict:
    """Function to generate device structure"""
    device = {
        "can_switch": "true",
        "operational_status": "1",
        "can_partitionvlans": "true",
        "firmware_manufacturer": vendor,
        "sys_domain_path": "/",
        "firmware_version": version,
        "sys_class_name": "cmdb_ci_netgear",
        "manufacturer": vendor,
        "vendor": vendor,
        "can_route": "true",
        "model_number": model,
        "serial_number": serial,
        "device_type": "router",
        "name": name,
        "mac_address": mac,
        "ip_address": ip_address,
        "model_id": product_model,
    }
    return device

# List of devices for offline testing
devices = [
    {
        "modelName": "cEOSLab",
        "internalVersion": "4.28.1F",
        "systemMacAddress": "00:1c:73:b0:d5:01",
        "bootupTimestamp": 0,
        "version": "4.28.1F",
        "architecture": "",
        "internalBuild": "",
        "hardwareRevision": "",
        "domainName": "atd.lab",
        "hostname": "spine1",
        "fqdn": "spine1.atd.lab",
        "serialNumber": "spine1",
        "deviceType": "eos",
        "danzEnabled": False,
        "mlagEnabled": False,
        "streamingStatus": "active",
        "parentContainerKey": "container_1d62446c-7ead-4788-a1a1-8250362031de",
        "status": "Registered",
        "complianceCode": "0000",
        "complianceIndication": "",
        "ztpMode": False,
        "unAuthorized": False,
        "ipAddress": "192.168.0.10",
    },
    {
        "modelName": "cEOSLab",
        "internalVersion": "4.28.1F",
        "systemMacAddress": "00:1c:73:b7:d5:01",
        "bootupTimestamp": 0,
        "version": "4.28.1F",
        "architecture": "",
        "internalBuild": "",
        "hardwareRevision": "",
        "domainName": "atd.lab",
        "hostname": "host2",
        "fqdn": "host2.atd.lab",
        "serialNumber": "host2",
        "deviceType": "eos",
        "danzEnabled": False,
        "mlagEnabled": False,
        "streamingStatus": "active",
        "parentContainerKey": "container_2cbfe3d7-77a1-4bb4-b51b-278c56cdc9a3",
        "status": "Registered",
        "complianceCode": "0000",
        "complianceIndication": "",
        "ztpMode": False,
        "unAuthorized": False,
        "ipAddress": "192.168.0.17",
    },
    {
        "modelName": "cEOSLab",
        "internalVersion": "4.28.1F",
        "systemMacAddress": "00:1c:73:b3:d5:01",
        "bootupTimestamp": 0,
        "version": "4.28.1F",
        "architecture": "",
        "internalBuild": "",
        "hardwareRevision": "",
        "domainName": "atd.lab",
        "hostname": "leaf2",
        "fqdn": "leaf2.atd.lab",
        "serialNumber": "leaf2",
        "deviceType": "eos",
        "danzEnabled": False,
        "mlagEnabled": False,
        "streamingStatus": "active",
        "parentContainerKey": "container_12463e1d-8af6-43fa-986a-e4e249fd62df",
        "status": "Registered",
        "complianceCode": "0000",
        "complianceIndication": "",
        "ztpMode": False,
        "unAuthorized": False,
        "ipAddress": "192.168.0.13",
    },
    {
        "modelName": "cEOSLab",
        "internalVersion": "4.28.1F",
        "systemMacAddress": "00:1c:73:b4:d5:01",
        "bootupTimestamp": 0,
        "version": "4.28.1F",
        "architecture": "",
        "internalBuild": "",
        "hardwareRevision": "",
        "domainName": "atd.lab",
        "hostname": "leaf3",
        "fqdn": "leaf3.atd.lab",
        "serialNumber": "leaf3",
        "deviceType": "eos",
        "danzEnabled": False,
        "mlagEnabled": False,
        "streamingStatus": "active",
        "parentContainerKey": "container_12463e1d-8af6-43fa-986a-e4e249fd62df",
        "status": "Registered",
        "complianceCode": "0000",
        "complianceIndication": "",
        "ztpMode": False,
        "unAuthorized": False,
        "ipAddress": "192.168.0.14",
    },
    {
        "modelName": "cEOSLab",
        "internalVersion": "4.28.1F",
        "systemMacAddress": "00:1c:73:b5:d5:01",
        "bootupTimestamp": 0,
        "version": "4.28.1F",
        "architecture": "",
        "internalBuild": "",
        "hardwareRevision": "",
        "domainName": "atd.lab",
        "hostname": "leaf4",
        "fqdn": "leaf4.atd.lab",
        "serialNumber": "leaf4",
        "deviceType": "eos",
        "danzEnabled": False,
        "mlagEnabled": False,
        "streamingStatus": "active",
        "parentContainerKey": "container_12463e1d-8af6-43fa-986a-e4e249fd62df",
        "status": "Registered",
        "complianceCode": "0000",
        "complianceIndication": "",
        "ztpMode": False,
        "unAuthorized": False,
        "ipAddress": "192.168.0.15",
    },
    {
        "modelName": "cEOSLab",
        "internalVersion": "4.28.1F",
        "systemMacAddress": "00:1c:73:b6:d5:01",
        "bootupTimestamp": 0,
        "version": "4.28.1F",
        "architecture": "",
        "internalBuild": "",
        "hardwareRevision": "",
        "domainName": "atd.lab",
        "hostname": "host1",
        "fqdn": "host1.atd.lab",
        "serialNumber": "host1",
        "deviceType": "eos",
        "danzEnabled": False,
        "mlagEnabled": False,
        "streamingStatus": "active",
        "parentContainerKey": "container_2cbfe3d7-77a1-4bb4-b51b-278c56cdc9a3",
        "status": "Registered",
        "complianceCode": "0000",
        "complianceIndication": "",
        "ztpMode": False,
        "unAuthorized": False,
        "ipAddress": "192.168.0.16",
    },
    {
        "modelName": "cEOSLab",
        "internalVersion": "4.28.1F",
        "systemMacAddress": "00:1c:73:b2:d5:01",
        "bootupTimestamp": 0,
        "version": "4.28.1F",
        "architecture": "",
        "internalBuild": "",
        "hardwareRevision": "",
        "domainName": "atd.lab",
        "hostname": "leaf1",
        "fqdn": "leaf1.atd.lab",
        "serialNumber": "leaf1",
        "deviceType": "eos",
        "danzEnabled": False,
        "mlagEnabled": False,
        "streamingStatus": "active",
        "parentContainerKey": "container_12463e1d-8af6-43fa-986a-e4e249fd62df",
        "status": "Registered",
        "complianceCode": "0000",
        "complianceIndication": "",
        "ztpMode": False,
        "unAuthorized": False,
        "ipAddress": "192.168.0.12",
    },
    {
        "modelName": "cEOSLab",
        "internalVersion": "4.28.1F",
        "systemMacAddress": "00:1c:73:b1:d5:01",
        "bootupTimestamp": 0,
        "version": "4.28.1F",
        "architecture": "",
        "internalBuild": "",
        "hardwareRevision": "",
        "domainName": "atd.lab",
        "hostname": "spine2",
        "fqdn": "spine2.atd.lab",
        "serialNumber": "spine2",
        "deviceType": "eos",
        "danzEnabled": False,
        "mlagEnabled": False,
        "streamingStatus": "active",
        "parentContainerKey": "container_1d62446c-7ead-4788-a1a1-8250362031de",
        "status": "Registered",
        "complianceCode": "0000",
        "complianceIndication": "",
        "ztpMode": False,
        "unAuthorized": False,
        "ipAddress": "192.168.0.11",
    },
    {
        "modelName": "cEOSLab",
        "internalVersion": "4.28.1F",
        "systemMacAddress": "00:1c:73:b8:d5:01",
        "bootupTimestamp": 0,
        "version": "4.28.1F",
        "architecture": "",
        "internalBuild": "",
        "hardwareRevision": "",
        "domainName": "atd.lab",
        "hostname": "cvx01",
        "fqdn": "cvx01.atd.lab",
        "serialNumber": "cvx01",
        "deviceType": "eos",
        "danzEnabled": False,
        "mlagEnabled": False,
        "streamingStatus": "active",
        "parentContainerKey": "container_0c1841f1-e287-42c1-a409-8e0d2000bcb9",
        "status": "Registered",
        "complianceCode": "0000",
        "complianceIndication": "",
        "ztpMode": False,
        "unAuthorized": False,
        "ipAddress": "192.168.0.18",
    },
]
