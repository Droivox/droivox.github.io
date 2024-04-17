import random, os

git_id = random.randint(-9999999, 999999)
path = os.path.dirname(os.path.realpath(__file__))
msg = str(git_id)

os.system("cd " + str(path))
os.system("git add .")
os.system("git commit -m " + str(msg))
os.system("git push")