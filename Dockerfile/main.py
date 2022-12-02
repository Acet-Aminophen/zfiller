from natsort import natsorted
from collections import defaultdict
import os

file_path = "/target"
file_type = ["jpg", "png", "webp", "gif", "jpeg", "jfif"]
recover_file_location = file_path + "/do_recover.txt"
name_dic = defaultdict(int)

if os.path.isfile(recover_file_location):
    with open(recover_file_location, 'r', encoding="utf-8") as f:
        log_list = f.read().splitlines()
        in_is = ""
        for idx, line in enumerate(log_list):
            if line == "IN":
                in_is = log_list[idx + 1]
            if line == "OUT":
                out_is = log_list[idx + 1]
                if "@eaDir" in in_is or "@eaDir" in out_is:
                    continue
                else:
                    os.rename(out_is, in_is)
                    print("IN")
                    print(out_is)
                    print("OUT")
                    print(in_is)
                if line == "CLEAR":
                    break
    print("RECOVER CLEARED")
    exit(0)

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
exit(0)
