import xadmin
from django.utils.html import format_html
from .models import Task, TaskBatch, Transaction
from .utils import get_download_zipfile, get_download_excelfile
from .forms import TaskForm



class TaskAdmin:
    def download(self, obj):
        if obj.status:
            button_html = "<a class='changelink' href={}>下载</a>".format(get_download_zipfile(obj))
        else:
            button_html = "<p class='changelink' >异常, 请检查条件重新添加任务</p>"
        return format_html(button_html)
    download.short_description = '下载汇总文件'

    list_display = ['name', 'date', 'batch_total', 'corporation', 'status', 'download']
    # empty_value_display = '无'
    exclude = ['file_no',]
    model_icon = 'fa fa-tasks'
    list_filter = ['corporation', 'status', 'date']
    search_fields = ['name']
    ordering = ['-date', '-id']
    form = TaskForm

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
        if obj.task.status:
            button_html = "<a class='changelink' href={}>下载</a>".format(get_download_excelfile(obj, '转账文件'))
        else:
            button_html = "<p class='changelink' >异常, 请检查条件重新添加任务</p>"
        return format_html(button_html)

    download_zz.short_description = '下载转账文件'
    list_display = ['task', 'num', 'batch_total', 'amount_total', 'download_zz']
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
    def company(self, obj):
        return obj.buyer.company
    company.short_description = '代定人账号'
    
    list_display = ['order_no', 'task', 'task_batch', 'buyer', 'seller', 'company', ]
    list_filter = ['task', 'task_batch', 'buyer', 'seller', 'order_no']
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
