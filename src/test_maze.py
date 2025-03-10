import unittest
from maze import Maze
from geometry import Point


class tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_unequal_size_cells(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(Point(0, 0), num_rows, num_cols, 20, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_destroy_entrance_and_exit(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(Point(0, 0), num_rows, num_cols, 20, 10)
        m1._break_entrance_and_exit()
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[-1][-1].has_bottom_wall, False)

    def test_maze_reset_visited(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(Point(0, 0), num_rows, num_cols, 20, 10)
        m1._break_entrance_and_exit()
        m1._break_wall_r(0, 0)
        m1._reset_cells_visited()
        for column in m1._cells:
            for cell in column:
                self.assertEqual(cell.visited, False)


if __name__ == "__main__":
    unittest.main()
