def mac2name(macaddress):
    macaddress = macaddress.upper()
    macaddress = macaddress.replace(":","") # Delete All (:) in Mac address

    macfile = open("mac_new.txt", "r", encoding="utf-8").read() # open macfile

    finded = []

    for mac in macfile.split("\n"):
        if mac == "":
            continue
        mac = mac.strip("\n") # Delete (\n) at end of line
        #print(mac)
        device = mac.split("\t")[1]  # device company
        mac = mac.split("\t")[0].replace(":", "") # device mac address
        mc = macaddress[0:len(mac)-1]
        if mc in mac:
            finded.append(device)
            print(device)
    del macfile
    return finded

print(mac2name("30:6a:85"))# ['Samsung Electronics Co.,Ltd']
print(mac2name("30:6a"))   # ['PENTA MEDIA CO., LTD.', 'Samsung Electronics Co.,Ltd']
print(mac2name("30"))      # [...]
