# asm8
#For creating a text file that can be monitored for the microservice, do the following code: 

def save_to_txt(expenses):
    f = open('./example.txt', 'r+')
    for item in expenses: 
        f.write(str(item["price"]))
        f.write("\n")

#Then to do the microservice, you simply need to make sure it reads from the correct file and then writes to a new one. 
