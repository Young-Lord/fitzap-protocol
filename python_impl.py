from bleak import BleakScanner, BleakClient
devices = [i for i in await BleakScanner.discover() if i.name is not None and i.name.startswith("DIAN-JI-")]
if not devices:
    print("device not found!")
    exit(1)
device = devices[0]
address = device.address
async with BleakClient(address) as client:
    services = [i for i in client.services if i.uuid == "0000ff01-0000-1000-8000-00805f9b34fb"]
    if not services:
        print("service not found!")
        exit(1)
    service = services[0]
    characteristics = [i for i in service.characteristics if i.uuid == "0000ff02-0000-1000-8000-00805f9b34fb"]
    if not characteristics:
        print("characteristic not found!")
        exit(1)
    char = characteristics[0]
    await client.start_notify(char, lambda a, b:print("response:", bytes(b)))
    await client.write_gatt_char(char, b"light=01", True)
