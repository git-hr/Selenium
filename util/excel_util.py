import xlrd
from xlutils.copy import copy
class ExcelUtil():
    def __init__(self,excel_path = '',index = None):
        if excel_path == '':
            excel_path = 'D:\workspace\python\config\case_data.xls'
        if index == None:
            index = 0
        self.excel_path = excel_path
        self.index = index
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[self.index]
        
    
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows != None:
            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        else:
            return None
    # 获取excel行数
    def get_lines(self):
        # 行数
        rows = self.table.nrows
        if rows >= 1:
            return rows
        else:
            return None

    # 获取单元格数据
    def get_col_value(self,row,cell):
        if self.get_lines() > row:
            data = self.table.cell(row,cell).value
            return data
        else:
            return None

    # 写入数据
    def write_value(self,row,value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(self.index).write(row,9,value)
        write_data.save(self.excel_path)
