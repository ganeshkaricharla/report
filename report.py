import xlsxwriter
from datetime import datetime

now = datetime.now().strftime("D%d%m%YT%H%M%S");

workbook = xlsxwriter.Workbook('report-'+now + '.xlsx')
worksheet = workbook.add_worksheet("Image1")

# Widen the first column to make the text clearer.
# worksheet.set_column('A:A', 30)

# Insert an image.
# worksheet.write('A2', 'Insert an image in a cell:')
worksheet.insert_image('A1', 'download.jpeg')

# # Insert an image offset in the cell.
# worksheet.write('A12', 'Insert an image with an offset:')
# worksheet.insert_image('B12', 'python.png', {'x_offset': 15, 'y_offset': 10})

# # Insert an image with scaling.
# worksheet.write('A23', 'Insert a scaled image:')
# worksheet.insert_image('B23', 'python.png', {'x_scale': 0.5, 'y_scale': 0.5})
worksheet = workbook.add_worksheet("IMage2")

# Widen the first column to make the text clearer.
# worksheet.set_column('A:A', 30)

# Insert an image.
# worksheet.write('A2', 'Insert an image in a cell:')
worksheet.insert_image('A1', 'download.jpeg')
workbook.close()