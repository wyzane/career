broker_url = "amqp://192.168.0.103"
result_backend = "redis://:wyzane@192.168.0.103"
include = ["celeryapp.tasks", "celeryapp.tasks1", "celeryapp.tasks2", "celeryapp.tasks3"]

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
enable_utc = True

task_default_queue = 'default'
task_default_exchange = 'default'
task_default_routing_key = 'default'
