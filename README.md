# python_tell_seek
black magic in file reading 

tell() function returns value far behind the length of a file. 

I tried it in Python 3.4, 3.5, 3.6. 
The same behaviour, the same pointers.

It seems all "magic" pointers are "normal" pointer + 0x10000000000000001
and these both pointers are interchangeable. 
