from azure.servicebus import ServiceBusService, Message, Topic, Rule, DEFAULT_RULE_NAME

bus_service = ServiceBusService(
    service_namespace = 'ashstoragebus11223334',
    shared_access_key_name = 'RootManageSharedAccessKey',
    shared_access_key_value = 'xBdj/QF1M86llL+8GXU4tVNVJJ4oQcHOg31MJ6pZSJI=')

bus_service.create_topic('newTestingTopic')

bus_service.create_subscription('newTestingTopic', 'ColourMessages')

