import xlwt

workbook = xlwt.Workbook(encoding="utf-8") #创建workbook对象
worksheet = workbook.add_sheet("sheet1")

#9 * 9乘法表
for i in range(0,9):
    # for j in range(0,i+1):
    #     worksheet.write(i, j, str((i + 1) * (j + 1)))  网课方法
    for j in range(0,9):
        if j <= i:
            worksheet.write(i,j,str((i+1) * (j+1)))  #写入数据，第一个参数表示行（0开始），第二个参数表示列，第三个参数是内容

workbook.save("TestXlwt.xlsx")
