from main import SmartHouse, Room, Device_AGD, Device_Entertaiment, Door, Window

myHouse = SmartHouse()

room01 = Room("Living room and kitchen")
room02 = Room("Corridor")
room03 = Room("Bedroom")
room04 = Room("Bathroom")

# LIGHTS
room01.add_lamp("01L000", "normal").add_lamp("01L001", "normal").add_lamp("01L002", "normal").add_lamp("01L003", "normal").add_lamp("01L004", "normal").add_lamp("01L005", "normal")

room02.add_lamp("02L000", "normal").add_lamp("02L001", "normal")

room03.add_lamp("03L000", "RGB").add_lamp("03L001", "normal").add_lamp("03L002", "normal").add_lamp("03L003", "normal").add_lamp("03L004", "normal")

room04.add_lamp("04L000", "normal")

# DOORS AND WINDOWS
door_010D00 = Door("010D00", "out")
door_020D00 = Door("020D00", "out")
door_023D01 = Door("023D01", "in")
door_024D02 = Door("024D02", "in")
window_010W00 = Window("010W00")
window_030W02 = Window("030W02")

room01.add_window(window_010W00).add_door(door_010D00)

room02.add_door(door_020D00).add_door(door_023D01).add_door(door_024D02)

room03.add_window(window_030W02).add_door(door_023D01)

room04.add_door(door_024D02)

# DEVICES
washing_machine = Device_AGD("04W000")
dishwasher = Device_AGD("01D001")
cooker = Device_AGD("01C002")
kettle = Device_AGD("01K003")
TV = Device_Entertaiment("01T004")
radio01 = Device_Entertaiment("01R005")
radio03 = Device_Entertaiment("03R006")
radio04 = Device_Entertaiment("04R007")

room01.add_device(TV).add_device(radio01).add_device(cooker).add_device(dishwasher).add_device(kettle)

room03.add_device(radio03)

room04.add_device(radio04).add_device(washing_machine)

myHouse.add_room(room01).add_room(room02).add_room(room03).add_room(room04)

print(myHouse)