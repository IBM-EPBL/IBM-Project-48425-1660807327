#Python progam to print even numbers in given range 

start = int(input("Enter the start of range: "))
end= int(input("Enter the end of range: "))
 
 #create a list that contains only odd numbers in given range
 
even_list = range(start,end+1)[start%2::2]
 
for num in even_list:
     
     print(num,end = "")