# Now lets understand how we can use String data type and how to store it in a variable, To store a String in a variable we have to use double quotes and enclose the value inside.

name= "Nishant"
about = "I am a software engineer at heart and would love to learn any technology that comes my way."

#  Now to print any of the following we can use the print key word

print(name);


#  We can concatinate a string 

full_intro = name + " - " + about

print(full_intro)

#  We can also turn string into upper case and lower case 

# Upper case
print(name.upper())

# Lower case
print(name.lower())


#  WE can dfind the index of the first occurrence of a substring (returns -1 if not found).
text = "Hello, World!"
print(text.find("World"))  

