from azure.servicebus import *
from colourFunctions import ColourFunctions
class AzureColourSuite ():

    BusService = ServiceBusService(
        service_namespace = 'ashstoragebus11223334',
        shared_access_key_name = 'RootManageSharedAccessKey',
        shared_access_key_value = 'xBdj/QF1M86llL+8GXU4tVNVJJ4oQcHOg31MJ6pZSJI=')

    def RendMessage(self, msgStr, properties, topic):
        msg = Message(str(msgStr), custom_properties = properties)
        self.BusService.send_topic_message(topic, msg)

    def ReceiveMessage(self, topic, sub, peekStat):
        colourDict = {}
        totalMessagecount = self.BusService.get_subscription(topic, sub).message_count
        for i in range(totalMessagecount):
            rmsg = self.BusService.receive_subscription_message(topic, sub, peek_lock = peekStat)
            colourList = []
            for j in range(rmsg.custom_properties["colourcount"]): 
                colourList.append(rmsg.custom_properties["colour" + str(j+1)])
            colourDict[rmsg.custom_properties["sku"]] = colourList

        return colourDict

    def attachColour(self, rTopic, rSub, peekStat, sTopic):
        totalMessageCount = self.BusService.get_subscription(rTopic, rSub).message_count
        colours = ColourFunctions("finalDictionary.csv")
        for i in range(totalMessageCount):
            msg = self.BusService.receive_subscription_message(rTopic, rSub, peek_lock = peekStat)
            itemSKU = str(msg.custom_properties["sku"])
            itemImgUrl = 'https://dynamic.indigoimages.ca/gifts/' + itemSKU + '.jpg?maxheight=240&width=228&quality=85&sale=25&lang=en'
            image = colours.URLToImage(itemImgUrl)
            colourList = colours.detectColour(image)
            properties = {}
            for j in range(len(colourList)):
                properties["colour" + str(j+1)] = colourList[j]

            sMsg = Message(itemSKU, custom_properties = properties)
            self.BusService.send_topic_message(sTopic, sMsg)
