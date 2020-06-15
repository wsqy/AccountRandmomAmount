import xadmin
from django.utils.html import format_html

from .models import  Task, TaskBatch, Transaction


class TaskAdmin:
    def download(self, obj):
        button_html = """<a class='changelink' href='{}'>下载本批次数据</a>""".format(obj.download_link)
        return format_html(button_html)
    download.short_description = '下载报表'

    add_form_template = 'xadmin/Tran/task/model_form.html'
    change_form_template = add_form_template
    list_display = ['date', 'batch_total', 'remark', 'status', 'download']
    readonly_fields = ['status',]
    empty_value_display = '无'

    def save_models(self):
        instance = self.new_obj
        if not instance.name:
            instance.name = instance.date.strftime('%Y-%m-%d任务')
        super(TaskAdmin, self).save_models()

class TaskBatchAdmin:
    list_display = ['task', 'num', 'batch_total', 'amount_total', 'remark', ]
    list_filter = ['task', ]
    empty_value_display = '无'

class TransactionAdmin:
    list_display = ['task', 'task_batch', 'buyer', 'seller', 'remark', ]
    list_filter = ['task', 'task_batch', ]
    empty_value_display = '无'

    def has_add_permission(self):
        return False

xadmin.site.register(Task, TaskAdmin)
xadmin.site.register(TaskBatch, TaskBatchAdmin)
xadmin.site.register(Transaction, TransactionAdmin)
