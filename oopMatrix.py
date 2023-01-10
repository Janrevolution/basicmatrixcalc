import oopMatrix
class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = []
        for i in range(self.rows):
            self.matrix.append([])
            for j in range(self.columns):
                self.matrix[i].append(0)
                
    def add(self, other_matrix):
        if self.rows != other_matrix.rows or self.columns != other_matrix.columns:
            try:
                print("\nNOT POSSIBLE \nMatrices must have the same dimensions to be added")
                print("Please enter again the size of matrices \n")
                main()
            except IndexError:
                pass
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.matrix[i][j] = self.matrix[i][j] + other_matrix.matrix[i][j]
        return result
    
    def subtract(self, other_matrix):
        if self.rows != other_matrix.rows or self.columns != other_matrix.columns:
            try:
                print("\nNOT POSSIBLE \nMatrices must have the same dimensions to be subtracted")
                print("Please enter again the size of matrices \n")
                main()
            except IndexError:
                pass
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.matrix[i][j] = self.matrix[i][j] - other_matrix.matrix[i][j]
        return result
    
    def multiply(self, other_matrix):
        if self.columns != other_matrix.rows:
            try:
                print("\nNOT POSSIBLE \n The number of columns in the first matrix must be equal to the number of rows in the second matrix to perform multiplication")
                print("Please enter again the size of matrices \n")
                main()
            except IndexError:
                pass
        result = Matrix(self.rows, other_matrix.columns)
        for i in range(self.rows):
            for j in range(other_matrix.columns):
                result.matrix[i][j] = 0
                for k in range(self.columns):
                    result.matrix[i][j] += self.matrix[i][k] * other_matrix.matrix[k][j]
        return result
    
    def __str__(self):  # This function creates spaces between elements of the matrices
        result = ""     # Initialize
        for i in range(self.rows):
            result += "\t"
            for j in range(self.columns):
                result += str(self.matrix[i][j]) + " " # The space between elements
            result += "\n"  # New line after a row
        return result

def get_matrix_element(matrix_number, row, col):
    while True:
        value = input(f"Enter the value for matrix {matrix_number} at position ({row},{col}): ")
        try:
            value = int(value)
            return value
        except ValueError:
            print("Invalid input, please input an integer only or you can simply quit the program by typing 'exit'")
        if value.lower() == "exit":
            exit()
def generate_matrix():
    try:
        rows1 = int(input("Enter the number of rows in matrix 1: "))
        columns1 = int(input("Enter the number of columns in matrix 1: "))
    except ValueError:
        print("\nInvalid input! Please enter integer values\n")
        main()

    matrix1 = Matrix(rows1, columns1)
    for i in range(rows1):
        for j in range(columns1):
            matrix1.matrix[i][j] = get_matrix_element(1, i+1, j+1)
    print("Matrix 1:")
    print("A = ", matrix1)
def main():
    # Get the dimensions of the two matrices from the user
    try:
        rows1 = int(input("Enter the number of rows in matrix 1: "))
        columns1 = int(input("Enter the number of columns in matrix 1: "))
        rows2 = int(input("Enter the number of rows in matrix 2: "))
        columns2 = int(input("Enter the number of columns in matrix 2: "))
    except ValueError:
        print("\nInvalid input! Please enter integer values\n")
        main()
    
    
    # Create the two matrices and fill them with values
    matrix1 = Matrix(rows1, columns1)
    for i in range(rows1):
        for j in range(columns1):
            matrix1.matrix[i][j] = get_matrix_element(1, i+1, j+1)

    matrix2 = Matrix(rows2, columns2)
    for i in range(rows2):
        for j in range(columns2):
            matrix2.matrix[i][j] = get_matrix_element(2, i+1, j+1)
    
    # Print the matrices
    print("Matrix 1:")
    print(matrix1)
    print("Matrix 2:")
    print(matrix2)
    
    # Get the operation from the user
    opIsValid = True
    while opIsValid:
        operation = input("Enter '+', '-', or '*' to perform the respective operation: ")
        
        # Perform the operation and print the result
        if operation == "+":
            result = matrix1.add(matrix2)
            opIsValid = False
        elif operation == "-":
            result = matrix1.subtract(matrix2)
            opIsValid = False
        elif operation == "*":
            result = matrix1.multiply(matrix2)
            opIsValid = False
        else:
            opIsValid = True
            result = "\nInvalid Operator\n"
    print("Result:")
    print(result)
    exit()

if __name__ == "__main__":
    while True:
        print("\nWhat do you want to do? Please enter your choice.\n")
        print("(1) Generate Matrix")
        print("(2) Calculate Matrices")
        print("(3) Exit")
        choice = (input(">> "))

        try:
            choice = int(choice)
            if choice == 1:
                generate_matrix()
            elif choice == 2:
                main()
            elif choice == 3:
                exit()
            elif choice != 1 or choice != 2:
                raise ValueError("Invalid")
        except ValueError as valerr:
            print("\nInvalid Choice. Please Try again")
            __name__