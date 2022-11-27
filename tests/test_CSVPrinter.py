import unittest
import csv
# from CSVPrinter import CSVPrinter

class CSVPrinter:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        with open(self.file_name) as f:
            reader = csv.reader(f)
            lines = [row for row in reader]
        return lines


class TestCSVPrinter(unittest.TestCase):

    def test_read(self):
        printer = CSVPrinter("./sample.csv")
        l = printer.read()
        self.assertEqual(3, len(l))
    
    def test_read1(self):
        printer = CSVPrinter("./sample.csv")
        line = printer.read()
        print(line)
        self.assertEqual(3, len(line))
    
    def test_read2(self):
        printer = CSVPrinter("./sample.csv")
        line = printer.read()
        self.assertEqual(" value2B", line[1][1])
    
    def test_read3(self):
        try:
            printer = CSVPrinter("./sample.csv")
            line = printer.read()
        except Exception as e:
            self.fail(e)
            


if __name__ == "__main__":
    unittest.main()
