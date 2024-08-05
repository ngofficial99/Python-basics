# Lets declare a variable 

lang = input("Enter the language")

if True:
    print("The statement is true")
    
# Like this we can check for one condition
if lang == "python":
    print("language is python")

# now if i want to perform an operation if language is python i will print python esle i will print not python

if lang == "python":
    print("language is python")
else:
    print("language is not python")
    
# Now if i want to add multiple conditions based on different porgramming language we will make use of else if block

if lang == "python":
    print("Entered language is python")
elif lang == "java":
    print("Entered language is Java")
elif lang == "javascript":
    print("Language entered is Javascript")
else:
    print("not recogonized")
    
