import xadmin
from django.utils.html import format_html
from .models import Task, TaskBatch, Transaction
from .utils import get_download_zipfile, get_download_excelfile



class TaskAdmin:
    def download(self, obj):
        button_html = "<a class='changelink' href={}>下载</a>".format(get_download_zipfile(obj))
        return format_html(button_html)
    download.short_description = '下载汇总文件'

    list_display = ['date', 'batch_total', 'status', 'download']
    # empty_value_display = '无'
    exclude = ['file_no',]
    model_icon = 'fa fa-tasks'

    def get_context(self):
        context = super(TaskAdmin, self).get_context()
        context.update({
            'show_save_as_new': False, 
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete_link': False,
        })
        return context

    def get_readonly_fields(self, obj=None):
        if 'update' in self.request.path:
            return  ['amount_total_min', 'amount_total_max', 'batch_num_min', \
                     'batch_num_max', 'batch_total','status', 'remark']
        else:
            return ['status',]


class TaskBatchAdmin:
    def download_zz(self, obj):
        button_html = "<a class='changelink' href={}>下载</a>".format(get_download_excelfile(obj, '转账文件'))
        return format_html(button_html)

    def download_hz(self, obj):
        button_html = "<a class='changelink' href={}>下载</a>".format(get_download_excelfile(obj, '转账信息'))
        return format_html(button_html)

    download_zz.short_description = '下载转账文件'
    download_hz.short_description = '下载转账信息'
    list_display = ['task', 'num', 'batch_total', 'amount_total', 'download_zz', 'download_hz']
    list_filter = ['task', ]
    readonly_fields = ['task', 'num', 'batch_total', 'amount_total',]
    empty_value_display = '无'
    model_icon = 'fa fa-info'

    def has_add_permission(self):
        return False

    def get_context(self):
        context = super(TaskBatchAdmin, self).get_context()
        context.update({
            'show_save': False,
            'show_save_as_new': False, 
            'show_save_and_continue': False, 
            'show_delete_link': False,
        })
        return context

class TransactionAdmin:
    list_display = ['task', 'task_batch', 'buyer', 'seller', 'amount', ]
    list_filter = ['task', 'task_batch', ]
    readonly_fields = ['task', 'task_batch', 'buyer', 'seller', 'amount', ]
    empty_value_display = '无'
    model_icon = 'fa fa-archive'

    def has_add_permission(self):
        return False

    def get_context(self):
        context = super(TransactionAdmin, self).get_context()
        context.update({
            'show_save': False,
            'show_save_as_new': False, 
            'show_save_and_continue': False, 
            'show_delete_link': False,
        })
        return context

xadmin.site.register(Task, TaskAdmin)
xadmin.site.register(TaskBatch, TaskBatchAdmin)
xadmin.site.register(Transaction, TransactionAdmin)
