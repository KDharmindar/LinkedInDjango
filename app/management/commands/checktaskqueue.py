from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from app.models import BotTask, BotTaskStatus, BotTaskType
from connector.models import TaskQueue


class Command(BaseCommand):
    help = 'collect_search : it will process all pending search results'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        pending_task_list = BotTask.objects.exclude(status__in=[BotTaskStatus.DONE, BotTaskStatus.ERROR])
        for pending_task in pending_task_list:
            queue_type = ContentType.objects.get_for_model(pending_task)
            task_queue = TaskQueue.objects.filter(object_id=pending_task.id, queue_type=queue_type)
            if task_queue:
                for task in task_queue:
                    pending_task.status = task.status
                    pending_task.save()
            else:
                TaskQueue(content_object=pending_task).save()
                
    #     self.check_taskqueue()
    #
    # def check_taskqueue(self):
    #     task_queues = TaskQueue.objects.filter(status=BotTaskStatus.QUEUED).all()
    #     for tq in task_queues:
    #         print('adding:', tq)
    #         BotTask.objects.create(name=tq.content_object, task_type=BotTaskType.SEARCH,
    #                                owner=tq.owner, status=tq.status)
    #