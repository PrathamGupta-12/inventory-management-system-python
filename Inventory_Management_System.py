class InventoryManagementSystem:
    def __init__(self):
        self.productList = []
        self.productDict = {}
        self.action = None

        while self.action != 7:

            print('''
                ========== Inventory Management System ==========
                1. Add Product
                2. Update Quantity
                3. Remove Product
                4. Search Product
                5. Display Inventory
                6. Display Total Inventory Value
                7. Exit
                ===============================================
                  ''')
            
            self.action = int(input("Enter your choice : "))

            if self.action == 1:

                productName = input("Enter the Product Name : ")

                if productName in self.productList:

                    print("---> Product already in the Inventory.")

                else:

                    quantity = int(input("Enter the Quantity : "))
                    pricePerUnit = int(input("Enter Price per Unit : "))

                    print("---> Product added Successfully.")

                    temp = {}
                    temp.update({"Quantity" : quantity})
                    temp.update({"Price" : pricePerUnit})

                    self.productList.append(productName)

                    self.productDict[productName] = temp

            elif self.action == 2:

                productName = input("Enter the Product Name : ")

                if productName not in self.productList:
                    print("---> Product does not exists in the Inventory.")
                
                else:

                    newQuantity = int(input("Enter quantity to add : "))
                    self.productDict[productName]["Quantity"] += newQuantity

                    print("---> Quantity updated successfully.")

            elif self.action == 3:

                productName = input("Enter the Product Name : ")

                if productName not in self.productList:
                    print("---> Product does not exists in the Inventory.")

                else:

                    del self.productDict[productName]
                    self.productList.remove(productName)

                    print(f"---> {productName} removed successfully.")

            elif self.action == 4:

                productName = input("Enter Product Name : ")
                
                if productName not in self.productList:
                    print(f"---> {productName} does not exists in the Inventory.")

                else:
                    print("---> Product Found\n")

                    print(f'''
                        Name      : {productName}
                        Quantity  : {self.productDict[productName]["Quantity"]}
                        Price     : {self.productDict[productName]["Price"]} 
                          ''')
                    
            elif self.action == 5:

                if not self.productDict:
                    print("Inventory is empty, Add Products to display them.")

                else:
                    print('''
                        ------------- Inventory -------------

                        Product     Quantity     Price
                          ''')
                    
                    for key in self.productDict:

                        print(f'''
                            {key}     {self.productDict[key]["Quantity"]}     {self.productDict[key]["Price"]}
                                ''')
                        
                    print('''
                        -------------------------------------
                          ''')
            elif self.action == 6:

                if not self.productDict:
                    print("Inventory is empty, Add Products to display them.")

                else:
                    totalInventoryValue = 0

                    for key in self.productDict:

                        totalInventoryValue += self.productDict[key]["Quantity"] * self.productDict[key]["Price"]

                    print(f"Total Inventory Value : ₹{totalInventoryValue}")

            elif self.action == 7:
                print("---> Program terminated successfully.")

            else:
                print("---> Invalid choice.")


inventory = InventoryManagementSystem()