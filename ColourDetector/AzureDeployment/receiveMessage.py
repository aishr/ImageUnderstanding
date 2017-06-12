from azure.servicebus import ServiceBusService, Message, Topic, Rule, DEFAULT_RULE_NAME

bus_service = ServiceBusService(
    service_namespace = 'ashstoragebus11223334',
    shared_access_key_name = 'RootManageSharedAccessKey',
    shared_access_key_value = 'xBdj/QF1M86llL+8GXU4tVNVJJ4oQcHOg31MJ6pZSJI=')

for i in range(bus_service.get_subscription('colourin', 'isClassified').message_count):
    rmsg = bus_service.receive_subscription_message('colourin', 'isClassified', peek_lock = False)
    print(rmsg.body)
    print(rmsg.custom_properties["colour1"])
