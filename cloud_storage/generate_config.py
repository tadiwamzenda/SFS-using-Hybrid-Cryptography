

import configparser

config_file = configparser.ConfigParser()
config_file.add_section("SMTPlogin")

# Add settings to section
# Here you need to modify the values of last parameter of set function
config_file.set("SMTPlogin", "sender_address", "mzendatp@gmail.com")
config_file.set("SMTPlogin", "receiver_address", "mzendatp@gmail.com")
config_file.set("SMTPlogin", "mailtrap_user", "a8e8af3be07d6c")
config_file.set("SMTPlogin", "mailtrap_password", "86a6715b53f68c")

# Saving config file as configurations.ini
with open(r"configurations.ini", 'w') as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()

print("Config file 'configurations.ini' created")
