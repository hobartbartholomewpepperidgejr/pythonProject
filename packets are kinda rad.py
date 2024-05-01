devices = []

packet = {
        "address": 9847008,
        "command": "connect",
        "data": "9847008",
        "sender": "9847008"
    }

class printer:
    devices.append("printer")
    connected = None
    address = 9847008
    def connect(self, sender):
        if self.connected == None:
            self.connected = sender
    def disconnect(self, sender):
        print("aeiou")




# central loop
while True:
    for i in devices:
        if eval(i).address == packet["address"]:
            eval(i+"."+packet['command']+"("+packet['data']+")")
    quit()