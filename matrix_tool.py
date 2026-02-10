import numpy as np

def input_matrix(name):
    """Function to input a matrix from user."""
    print(f"Enter details for matrix {name}:")
    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))
    print(f"Enter the elements row by row (space-separated):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print("Error: Incorrect number of columns. Try again.")
            return input_matrix(name)
        matrix.append(row)
    return np.array(matrix)

def display_matrix(matrix, name):
    """Function to display a matrix in a structured format."""
    print(f"\n{name}:")
    print(matrix)
    print()

def main():
    print("Welcome to the Matrix Operations Tool!")
    print("This tool uses NumPy for matrix operations.\n")

    # Input matrices
    matrix_a = input_matrix("A")
    matrix_b = input_matrix("B")

    display_matrix(matrix_a, "Matrix A")
    display_matrix(matrix_b, "Matrix B")

    while True:
        print("Available operations:")
        print("1. Addition (A + B)")
        print("2. Subtraction (A - B)")
        print("3. Multiplication (A * B)")
        print("4. Transpose of A")
        print("5. Transpose of B")
        print("6. Determinant of A")
        print("7. Determinant of B")
        print("8. Exit")

        choice = input("Choose an operation (1-8): ").strip()

        if choice == '1':
            if matrix_a.shape == matrix_b.shape:
                result = matrix_a + matrix_b
                display_matrix(result, "A + B")
            else:
                print("Error: Matrices must have the same dimensions for addition.\n")

        elif choice == '2':
            if matrix_a.shape == matrix_b.shape:
                result = matrix_a - matrix_b
                display_matrix(result, "A - B")
            else:
                print("Error: Matrices must have the same dimensions for subtraction.\n")

        elif choice == '3':
            if matrix_a.shape[1] == matrix_b.shape[0]:
                result = np.dot(matrix_a, matrix_b)
                display_matrix(result, "A * B")
            else:
                print("Error: Number of columns in A must equal number of rows in B for multiplication.\n")

        elif choice == '4':
            result = matrix_a.T
            display_matrix(result, "Transpose of A")

        elif choice == '5':
            result = matrix_b.T
            display_matrix(result, "Transpose of B")

        elif choice == '6':
            if matrix_a.shape[0] == matrix_a.shape[1]:
                det = np.linalg.det(matrix_a)
                print(f"\nDeterminant of A: {det}\n")
            else:
                print("Error: Matrix A must be square for determinant calculation.\n")

        elif choice == '7':
            if matrix_b.shape[0] == matrix_b.shape[1]:
                det = np.linalg.det(matrix_b)
                print(f"\nDeterminant of B: {det}\n")
            else:
                print("Error: Matrix B must be square for determinant calculation.\n")

        elif choice == '8':
            print("Thank you for using the Matrix Operations Tool!")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()