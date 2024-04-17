import random, os

path = os.path.dirname(os.path.realpath(__file__))
msg = input("Git -M : ")

os.system("cd " + str(path))
os.system("git add .")
os.system("git commit -m " + msg)
os.system("git push")