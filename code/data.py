from code import utils
from code.row import Row
from code.cols import Cols

class Data:
    def __init__(self, src):
        rows_csv = utils.csv_function(src)
        self.cols = None  # summaries of data
        self.rows = []

        for row in rows_csv:
            self.rows.append(row)
        self.add(self.rows)

    # add cell to appropriate column
    def add(self, xs):
        if self.cols is None:
            self.cols = Cols(xs[0])
            self.rows.pop(0)
        for ky, todo_x in self.cols.x.items():
            for r in xs:
                for c in r:
                    if r.index(c) == ky:
                        row = Row(c)
                        todo_x.add(row.cells)
        for ky, todo_y in self.cols.y.items():
            for r in xs:
                for c in r:
                    if r.index(c) == ky:
                        row = Row(c)
                        todo_y.add(row.cells)

    def stats(self, places, showCols, fun):
        showCols, fun = showCols or self.cols.y, fun or "mid"
        t = {}
        for ky, col in showCols.items():
            v = fun(col)
            if type(v) is float:
                v = utils.rnd(v, places)
            t[col.name] = v
        return t
