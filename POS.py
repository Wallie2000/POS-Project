class MyProduct:
    #Initialize product with name and price
    def __init__(self, product_name, product_price):
        self.name = product_name
        self.price = (product_price)

class AddItemReceipt():
    def __init__(self):
        self.items = [] #List to store added products
        self.total = 0 #Variable used to store total price of products

    #Method to add Item to receipt
    def add_item(self, items):
        self.items.append(items)
        self.total += items.price

    #Method to print the receipt
    def Receipt(self):
        print('_________________')
        print('Receipt.')
        print('')
        print('Products: ')
        print('')
        for product in self.items:  
            print(f'{product.name} R{product.price:.2f}')
        print('-------------------------')
        print(f'Total: R{self.total:.2f}')
        print('-------------------------\n')

 
def main():
    add_item_receipt = AddItemReceipt()
    sentinel = 'q' #Sentinel variable to exit the loop
    
    #Infinite loop using iter(int, 1) 
    for _ in iter(int, 1):
        
        print('POS.')
        print('1. Add item.')
        print('2. Print receipt.')

        print('Enter \'q\' to Quit')
        print('')

        answer = input('Enter your choice: ')
        if answer.lower() == sentinel:
            print('Goodbye.')
            break

        if answer == '1':
            while True:
                name = input('Enter name of product: ')
                if name.lower() == sentinel:
                    print('Goodbye.')
                    return
                if name.isalpha():  # Check if the input is a string containing only letters
                    break
                else:
                    print('')
                    print("Invalid input. Please enter name of product.")
                    print('')
                    continue
                    
            while True:
                price = input('Enter price of product: R')
                print('')
                if name.lower() == sentinel: #If sentinel is used end the loop
                    print('Goodbye.')
                    return
                try:
                    price = float(price)  # Check if the input is a valid float
                    break
                except ValueError:
                    print("Invalid input. Please enter price of product.")
                    print('')
                    continue

          
            items = MyProduct(name, price)
            add_item_receipt.add_item(items)

        #Elif that prints the receipt.
        elif answer == '2':
            add_item_receipt.Receipt()

        else:
            print('Enter valid choice, 1, 2 or q\n')#When no valid choice is entered this message displays.
            

        
               
if __name__ == '__main__':
    main()
        

    


    









    

        


   
   

           

   

    

    
    

     





          

