import re

text = open("vendorMacs.xml", "r", encoding="utf-8").read()
new_text = ""
for i in text.split("\n"):
    try:
        comp = re.findall(r"mac_prefix=\".{1,}\" vendor_name=\"(.{1,})\"", i)[0]
        mac = re.findall(r"mac_prefix=\"(.{1,})\" vendor_name=\".{1,}\"", i)[0]
        new_text += mac + "\t" + comp + "\n"
        #print(mac, comp)
    except:
        pass

open("mac_new.txt", "w", encoding="utf-8").write(new_text)
print("end")
