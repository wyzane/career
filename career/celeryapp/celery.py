from celery import Celery
from kombu import Queue, Exchange, binding


app = Celery("celeryapp")
app.config_from_object("celeryapp.config")


ex_default = Exchange('default', type="direct")
ex_tasks = Exchange('media', type='direct')

app.conf.task_queue = (
    Queue('default', ex_default, routing_key='default'),
    Queue('tasks', [
        binding(ex_tasks, routing_key="tasks1.test"),
        binding(ex_tasks, routing_key="tasks2.test"),
    ]),
)

app.conf.task_routes = {
    "celeryapp.tasks.*": {
        "queue": 'default',
        "routing_key": 'default'
    },
    "celeryapp.tasks1.*": {
        "queue": 'tasks',
        "routing_key": 'tasks1.test'
    },
    "celeryapp.tasks2.*": {
        "queue": 'tasks',
        "routing_key": 'tasks.test'
    },
    "celeryapp.tasks3.*": {
        "queue": 'tasks',
        "routing_key": 'tasks1.test'
    }
}


if __name__ == '__main__':
    app.start()
