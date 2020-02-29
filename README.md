# new-textro
A text-based game exploring the post-apocalyptic city of New Metro. Developed in Python for ShefJam 7

## Setup
Make sure you have Python installed on your machine. This app was developed in Python 3.7 on Windows 10.

If there are any issues with imports (for example, modules in the NPCs folder not being able find other modules), make sure you have added the following to your PYTHONPATH environment variable:
* Python installation path (e.g. C:\Users\username\AppData\Local\Programs\Python\Python37-32)
* The path to the New-Textro parent folder (e.g. C:\Users\username\Documents\New-Textro)
* The path to the subfolder that is struggling to import other modules (e.g. C:\Users\username\Documents\New-Textro\NPCs)

Alternatively, try adding the following code to the top of the file:
* For problems with imports in the same directory

    > import os,sys
    > sys.path.append(os.path.join(os.path.dirname(\_\_file__)))

* For problems with imports in the parent directory

    > import os,sys,inspect
    > currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    > parentdir = os.path.dirname(currentdir)
    > sys.path.insert(0,parentdir) 