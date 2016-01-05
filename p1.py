def list1():
    list=[]
    while True:
        usint = input("please enter items ")
        list.append(usint)
        print(list)
        
        for x in list:
            list.count(x)
            
            if((list.count(x)) > 1):
                print("No Duplicates!")
              
                list.clear()
                break
            
list1()