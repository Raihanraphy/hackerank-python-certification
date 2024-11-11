#!/bin/python3
import os


class VendingMachine():
    def __init__(self,value_1,value_2):
        self.value_1=value_1
        self.value_2=value_2

    def buy(self,new_val,new_val2):
        if(self.value_1>=new_val and new_val*self.value_2<=new_val2):
            self.value_1-=new_val
            return new_val2-(new_val*self.value_2)
        else:
            if(self.value_1<new_val):
                return "Not enough items in the machine"
            else:
                return "Not enough coins"
            
            
         
        
    pass
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")


    fptr.close()