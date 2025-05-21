import os
from sparse_matrix import SparseMatrix


def main():
    print("Select matrix operation:")

    print("1. Addition")

    print("2. Subtraction")

    print("3. Multiplication (Fast)")

    print("4. Multiplication (Normal)")

    print("5. Display Sparse Matrix")

    choice = input("Enter your choice (1/2/3/4/5): ").strip()

    if choice not in {"1", "2", "3", "4", "5"}:
        return print("Invalid choice. Quitting...")

    matrix_file_1 = input(
        f"Enter the path of the{' first' if choice != '5' else ''} matrix file: "
    ).strip()

    matrix_file_2 = ""

    if choice != "5":
        matrix_file_2 = input("Enter the path of the second matrix file: ").strip()

    print("\n")
    if choice == "1":
        print("\033[93mLoading matrices and performing addition...\033[0m")
    elif choice == "2":
        print("\033[93mLoading matrices and performing subtraction...\033[0m")
    elif choice == "3":
        print("\033[93mLoading matrices and performing fast multiplication...\033[0m")
    elif choice == "4":
        print("\033[93mLoading matrices and performing normal multiplication...\033[0m")
    elif choice == "5":
        print("\033[93mLoading matrix and displaying...\033[0m")

    try:
        matrix1 = SparseMatrix(matrix_file_path=matrix_file_1)

        matrix2 = SparseMatrix(matrix_file_path=matrix_file_2)

        if choice == "5":
            return matrix1.display()

        output_file = ""

        directory = matrix_file_1.split("sample_inputs")[0]

        if choice == "1":
            result = matrix1.add(matrix2)

            output_file = f'{directory}/outputs/Addition of {matrix_file_1.split("/")[-1].split(".txt")[0]} and {matrix_file_2.split("/")[-1].split(".txt")[0]}.txt'

        elif choice == "2":
            result = matrix1.subtract(matrix2)

            output_file = f'{directory}/outputs/Subtraction of {matrix_file_2.split("/")[-1].split(".txt")[0]} from {matrix_file_1.split("/")[-1].split(".txt")[0]}.txt'

        elif choice == "3":
            result = matrix1.multiply_optimal(matrix2)

            output_file = f'{directory}/outputs/Multiplication of {matrix_file_1.split("/")[-1].split(".txt")[0]} and {matrix_file_2.split("/")[-1].split(".txt")[0]}.txt'

        elif choice == "4":
            result = matrix1.multiply_slow(matrix2)

            output_file = f'{directory}/outputs/Multiplication of {matrix_file_1.split("/")[-1].split(".txt")[0]} and {matrix_file_2.split("/")[-1].split(".txt")[0]}.txt'

        os.makedirs(f"{directory}/outputs", exist_ok=True)

        result.write_to_file(output_file)

        print("\n")
        print(f"\033[92mOperation successful! Result written to {output_file}\033[0m")

    except SyntaxError as error:
        print(f"Syntax Error: {error}")

    except FileNotFoundError:
        print("File Not Found Error: One or both input files were not found.")

    except Exception as error:
        print(f"Unexpected Error: An unexpected error occurred: {error}")


main()
