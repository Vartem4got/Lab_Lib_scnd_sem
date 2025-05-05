from collections import deque
import ast

def flood_fill(matr, s_row, s_col, new_color, rows, cols):
    if not (0 <= s_row < rows and 0 <= s_col < cols):
        print(f"Bad start. Watch coordinates")
        return matr

    s_color = matr[s_row][s_col]

    if s_color == new_color:
        return matr

    q = deque([(s_row, s_col)])
    visi = set([(s_row, s_col)])
    direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while q:
        cur_row, cur_col = q.popleft()
        matr[cur_row][cur_col] = new_color

        for dr, dc in direct:
            new_row, new_col = cur_row + dr, cur_col + dc
            if 0 <= new_row < len(matr) and 0 <= new_col < len(matr[0]) and \
               matr[new_row][new_col] == s_color and \
               (new_row, new_col) not in visi:
                visi.add((new_row, new_col))
                q.append((new_row, new_col))

    return matr

def process_matrix(lines):
    if len(lines) < 3:
        raise ValueError("File empty/not enough lines.")

    dims_str = lines[0].strip().split(',')
    if len(dims_str) != 2:
        raise ValueError("Invalid format rows,cols")
    try:
        rows = int(dims_str[0])
        cols = int(dims_str[1])
    except ValueError:
        raise ValueError("Int!")

    coords_str = lines[1].strip().split(',')
    if len(coords_str) != 2:
        raise ValueError("Invalid start")
    try:
        s_row = int(coords_str[0])
        s_col = int(coords_str[1])
    except ValueError:
        raise ValueError("int!")

    new_color = lines[2].strip().strip("'")
    if not new_color:
        raise ValueError("color pls")

    matr = []
    for i, line in enumerate(lines[3:]):
        clear_line = line.strip()
        if not clear_line:
            continue
        try:
            row = ast.literal_eval(clear_line)
            if not isinstance(row, list):
                raise ValueError(f"Matrix row {i+1} is not a list.")
            if not row:
                raise ValueError(f"Matrix row {i+1} is empty.")
            matr.append(row)
        except (SyntaxError, ValueError) as e:
            raise ValueError(f"Error parsing matrix row {i+1}: '{clear_line}'. Details: {e}") # done by ai and i let it here for debugging

    if len(matr) != rows or (matr and len(matr[0]) != cols):
        raise ValueError("Dimensions do not match the matrix size.")

    return matr, s_row, s_col, new_color, rows, cols

def display_matrix(matrix):
    for row in matrix:
        print(' '.join(row))

def main():
    input_file = "input.txt"
    output_file = "output.txt"

    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        matr, start_row, start_col, color_to_fill, rows, cols = process_matrix(lines)

        print("Original Matrix:")
        display_matrix(matr)

        while True:
            try:
                coords_input = input("Enter rows,cols,color ( 2,9,G ) or q to exit - ").lower()
                if coords_input == 'q':
                    break

                parts = coords_input.split(',')
                if len(parts) != 3:
                    print("Please use row,col,color")
                    continue

                row_change, col_change, new_fill_color = parts[0].strip(), parts[1].strip(), parts[2].strip().upper()

                try:
                    row_change = int(row_change)
                    col_change = int(col_change)
                except ValueError:
                    print("Int!")
                    continue

                if not (0 <= row_change < rows and 0 <= col_change < cols):
                    print("Smaller cords")
                    continue

                modified_matr = flood_fill(matr, row_change, col_change, new_fill_color, rows, cols)

                print("\nMod matrix - ")
                display_matrix(modified_matr)

                with open(output_file, 'w') as outfile:
                    for row in modified_matr:
                        outfile.write(' '.join(row) + '\n')
                print(f"\nUpdt matrix to - {output_file}")

            except ValueError as ve:
                print(f"Error: {ve}")
            except Exception as e:
                print(f"I dk what")

    except FileNotFoundError:
        print(f"No input file")
    except ValueError as ve:
        print(f"Val error")
    except IndexError:
        print("File empty/not full")
    except SyntaxError:
        print("Bag synt")
    except Exception as e:
        print(f"File error")

if __name__ == "__main__":
    main()