# Write an alphabet tree to a file
# An alphabet tree looks like this:

##a
##bb
##ccc
##dddd
##eeeee
file_name = input("Filename pls")
x = input("What is the last letter of the alphabet tree? (Please enter a letter)")

def alphabet_tree(last_letter,file_name):
  """write the alphabet tree ending with *last_letter* to the file with file name *file_name*."""
  a = 'abcdefghijklmnopqrstuvwxyz'
  stop = 0
  for k in range(len(a)):
    if last_letter == a[k]:
      stop = 25-k
  for i in range (len(a)-stop):
    x = open(file_name,'a')
    x.write((a[i]*(i+1)))
    x.write('\n')
    x.close()
            
alphabet_tree(x,file_name)
