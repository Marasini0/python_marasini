import os
#renaming the test.py.txt to meroFile.txt
if os.path.exists('test.py.txt'):
    os.rename('test.py.txt', 'meroFile.txt')

#delete the file
if os.path.exists('meroFile.txt'):
    os.remove('meroFile.txt')




