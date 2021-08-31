import subprocess
from cs50 import get_string
import os

#cmd = "pset2/substitution/substitution.c"
# Example
# cmd = HelloWorld.c
print ("Hey this is Python Script Running\n")
#subprocess.call("pset1/hello/hello.c adam", shell=True) #For Compiling
#subprocess.call("./a.out")
#os.system("gcc -o hello hello.c")
#if os.path.isfile("hello"):
 #   os.system("./hello John")
    #x = subprocess.check_output("./hello John", shell=True)
    #print(x + "x")
#else:
 #   print("no file")

getVersion =  subprocess.Popen("./plurality a b", shell=True, stdout=subprocess.PIPE).stdout
version =  getVersion.read()

print(version.decode())

#end thats all

