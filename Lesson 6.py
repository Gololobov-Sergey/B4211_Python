import os

path = "C:\\Users\\golol\\Downloads"

path = os.path.normpath(path)

'''for p, d, f in os.walk(path):
    print(f"Path  - {p}")
    print(f"Dirs  - {d}")
    print(f"Files - {f}")'''

'''print(os.path.isdir(path))
print(os.path.isabs(path))
print(os.path.islink(path))
print(os.path.isfile(path))
print(os.path.exists(path))

dir = "111"
path = os.path.join(path, dir)
print(path)
os.mkdir(path)'''

'''file = open("text.txt", "w", encoding="utf-8")
file.write("Слава Україні!")
file.close()'''

'''file = open("text.txt", "a", encoding="utf-8")
file.write("Слава Україні!\n")
file.close()'''

'''file = open("text.txt", "r", encoding="utf-8")
lines = file.readlines()
print(lines)
file.close()'''

'''with open("text.txt", "r", encoding="utf-8") as file:
    print(file.read())'''

#print(os.path.getctime("text.txt"))

def spy(path):
    path = os.path.normpath(path)
    result = {"dirs":[], "files":[]}
    for p, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            result["dirs"].append(dir)
        for file in filenames:
            result["files"].append(file)
    with open("spy.txt", "w", encoding="utf-8") as file:
        file.write(f"PATH : {path:-<50}\n")
        file.write("{:-<50}\n".format("Directories:"))
        for dir in result["dirs"]:
            file.write(f"\t[{str.upper(dir)}]\n")
        file.write("{:-<50}\n".format("Files:"))
        for files in result["files"]:
            file.write(f"\t[{files}]\n")


p = "d:/inst"
spy(p)