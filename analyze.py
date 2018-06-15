import os

f = open("KingBase2018-A80-A99.pgn", encoding="iso-8859-1")
size = os.fstat(f.fileno()).st_size

magic_pointers = []
while f.readline():
    if f.tell() > size:
        magic_pointers.append(f.tell())

print("length of magic_pointers after readline(): {}"\
      .format(len(magic_pointers)))

print("first magic pointer: {}".format(magic_pointers[0]))
f.seek(magic_pointers[0])
print(f.readline())
print("tell() after seek() and readline() {}".format(f.tell()))

# supermagic
f.seek(500)
for i in range(3):
    print(f.readline())
print(f.tell())
mp1 = f.tell()

f.seek(624)
print(f.readline())
print(f.tell())
mp2 = f.tell()

print("is the pointer {} the same as {} or not???".format(mp1, mp2))

