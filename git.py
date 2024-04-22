import random, os

path = os.path.dirname(os.path.realpath(__file__))
msg = str(random.randint(0, 999999999999999))

os.system("cd " + str(path))
os.system("git add .")
os.system("git commit -m " + msg)
os.system("git push")
os.system("@pause")