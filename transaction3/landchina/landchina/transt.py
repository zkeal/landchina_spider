fo=open('proxy.txt')
fo_content= fo.readlines()
fo.close()
file_object = open('proxy1.txt', 'w')
for temp in fo_content:
    temp='http://'+temp
    file_object.write(temp)

