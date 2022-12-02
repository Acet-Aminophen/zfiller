from natsort import natsorted
from collections import defaultdict
import os

file_path = "/target"
file_type = ["jpg", "png", "webp", "gif", "jpeg", "jfif"]
name_dic = defaultdict(int)

for file in os.walk(file_path):
    files = file[2][:]
    for idx, name in enumerate(natsorted(files)):
        if "@eaDir" in file[0]:
            continue
        type_is = name.split(".")[-1]
        if type_is not in file_type:
            continue
        org_path = file[0] + "/" + name
        renamed = file[0] + "/" + str(name_dic[file[0]] + 1).zfill(5) + "." + type_is
        os.rename(org_path, renamed)
        name_dic[file[0]] += 1
        print("IN")
        print(org_path)
        print("OUT")
        print(renamed)

print("CLEAR")