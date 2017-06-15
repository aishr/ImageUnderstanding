from azure.servicebus import *
from colourFunctions import * 

bus_service = ServiceBusService(
    service_namespace = 'ashstoragebus11223334',
    shared_access_key_name = 'RootManageSharedAccessKey',
    shared_access_key_value = 'xBdj/QF1M86llL+8GXU4tVNVJJ4oQcHOg31MJ6pZSJI=')

def getAndSendToAzure(serviceBus:ServiceBusService, topicIn, subIn, topicOut):

    totalMessageCount = serviceBus.get_subscription(topicIn, subIn).message_count

    for i in range(totalMessageCount):
        msg = serviceBus.receive_subscription_message(topicIn, subIn, peek_lock = False)
        propCheck = 'sku'
        SKU = str(msg.custom_properties[propCheck])
        imgURL = 'https://dynamic.indigoimages.ca/gifts/' + SKU + '.jpg?maxheight=240&width=228&quality=85&sale=25&lang=en'
        image = URLToImage(imgURL)
        colourList = detectColour(image, "../Dictionaries/finalDictionary.csv")
        properties = {}
        for j in range(len(colourList)):
            propName = "colour" + str(j+1)
            properties[propName] = colourList[j]

        newMsg = Message(SKU, custom_properties = properties)
        serviceBus.send_topic_message(topicOut, newMsg)


if __name__ == '__main__':
    getAndSendToAzure(bus_service, "colourout", "pleaseClassify", "colourin")
