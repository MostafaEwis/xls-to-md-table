import xlrd;
from mdutils.mdutils import MdUtils
import sys

filename = sys.argv[1];
mdout = sys.argv[2];

book = xlrd.open_workbook(filename);
sheet = book.sheet_by_name("Sheet1")
md = MdUtils(file_name=mdout)

data = []

for j in range(0, sheet.nrows):
    for i in range(0, sheet.ncols):
        data.append(sheet.cell_value(j, i));


md.new_table(columns=sheet.ncols, rows=sheet.nrows, text=data, text_align='left');
md.create_md_file();
book.release_resources();
del book;