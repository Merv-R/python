import re

pattern = "\(\d{3}\)[\s|-]\d{3}[\s|-]\d{4}|\d{10}"
pattern2 = "[a-zA-Z0-9_]*@[a-zA-Z0-9]*\.[com|org|edu|gov]+"
pattern3 = "ID[^\d]*(\d*)"

with open("sample.txt", "r") as f:
    lines = f.read()
    phone_num = re.findall(pattern, lines)
    emails = re.findall(pattern2, lines)
    ids = re.findall(pattern3, lines)
    print(phone_num)
    print(emails)
    print(ids)