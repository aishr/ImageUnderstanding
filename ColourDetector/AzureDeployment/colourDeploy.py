from azure.servicebus import *
from colourFunctions import * 

bus_service = ServiceBusService(
    service_namespace = 'ashstoragebus11223334',
    shared_access_key_name = 'RootManageSharedAccessKey',
    shared_access_key_value = 'xBdj/QF1M86llL+8GXU4tVNVJJ4oQcHOg31MJ6pZSJI=')

def getAndSendToAzure(serviceBus:ServiceBusService, topic, subscription):

    totalMessageCount = serviceBus.get_subscription(topic, subscription).message_count

    for i in range(totalMessageCount):
        msg = serviceBus.receive_subscription_message(topic, subscription, peek_lock = False)
        SKU = msg.custom_properties["SKU"]
        imgURL = 'https://dynamic.indigoimages.ca/gifts/' + SKU + '.jpg?maxheight=240&width=228&quality=85&sale=25&lang=en'
        image = URLToImage(imgURL)
        colourList = detectColour(image)
        properties = {}
        for i in range(len(colourList)):
            propName = "colour" + str(i+1)
            properties[propName] = colourList[i]

        newMsg = Message(SKU, custom_properties = properties)
        serviceBus.send_topic_message(topic, newMsg)
