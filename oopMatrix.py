class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []
        for i in range(self.rows):
            self.matrix.append([])
            for j in range(self.cols):
                self.matrix[i].append(0)
                
    def add(self, other_matrix):
        if self.rows != other_matrix.rows or self.cols != other_matrix.cols:
            raise ValueError("Matrices must have the same dimensions to be added")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[i][j] = self.matrix[i][j] + other_matrix.matrix[i][j]
        return result
    
    def subtract(self, other_matrix):
        if self.rows != other_matrix.rows or self.cols != other_matrix.cols:
            raise ValueError("Matrices must have the same dimensions to be subtracted")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[i][j] = self.matrix[i][j] - other_matrix.matrix[i][j]
        return result
    
    def multiply(self, other_matrix):
        if self.cols != other_matrix.rows:
            raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix to perform multiplication")
        result = Matrix(self.rows, other_matrix.cols)
        for i in range(self.rows):
            for j in range(other_matrix.cols):
                result.matrix[i][j] = 0
                for k in range(self.cols):
                    result.matrix[i][j] += self.matrix[i][k] * other_matrix.matrix[k][j]
        return result
    
    def __str__(self):
        result = ""
        for i in range(self.rows):
            for j in range(self.cols):
                result += str(self.matrix[i][j]) + " "
            result += "\n"
        return result

def main():
    # Get the dimensions of the two matrices from the user
    rows1 = int(input("Enter the number of rows in matrix 1: "))
    cols1 = int(input("Enter the number of columns in matrix 1: "))
    rows2 = int(input("Enter the number of rows in matrix 2: "))
    cols2 = int(input("Enter the number of columns in matrix 2: "))
    
    # Create the two matrices and fill them with values
    matrix1 = Matrix(rows1, cols1)
    matrix2 = Matrix(rows2, cols2)
    for i in range(rows1):
        for j in range(cols1):
            matrix1.matrix[i][j] = int(input(f"Enter the value for matrix 1 at position ({i+1},{j+1}): "))
    for i in range(rows2):
        for j in range(cols2):
            matrix2.matrix[i][j] = int(input(f"Enter the value for matrix 2 at position ({i+1},{j+1}): "))
    
    # Print the matrices
    print("Matrix 1:")
    print(matrix1)
    print("Matrix 2:")
    print(matrix2)
    
    # Get the operation from the user
    operation = input("Enter 'add', 'subtract', or 'multiply' to perform the respective operation: ")
    
    # Perform the operation and print the result
    if operation == "add":
        result = matrix1.add(matrix2)
    elif operation == "subtract":
        result = matrix1.subtract(matrix2)
    elif operation == "multiply":
        result = matrix1.multiply(matrix2)
    else:
        result = "Invalid input"
    print("Result:")
    print(result)

if __name__ == "__main__":
    main()
