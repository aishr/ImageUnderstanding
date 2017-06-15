from azure.servicebus import ServiceBusService, Message, Topic, Rule, DEFAULT_RULE_NAME

bus_service = ServiceBusService(
    service_namespace = 'ashstoragebus11223334',
    shared_access_key_name = 'RootManageSharedAccessKey',
    shared_access_key_value = 'xBdj/QF1M86llL+8GXU4tVNVJJ4oQcHOg31MJ6pZSJI=')

skus = [657284666103, 732396464226, 630870129497, 5060121267558, 778988128503, 670983079739]

for sku in skus:
    properties = {}
    propName = "sku"
    properties[propName] = sku
    msg = Message(str(sku), custom_properties = properties)
    bus_service.send_topic_message('colourout', msg)
    print("message sent")
