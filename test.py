import re
import datetime
txt = "Thứ Ba, 28 thng 3, 2023"
rg_pattern = "([0-9]+)"
x = re.findall(rg_pattern, txt)
print(datetime.datetime.now().strftime("%m/%d/%Y"))
print(datetime.datetime.now().strftime("%H:%M:%S"))