import xadmin
from django.utils.html import format_html
from .models import  Task, TaskBatch, Transaction

class TaskAdmin:
    def download(self, obj):
        button_html = """<a class='changelink' href='{}'>下载本批次数据</a>""".format(obj.download_link)
        return format_html(button_html)
    download.short_description = '下载报表'

    list_display = ['date', 'batch_total', 'remark', 'status', 'download']
    empty_value_display = '无'

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
                     'batch_num_max', 'batch_total','status','remark', 'download_link']
        else:
            return ['status',]


class TaskBatchAdmin:
    list_display = ['task', 'num', 'batch_total', 'amount_total', 'remark', ]
    list_filter = ['task', ]
    readonly_fields = ['task', 'num', 'batch_total', 'amount_total', 'remark',]
    empty_value_display = '无'

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
    list_display = ['task', 'task_batch', 'buyer', 'seller', 'amount', 'remark', ]
    list_filter = ['task', 'task_batch', ]
    readonly_fields = ['task', 'task_batch', 'buyer', 'seller', 'amount', 'remark', ]
    empty_value_display = '无'

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
