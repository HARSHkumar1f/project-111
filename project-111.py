import os;
import shutil;

os.getcwd()
#os.mkdir("Images")

 #split the Text
path="get-pip.py";
root,extension=os.path.splitext(path);
print("the root elemen are",root)
print("the extension is",extension)

#making a copy of file
source="get-pip.py"
destination="get-pip1.py"
dest=shutil.copy(source,destination)
print("after copying the file")