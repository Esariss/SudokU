from sudoku import Sudoku

if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.generate_map_vals()
    sudoku.hide_cells()

    print(*sudoku.sudoku_map, sep="\n")
    print("============================")
    print(*sudoku.playable_sudoku_map, sep="\n")
