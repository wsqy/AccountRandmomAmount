import os
import glob
import zipfile
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, numbers


class CreateExcel:
    def __init__(self, task):
        self.date = task.date
        self.date_year = self.date.strftime('Y')
        self.date_month = self.date.strftime('m')
        self.date_day = self.date.strftime('d')
        self.random_str = task.file_no
        self.date_str = self.date.strftime('%Y-%m-%d')
        self.filepath = self.date.strftime('%Y-%m{0}%d{0}'.format(os.sep))
        
        self.filename_content = '{}-{}'.format(self.date_str, self.random_str)
        self.filename = '{}-汇总.xlsx'.format(self.filename_content)
        self.all_center = Alignment(horizontal='center', vertical='center')
        self.workbook = Workbook()

        # 创建一张新表
        self.worksheet = self.workbook.active
        self.header()
        try:
            os.makedirs(self.filepath)
            # print()
        except Exception as e:
            pass

    def close(self):
        self.workbook.save("{}{}".format(self.filepath, self.filename))

    def header(self):
        """
        """
        # 填充汇总表 文字为居中
        self.worksheet['A1'].alignment = self.all_center
        self.worksheet['B1'].alignment = self.all_center
        self.worksheet['C1'].alignment = self.all_center

    def insert(self):
        pass

    def footer(self):
        pass

    def creat_zipfile(self):
        file_list = glob.iglob(r'{}*{}*.xlsx'.format(self.filepath, self.random_str))
        z = zipfile.ZipFile('{}{}.zip'.format(self.filepath, self.filename_content), 'w') 
        for file in file_list:
            z.write(file, file.replace(self.filepath, ''))
        z.close()


class FujianHuizongExcel(CreateExcel):
    """
    """
    def header(self):
        """
        """
        super(FujianHuizongExcel,self).header()
        # 添加表头
        self.worksheet['A1'] = '表格名称'
        self.worksheet['B1'] = '汇总金额(万元)'
        self.worksheet['C1'] = '笔数'
        # 调整表格宽度
        self.worksheet.column_dimensions['A'].width = 25+2
        self.worksheet.column_dimensions['B'].width = 12+2
        self.worksheet.column_dimensions['C'].width = 4+2
    
    def insert(self, instance):
        i = str(instance.num+1)
        # 填充汇总表数据
        self.worksheet['A%s'% i ] = '{}-{}.xlsx'.format(self.filename_content, instance.num)
        self.worksheet['B%s'% i ] = instance.amount_total
        self.worksheet['C%s'% i ] = instance.batch_total

        # 填充汇总表 文字为居中
        self.worksheet['A%s'% i ].alignment = self.all_center
        self.worksheet['B%s'% i ].alignment = self.all_center
        self.worksheet['C%s'% i ].alignment = self.all_center


class JiangxiHuizongExcel(CreateExcel):
    pass


class TranExcel(CreateExcel):
    def __init__(self, taskbatch):
        task = taskbatch.task
        super(TranExcel,self).__init__(task)
        self.filename_content = '{}-{}-转账文件-{}'.format(self.date_str, self.random_str, taskbatch.num)
        self.filename = '{}.xlsx'.format(self.filename_content)

    def close(self):
        self.workbook.save("{}{}".format(self.filepath, self.filename))
        pass

    def header(self):
        pass

    def footer(self):
        pass


class FujianTranExcel(TranExcel):
    """
    """
    def header(self):
        """
        """
        super(FujianTranExcel,self).header()
        # 添加表头
        self.worksheet['A1'] = '账户账号'
        self.worksheet['B1'] = '转账金额(万元)'
        self.worksheet['C1'] = '备注'
        # 调整表格宽度
        self.worksheet.column_dimensions['A'].width = 15+2
        self.worksheet.column_dimensions['B'].width = 12+2
        self.worksheet.column_dimensions['C'].width = 10+2
    
    def insert(self, i, instance, account):
        """
        """
        self.worksheet['A%s'% i] = account.account
        self.worksheet['A%s'% i].alignment = self.all_center
        self.worksheet['A%s'% i].number_format = numbers.FORMAT_TEXT
        self.worksheet['B%s'% i] = instance.amount
        self.worksheet['B%s'% i].alignment = self.all_center
        self.worksheet['C%s'% i] = instance.task.remark
        self.worksheet['C%s'% i].alignment = self.all_center


class TranInfoExcel(TranExcel):
    def __init__(self, taskbatch):
        super(TranInfoExcel,self).__init__(task, random_str)
        self.filename_content = '{}-{}-转账信息-{}'.format(self.date_str, self.random_str, taskbatch.num)
        self.filename = '{}.xlsx'.format(self.filename_content)

    def close(self):
        self.workbook.save("{}{}".format(self.filepath, self.filename))
        pass

    def header(self):
        pass

    def insert(self):
        pass


def test():
    from Tran.models import Task, TaskBatch, Transaction
    task = Task.objects.get(id=6)
    tran_huizong_excel = FujianHuizongExcel(task)
    for i, taskbatch in enumerate(TaskBatch.objects.filter(task=task), 1):
        tran_huizong_excel.insert(taskbatch)
        tran_excel = FujianTranExcel(taskbatch)
        # print(tran_excel.filename)
        for j, transaction in enumerate(Transaction.objects.filter(task_batch=taskbatch), 2):
            tran_excel.insert(j, transaction)
        tran_excel.close()
    tran_huizong_excel.close()
    tran_huizong_excel.creat_zipfile()


if __name__ == '__main__':
    test()
    