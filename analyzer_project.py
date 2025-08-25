
import numpy as np


class ANALYZER:
    
  
 

    def create_array(self):
       
        print("select the type of array to create\n")
        print("1.1D array\n2.2D array\n3.3D array\n")
        choice = int(input("Enter your choice for dimentional array :"))
        if choice == 1:

            list = input("Enter ypur elements for the crating array seprated by space :")
            A = list.split()
            self.arr1D = np.array(A, dtype=int)
            print(f"1D array created successfully!:{self.arr1D}")
            
            print("1.indexing\n2.slicing\n3.go back\n")
            choose = int(input("Choose an option for opration :"))
            
            if choose==1:
                B = int(input("Enter your indexing number :"))
                print(self.arr1D[B])
                
            if choose==2:
                C = int(input("Enter your starting index :"))
                D = int(input("Enter your ending index :"))
                print(self.arr1D[C:D])
                
            if choose==3:
                print("Go beck !")
                choice = int(input("Enter your choice for dimentional array :"))
        elif choice == 2:
            list = input("Enter ypur elements for the crating array seprated by space :")
            list = list.split()
            A = int(input("Enter the row range :"))
            B = int(input("Enter the colum range :"))
            arr2D = np.reshape(list,(A,B))
            self.arr2D=arr2D.astype(int)
            print("2D array created successfully!")
            print(arr2D)
            print("1.indexing\n2.slicing\n3.go back\n") 
            choose = int(input("Choose an option for opration :"))
            
            if choose==1:
                S = int(input("Enter your indexing number :"))
                E = int(input("Enter your ending index :"))
                print(self.arr2D[S,E])
                
            if choose==2:
                C = int(input("Enter your starting index for row :"))
                D = int(input("Enter your ending index for row :"))
                F = int(input("Enter your starting index for colum :"))
                G = int(input("Enter your ending index for colum :"))
                print(self.arr2D[C:D,F:G])
                
            if choose==3:
                print("Go beck !")
                choice = int(input("Enter your choice for dimentional array :"))
        elif choice == 3:
            list = input("Enter ypur elements for the crating array seprated by space :")
            list = list.split()
            A = int(input("Enter the row range :"))
            B = int(input("Enter the colum range :"))
            C = int(input("Enter the last range :"))
            arr3D = np.reshape(list,(A,B,C))
            self.arr3D=arr3D.astype("int")
            print("3D array created successfully!")
            print(self.arr3D)
            print("1.indexing\n2.slicing\n3.go back\n")
            choose = int(input("Choose an option for opration :"))
            
            if choose==1:
                S = int(input("Enter your indexing number :"))
                E = int(input("Enter your ending index :"))
                H = int(input("Enter your last index :"))
                print(self.arr3D[S,E,H])
                
            if choose==2:
                C = int(input("Enter your starting index for row :"))
                D = int(input("Enter your ending index for row :"))
                F = int(input("Enter your starting index for colum :"))
                G = int(input("Enter your ending index for colum :"))
                J = int(input("Enter your ending index for row :"))
                L = int(input("Enter your starting index for colum :"))
                print(self.arr3D[C:D,F:G,J:L])
                
            if choose==3:
                print("Go beck !")
                
            
    
    def mathamatical(self):
        arr1 = self.get_array("first")
        arr2 = self.get_array("second")
            # arry1=np.array()
        a=int(input("Choose an mathamatical Opration:\n1.Addition \n2.Subtraction\n3.multyplication\n4.Divition"))    
        if a==1:
            result=np.add(arr1,arr2)
            print(result)       
        if a==2:
            result=np.subtract(arr1,arr2)
            print(result)
        if a==3:
            result=np.multiply(arr1,arr2)
            print(result)
        if a==4:
            result=np.divide(arr2,arr1)
            print(result)
    def combine_or_split(self):
        print("1. Combine Arrays\n2. Split Array")
        c = int(input("Enter your choice: "))

        arr1 = self.get_array("first")
        arr2 = self.get_array("second")
        if c == 1:
            try:
                result = np.concatenate((arr1, arr2), axis=0)
                print("Combined Array:")
                print(result)
            except ValueError as e:
                print(f"Error combining arrays: {e}")
        elif c == 2:
            try:
                n = int(input("Enter number of splits: "))
                result = np.array_split(arr1, n)
                print("Split Result:")
                for part in result:
                    print(part)
            except Exception as e:
                print(f"Error splitting array: {e}")
        else:
            print("Invalid choice.")
            
            
    def search_short_filter(self):
        arr = self.get_array("array")

        print("Choose an option:\n1. Search Value\n2. Sort Array\n3. Filter Values")
        f = int(input("Enter your choice: "))
        if f == 1:
            val = int(input("Enter value to search: "))
            result = np.where(arr == val)
            print(f"Element found at: {result}")
        elif f == 2:
            print("Sorted Array:")
            print(np.sort(arr))
        elif f == 3:
            val = int(input("Filter elements less than: "))
            print(arr[arr < val])
        else:
            print("Invalid choice.")
    def aggregate_and_satistics(self):
        print("choose an aggregate/statistical opration\n1.sum\n2.mean\n3.median\n4.standerd_divition\n5.variance\n")
        v = int(input("Enter your choice :"))
        
        A = int(input("Enter the START range :"))
        B = int(input("Enter the STOP range :"))
        arr2D = np.arange (A,B)
        # arr1=arr2D.astype("int")
        if v==1:
            print(arr2D.sum())
            
        if v==2:
            print(arr2D.mean())
            
        if v==3:
            print(np.median(arr2D))

            
        if v==4:
            print(arr2D.std())
            
        if v==5:
            print(arr2D.var())
            
            
    def get_array(self, name="array"):
        data = list(map(int, input(f"Enter ypur elements for the crating {name} array seprated by space : ").split()))
        if len(data) != 6:
            raise ValueError("You must enter exactly 6 elements.")
        rows = int(input(f"Enter row size for {name} array: "))
        cols = int(input(f"Enter column size for {name} array: "))
        if rows * cols != 6:
            raise ValueError("Row * Column must equal 6.")
        arr = np.reshape(data, (rows, cols))
        return arr
            
a = ANALYZER()

while True:
    print("Walcome to the numpy anaylyzer!!")
    print("1. Create a NumPy array")
    print("2. Perform mathematical operation")
    print("3. Combine or split arrays")
    print("4. Search, sort, or filter array")
    print("5. Compute aggregate/statistics")
    print("6. Exit")

    try:
        press = int(input("choose an option for analyzer : "))
        if press == 1:
            a.create_array()
        elif press == 2:
            a.mathamatical()
        elif press == 3:
            a.combine_or_split()
        elif press == 4:
            a.search_short_filter()
        elif press == 5:
            a.aggregate_and_satistics()
        elif press == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Try again.")
    except Exception as e:
        print(f"Error: {e}")