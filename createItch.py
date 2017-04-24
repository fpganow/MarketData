#!/usr/bin/env python3

from Itch41 import *


def generateMessages(messages):
    genMessages = [ ]
    for message in messages:
        msg = ItchMessageFactory.createFromArgs(message)
        if msg:
            genMessages.append(msg)
    return genMessages

def saveMessagesToFile(messages, fileName):
    print("Creating file: {}".format(fileName))
    import os
    if os.path.exists(fileName):
        os.remove(fileName)
    for message in messages:
        print("-- Dumping message to file {0} --".format(fileName))
        message.dumpPretty()
        message.appendToFile(fileName)

def create_Test_1():
    # Create 3 Add Order Messages
    # Execute Order #2
    outFile = "Itch.test1.dat"

    # Begin code for generating a bunch of messages
    messages = [ ]
    messages.append( [          MessageType.TimeStamp, {     Field.Seconds: 1000 } ] )
    messages.append( [           MessageType.AddOrder, { Field.NanoSeconds:   10, Field.OrderRefNum: 1, Field.Side: 'B', Field.Shares: 200, Field.Stock: "AAPL", Field.Price: 100.53 } ] )
    messages.append( [           MessageType.AddOrder, { Field.NanoSeconds:   20, Field.OrderRefNum: 2, Field.Side: 'B', Field.Shares: 300, Field.Stock: "AAPL", Field.Price: 100.55 } ] )
    messages.append( [           MessageType.AddOrder, { Field.NanoSeconds:   30, Field.OrderRefNum: 3, Field.Side: 'B', Field.Shares: 400, Field.Stock: "AAPL", Field.Price: 100.56 } ] )
    messages.append( [      MessageType.OrderExecuted, { Field.NanoSeconds:   40, Field.OrderRefNum: 2, Field.Shares: 300, Field.MatchNum: 1001 } ] )

    saveMessagesToFile( generateMessages( messages ), outFile )

def create_Test_2():
    # Create 3 Add Order Messages
    # Replace Order #3 with Order #4
    # Execute Order #4

    outFile = "Itch.test2.dat"

    messages = [ ]
    messages.append( [          MessageType.TimeStamp, {     Field.Seconds: 2000 } ] )
    messages.append( [           MessageType.AddOrder, { Field.NanoSeconds:   15, Field.OrderRefNum: 10, Field.Side: 'B', Field.Shares: 225, Field.Stock: "AAPL", Field.Price: 100.11 } ] )
    messages.append( [           MessageType.AddOrder, { Field.NanoSeconds:   25, Field.OrderRefNum: 20, Field.Side: 'B', Field.Shares: 325, Field.Stock: "AAPL", Field.Price: 100.12 } ] )
    messages.append( [           MessageType.AddOrder, { Field.NanoSeconds:   35, Field.OrderRefNum: 30, Field.Side: 'B', Field.Shares: 425, Field.Stock: "AAPL", Field.Price: 100.10 } ] )
    messages.append( [       MessageType.OrderReplace, { Field.NanoSeconds:   45, Field.OrderRefNum: 30, Field.NewOrderRefNum: 40, Field.Shares: 200, Field.Price: 100.52 } ] )
    messages.append( [      MessageType.OrderExecuted, { Field.NanoSeconds:   55, Field.OrderRefNum: 40, Field.Shares: 200, Field.MatchNum: 1001 } ] )

    saveMessagesToFile( generateMessages( messages ), outFile )

#messages.append( [ MessageType.OrderExecutedPrice, { Field.NanoSeconds:   1, Field.OrderRefNum: 1, Field.Shares: 200, Field.MatchNum: 101, Field.Printable: 'Y', Field.Price: 100.52 } ] )
#messages.append( [        MessageType.OrderCancel, { Field.NanoSeconds:   1, Field.OrderRefNum: 1, Field.Shares: 200 } ] )
#messages.append( [        MessageType.OrderDelete, { Field.NanoSeconds:   1, Field.OrderRefNum: 1} ] )

create_Test_1()
create_Test_2()

