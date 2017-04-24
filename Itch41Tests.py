#!/usr/bin/env python3

import unittest

from Itch41 import *

class Create_Itch41_Messages_Test(unittest.TestCase):
    """ Tests for creating, parsing and dumping Itch 41 messages """

    def test_create_TimeStamp(self):
        # GIVEN
        messageArgs = [ MessageType.TimeStamp, { Field.Seconds: 100 } ]

        # WHEN
        message = ItchMessageFactory.createFromArgs( messageArgs )

        # THEN
        self.assertEqual( 'T', message.MessageType )
        self.assertEqual( 100, message.Seconds )

    def test_create_SystemEvent(self):
        # GIVEN
        messageArgs = [ MessageType.SystemEvent, {
                                Field.NanoSeconds    :      105,
                                Field.EventCode      :       'O'
                             } ]

        # WHEN
        message = ItchMessageFactory.createFromArgs( messageArgs )

        # THEN
        self.assertEqual(      'S', message.MessageType )
        self.assertEqual(      105, message.NanoSeconds )
        self.assertEqual(      'O', message.EventCode )

    def test_create_StockDirectory(self):
        # GIVEN
        messageArgs = [ MessageType.StockDirectory, {
                                Field.NanoSeconds      :      105,
                                Field.Stock            :   "AAPL",
                                Field.MarketCategory   :      'Q',
                                Field.FinancialStatus  :      ' ',
                                Field.RoundLotSize     :       50,
                                Field.RoundLotsOnly    :      'Y',
                             } ]

        # WHEN
        message = ItchMessageFactory.createFromArgs( messageArgs )

        # THEN
        self.assertEqual(      'R', message.MessageType )
        self.assertEqual(      105, message.NanoSeconds )
        self.assertEqual(   "AAPL", message.Stock )
        self.assertEqual(      'Q', message.MarketCategory )
        self.assertEqual(      ' ', message.FinancialStatus )
        self.assertEqual(       50, message.RoundLotSize )
        self.assertEqual(      'Y', message.RoundLotsOnly )

    def test_create_StockTradingAction(self):
        # GIVEN
        messageArgs = [ MessageType.StockTradingAction, {
                                Field.NanoSeconds      :      105,
                                Field.Stock            :   "AAPL",
                                Field.TradingState     :      'T',
                                Field.Reserved         :      ' ',
                                Field.Reason           :   "1234",
                             } ]

        # WHEN
        message = ItchMessageFactory.createFromArgs( messageArgs )

        # THEN
        self.assertEqual(      'H', message.MessageType )
        self.assertEqual(      105, message.NanoSeconds )
        self.assertEqual(   "AAPL", message.Stock )
        self.assertEqual(      'T', message.TradingState )
        self.assertEqual(      ' ', message.Reserved )
        self.assertEqual(   "1234", message.Reason )

    def test_create_RegSHORestriction(self):
        # GIVEN
        messageArgs = [ MessageType.RegSHORestriction, {
                                Field.NanoSeconds      :      105,
                                Field.Stock            :   "AAPL",
                                Field.RegSHOAction     :      '0',
                             } ]

        # WHEN
        message = ItchMessageFactory.createFromArgs( messageArgs )

        # THEN
        self.assertEqual(      'Y', message.MessageType )
        self.assertEqual(      105, message.NanoSeconds )
        self.assertEqual(   "AAPL", message.Stock )
        self.assertEqual(      '0', message.RegSHOAction )

    def test_create_MarketParticipantPosition(self):
        # GIVEN
        messageArgs = [ MessageType.MarketParticipantPosition, {
                                Field.NanoSeconds             :      105,
                                Field.Mpid                    :   "mpid",
                                Field.Stock                   :   "AAPL",
                                Field.PrimaryMarketMaker      :      'Y',
                                Field.MarketMakerMode         :      'N',
                                Field.MarketParticipantState  :      'A',
                             } ]

        # WHEN
        message = ItchMessageFactory.createFromArgs( messageArgs )

        # THEN
        self.assertEqual(        'L', message.MessageType )
        self.assertEqual(        105, message.NanoSeconds )
        self.assertEqual(     "mpid", message.Mpid )
        self.assertEqual(     "AAPL", message.Stock )
        self.assertEqual(        'Y', message.PrimaryMarketMaker )
        self.assertEqual(        'N', message.MarketMakerMode )
        self.assertEqual(        'A', message.MarketParticipantState )

    def test_create_AddOrder(self):
        # GIVEN
        messageArgs = [ MessageType.AddOrder, {
                                Field.NanoSeconds : 101,
                                Field.OrderRefNum : 1001,
                                Field.Side : 'B',
                                Field.Shares : 300,
                                Field.Stock : "AAPL",
                                Field.Price : 100.99
                             } ]

        # WHEN
        message = ItchMessageFactory.createFromArgs( messageArgs )

        # THEN
        self.assertEqual(     'A', message.MessageType )
        self.assertEqual(     101, message.NanoSeconds )
        self.assertEqual(    1001, message.OrderRefNum )
        self.assertEqual(     'B', message.Side )
        self.assertEqual(     300, message.Shares )
        self.assertEqual(  "AAPL", message.Stock )
        self.assertEqual(  100.99, message.Price )

    def test_create_AddOrder_with_Mpid(self):
        # GIVEN
        messageArgs = [ MessageType.AddOrderWithMPID, {
                                Field.NanoSeconds : 101,
                                Field.OrderRefNum : 1001,
                                Field.Side : 'B',
                                Field.Shares : 300,
                                Field.Stock : "AAPL",
                                Field.Price : 100.99,
                                Field.Mpid : "MyId"
                             } ]

        # WHEN
        message = ItchMessageFactory.createFromArgs( messageArgs )

        # THEN
        self.assertEqual(     'F', message.MessageType )
        self.assertEqual(     101, message.NanoSeconds )
        self.assertEqual(    1001, message.OrderRefNum )
        self.assertEqual(     'B', message.Side )
        self.assertEqual(     300, message.Shares )
        self.assertEqual(  "AAPL", message.Stock )
        self.assertEqual(  100.99, message.Price )
        self.assertEqual(  "MyId", message.Mpid )

    def test_create_OrderExecuted(self):
        # GIVEN
        messageArgs = [ MessageType.OrderExecuted, {
                                Field.NanoSeconds : 104,
                                Field.OrderRefNum : 1002,
                                Field.Shares : 350,
                                Field.MatchNum : 123,
                             } ]

        # WHEN
        message = ItchMessageFactory.createFromArgs( messageArgs )

        # THEN
        self.assertEqual(     'E', message.MessageType )
        self.assertEqual(     104, message.NanoSeconds )
        self.assertEqual(    1002, message.OrderRefNum )
        self.assertEqual(     350, message.Shares )
        self.assertEqual(     123, message.MatchNum )

    def test_create_OrderExecuted_with_Price(self):
        # GIVEN
        messageArgs = [ MessageType.OrderExecutedWithPrice, {
                                Field.NanoSeconds : 154,
                                Field.OrderRefNum : 1003,
                                Field.Shares : 375,
                                Field.MatchNum : 124,
                                Field.Printable : 'Y',
                                Field.Price: 123.2501
                             } ]

        # WHEN
        message = ItchMessageFactory.createFromArgs( messageArgs )

        # THEN
        self.assertEqual(       'C', message.MessageType )
        self.assertEqual(       154, message.NanoSeconds )
        self.assertEqual(      1003, message.OrderRefNum )
        self.assertEqual(       375, message.Shares )
        self.assertEqual(       124, message.MatchNum )
        self.assertEqual(  123.2501, message.Price )

    def test_create_OrderCancel(self):
        # GIVEN
        messageArgs = [ MessageType.OrderCancel, {
                                Field.NanoSeconds : 164,
                                Field.OrderRefNum : 1004,
                                Field.Shares : 400
                             } ]

        # WHEN
        message = ItchMessageFactory.createFromArgs( messageArgs )

        # THEN
        self.assertEqual(       'X', message.MessageType )
        self.assertEqual(       164, message.NanoSeconds )
        self.assertEqual(      1004, message.OrderRefNum )
        self.assertEqual(       400, message.Shares )

    def test_create_OrderDelete(self):
        # GIVEN
        messageArgs = [ MessageType.OrderDelete, {
                                Field.NanoSeconds : 165,
                                Field.OrderRefNum : 1005
                             } ]

        # WHEN
        message = ItchMessageFactory.createFromArgs( messageArgs )

        # THEN
        self.assertEqual(       'D', message.MessageType )
        self.assertEqual(       165, message.NanoSeconds )
        self.assertEqual(      1005, message.OrderRefNum )

    def test_create_OrderReplace(self):
        # GIVEN
        messageArgs = [ MessageType.OrderReplace, {
                                Field.NanoSeconds    :      175,
                                Field.OrderRefNum    :     1006,
                                Field.NewOrderRefNum :     1007,
                                Field.Shares         :      500,
                                Field.Price          : 123.2501
                             } ]

        # WHEN
        message = ItchMessageFactory.createFromArgs( messageArgs )

        # THEN
        self.assertEqual(       'U', message.MessageType )
        self.assertEqual(       175, message.NanoSeconds )
        self.assertEqual(      1006, message.OrderRefNum )
        self.assertEqual(      1007, message.NewOrderRefNum )
        self.assertEqual(       500, message.Shares )
        self.assertEqual(  123.2501, message.Price )

    def test_create_TradeNonCross(self):
        # GIVEN
        messageArgs = [ MessageType.TradeNonCross, {
                                Field.NanoSeconds    :      175,
                                Field.OrderRefNum    :     1006,
                                Field.Side           :      'B',
                                Field.Shares         :      300,
                                Field.Stock          :   "AAPL",
                                Field.Price          : 123.2501,
                                Field.MatchNum       :      400,
                             } ]

        # WHEN
        message = ItchMessageFactory.createFromArgs( messageArgs )

        # THEN
        self.assertEqual(        'P', message.MessageType )
        self.assertEqual(        175, message.NanoSeconds )
        self.assertEqual(       1006, message.OrderRefNum )
        self.assertEqual(        'B', message.Side )
        self.assertEqual(        300, message.Shares )
        self.assertEqual(     "AAPL", message.Stock )
        self.assertEqual(   123.2501, message.Price )
        self.assertEqual(        400, message.MatchNum )

    def test_create_CrossTrade(self):
        # GIVEN
        messageArgs = [ MessageType.CrossTrade, {
                                Field.NanoSeconds    :      175,
                                Field.Shares         :      300,
                                Field.Stock          :   "AAPL",
                                Field.CrossPrice     : 123.2501,
                                Field.MatchNum       :      400,
                                Field.CrossType      :      'O',
                             } ]

        # WHEN
        message = ItchMessageFactory.createFromArgs( messageArgs )

        # THEN
        self.assertEqual(        'Q', message.MessageType )
        self.assertEqual(        175, message.NanoSeconds )
        self.assertEqual(        300, message.Shares )
        self.assertEqual(     "AAPL", message.Stock )
        self.assertEqual(   123.2501, message.CrossPrice )
        self.assertEqual(        400, message.MatchNum )
        self.assertEqual(        'O', message.CrossType )

    def test_create_BrokenTrade(self):
        # GIVEN
        messageArgs = [ MessageType.BrokenTrade, {
                                Field.NanoSeconds    :      175,
                                Field.MatchNum       :      400,
                             } ]

        # WHEN
        message = ItchMessageFactory.createFromArgs( messageArgs )

        # THEN
        self.assertEqual(        'B', message.MessageType )
        self.assertEqual(        175, message.NanoSeconds )
        self.assertEqual(        400, message.MatchNum )

    def test_create_NetOrderImbalance(self):
        # GIVEN
        messageArgs = [ MessageType.NetOrderImbalance, {
                                Field.NanoSeconds              :       175,
                                Field.PairedShares             :      1000,
                                Field.ImbalanceShares          :      2000,
                                Field.ImbalanceDirection       :       'B',
                                Field.Stock                    :    "AAPL",
                                Field.FarPrice                 :  100.1234,
                                Field.NearPrice                :  101.9004,
                                Field.CurrentReferencePrice    :  102.8004,
                                Field.CrossType                :       'O',
                                Field.PriceVariationIndicator  :       'L',
                             } ]

        # WHEN
        message = ItchMessageFactory.createFromArgs( messageArgs )

        # THEN
        self.assertEqual(        'I', message.MessageType )
        self.assertEqual(        175, message.NanoSeconds )
        self.assertEqual(       1000, message.PairedShares )
        self.assertEqual(       2000, message.ImbalanceShares )
        self.assertEqual(        'B', message.ImbalanceDirection )
        self.assertEqual(     "AAPL", message.Stock )
        self.assertEqual(   100.1234, message.FarPrice )
        self.assertEqual(   101.9004, message.NearPrice )
        self.assertEqual(   102.8004, message.CurrentReferencePrice )
        self.assertEqual(        'O', message.CrossType )
        self.assertEqual(        'L', message.PriceVariationIndicator )

    def test_create_RetailInterestMessage(self):
        # GIVEN
        messageArgs = [ MessageType.RetailInterestMessage, {
                                Field.NanoSeconds   :       175,
                                Field.Stock         :    "AAPL",
                                Field.InterestFlag  :       'B',
                             } ]

        # WHEN
        message = ItchMessageFactory.createFromArgs( messageArgs )

        # THEN
        self.assertEqual(        'N', message.MessageType )
        self.assertEqual(        175, message.NanoSeconds )
        self.assertEqual(     "AAPL", message.Stock )
        self.assertEqual(        'B', message.InterestFlag )

class Create_Itch41_Messages_From_RawBytes(unittest.TestCase):
    """ Tests for creating, parsing and dumping Itch 41 messages from raw bytes 
        as encountered in a feed
    """

    def test_create_TimeStamp(self):
        # GIVEN
        rawMessage = bytearray()
        rawMessage.extend( [ 0x00, 0x05, 0x54, 0x00, 0x00, 0x58, 0xb7 ] )

        # WHEN
        message = ItchMessageFactory.createFromBytes( rawMessage )

        # THEN
        self.assertEqual(    'T', message.MessageType )
        self.assertEqual( 0x58b7, message.Seconds )

    def test_create_SystemEvent(self):
        # GIVEN
        rawMessage = bytearray()
        rawMessage.extend( [ 0x00, 0x06, 0x53, 0x11, 0xcd, 0x6c, 0xc9, 0x4f ])

        # WHEN
        message = ItchMessageFactory.createFromBytes( rawMessage )

        # THEN
        self.assertEqual(        'S', message.MessageType )
        self.assertEqual( 0x11cd6cc9, message.NanoSeconds )
        self.assertEqual(        'O', message.EventCode )

    def test_create_StockDirectory(self):
        # GIVEN
        rawMessage = bytearray()
        rawMessage.extend( [ 0x00, 0x14, 0x52, 0x1d, 0x48, 0xbd, 0xc7, 0x41 ] )
        rawMessage.extend( [ 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x4e ] )
        rawMessage.extend( [ 0x20, 0x00, 0x00, 0x00, 0x64, 0x4e ] )

        # WHEN
        message = ItchMessageFactory.createFromBytes( rawMessage )

        # THEN
        self.assertEqual(        'R', message.MessageType            )
        self.assertEqual(  491306439, message.NanoSeconds            )
        self.assertEqual(        "A", message.Stock                  )
        self.assertEqual(        'N', message.MarketCategory         )
        self.assertEqual(        ' ', message.FinancialStatus        )
        self.assertEqual(        100, message.RoundLotSize           )
        self.assertEqual(        'N', message.RoundLotsOnly          )

    def test_create_StockTradingAction(self):
        # GIVEN
        rawMessage = bytearray()
        rawMessage.extend( [ 0x00, 0x13, 0x48, 0x1d, 0x4b, 0xf3, 0x19, 0x41 ] )
        rawMessage.extend( [ 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x54 ] )
        rawMessage.extend( [ 0x20, 0x20, 0x20, 0x20, 0x20 ] )

        # WHEN
        message = ItchMessageFactory.createFromBytes( rawMessage )

        # THEN
        self.assertEqual(        'H', message.MessageType            )
        self.assertEqual(  491516697, message.NanoSeconds            )
        self.assertEqual(        "A", message.Stock                  )
        self.assertEqual(        'T', message.TradingState           )
        self.assertEqual(        ' ', message.Reserved               )
        self.assertEqual(     "    ", message.Reason                 )

    def test_create_RegSHORestriction(self):
        # GIVEN
        rawMessage = bytearray()
        rawMessage.extend( [ 0x00, 0x0e, 0x59, 0x1d, 0x4d, 0xa0, 0x8e, 0x41 ] )
        rawMessage.extend( [ 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x30 ] )

        # WHEN
        message = ItchMessageFactory.createFromBytes( rawMessage )

        # THEN
        self.assertEqual(        'Y', message.MessageType            )
        self.assertEqual(  491626638, message.NanoSeconds            )
        self.assertEqual(        "A", message.Stock                  )
        self.assertEqual(        '0', message.RegSHOAction           )

    def test_create_MarketParticipantPosition(self):
        # GIVEN
        rawMessage = bytearray()
        rawMessage.extend( [ 0x00, 0x14, 0x4c, 0x24, 0x30, 0x64, 0xc5, 0x41 ] )
        rawMessage.extend( [ 0x54, 0x44, 0x46, 0x41, 0x41, 0x50, 0x4c, 0x20 ] )
        rawMessage.extend( [ 0x20, 0x20, 0x20, 0x59, 0x4e, 0x41 ] )

        # WHEN
        message = ItchMessageFactory.createFromBytes( rawMessage )

        # THEN
        self.assertEqual(        'L', message.MessageType            )
        self.assertEqual(  607151301, message.NanoSeconds            )
        self.assertEqual(     "ATDF", message.Mpid                   )
        self.assertEqual(     "AAPL", message.Stock                  )
        self.assertEqual(        'Y', message.PrimaryMarketMaker     )
        self.assertEqual(        'N', message.MarketMakerMode        )
        self.assertEqual(        'A', message.MarketParticipantState )

    def test_create_AddOrderWithMPID(self):
        # GIVEN
        rawMessage = bytearray()
        rawMessage.extend( [ 0x00, 0x22, 0x46, 0x02, 0x43, 0xd1, 0x46, 0x00 ] )
        rawMessage.extend( [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x16, 0xb2, 0x42 ] )
        rawMessage.extend( [ 0x00, 0x00, 0x00, 0x64, 0x5a, 0x56, 0x5a, 0x5a ] )
        rawMessage.extend( [ 0x54, 0x20, 0x20, 0x20, 0x00, 0x02, 0x97, 0xac ] )
        rawMessage.extend( [ 0x4c, 0x45, 0x48, 0x4d ] )

        # WHEN
        message = ItchMessageFactory.createFromBytes( rawMessage )

        # THEN
        self.assertEqual(        'F', message.MessageType            )
        self.assertEqual(   37998918, message.NanoSeconds            )
        self.assertEqual(       5810, message.OrderRefNum            )
        self.assertEqual(        'B', message.Side                   )
        self.assertEqual(        100, message.Shares                 )
        self.assertEqual(    "ZVZZT", message.Stock                  )
        self.assertEqual(      16.99, message.Price                  )
        self.assertEqual(     "LEHM", message.Mpid                   )

    def test_create_AddOrder(self):
        # GIVEN
        rawMessage = bytearray()
        rawMessage.extend( [ 0x00, 0x1e, 0x41, 0x0d, 0xbb, 0xd4, 0x0f, 0x00 ] )
        rawMessage.extend( [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x16, 0xe7, 0x42 ] )
        rawMessage.extend( [ 0x00, 0x0f, 0x42, 0x3f, 0x4c, 0x47, 0x4c, 0x2b ] )
        rawMessage.extend( [ 0x20, 0x20, 0x20, 0x20, 0x00, 0x00, 0x00, 0x01 ] )

        # WHEN
        message = ItchMessageFactory.createFromBytes( rawMessage )

        # THEN
        self.assertEqual(        'A', message.MessageType            )
        self.assertEqual(  230413327, message.NanoSeconds            )
        self.assertEqual(       5863, message.OrderRefNum            )
        self.assertEqual(        'B', message.Side                   )
        self.assertEqual(     999999, message.Shares                 )
        self.assertEqual(     "LGL+", message.Stock                  )
        self.assertEqual(     0.0001, message.Price                  )

    def test_create_OrderDelete(self):
        # GIVEN
        rawMessage = bytearray()
        rawMessage.extend( [ 0x00, 0x0d, 0x44, 0x21, 0x95, 0x1b, 0xcf, 0x00 ] )
        rawMessage.extend( [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x31, 0x6b ] )

        # WHEN
        message = ItchMessageFactory.createFromBytes( rawMessage )

        # THEN
        self.assertEqual(        'D', message.MessageType            )
        self.assertEqual(  563420111, message.NanoSeconds            )
        self.assertEqual(      12651, message.OrderRefNum            )

    def test_create_OrderExecuted(self):
        # GIVEN
        rawMessage = bytearray()
        rawMessage.extend( [ 0x00, 0x19, 0x45, 0x18, 0x45, 0xcd, 0x07, 0x00 ] )
        rawMessage.extend( [ 0x00, 0x00, 0x00, 0x00, 0x00, 0xe9, 0xca, 0x00 ] )
        rawMessage.extend( [ 0x00, 0x03, 0xe8, 0x00, 0x00, 0x00, 0x00, 0x00 ] )
        rawMessage.extend( [ 0x00, 0x00, 0x01 ] )

        # WHEN
        message = ItchMessageFactory.createFromBytes( rawMessage )

        # THEN
        self.assertEqual(        'E', message.MessageType            )
        self.assertEqual(  407227655, message.NanoSeconds            )
        self.assertEqual(      59850, message.OrderRefNum            )
        self.assertEqual(       1000, message.Shares                 )
        self.assertEqual(          1, message.MatchNum               )

    def test_create_NetOrderImbalance(self):
        # GIVEN
        rawMessage = bytearray()
        rawMessage.extend( [ 0x00, 0x2c, 0x49, 0x00, 0x2f, 0x44, 0x84, 0x00 ] )
        rawMessage.extend( [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ] )
        rawMessage.extend( [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x4f ] )
        rawMessage.extend( [ 0x49, 0x50, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20 ] )
        rawMessage.extend( [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ] )
        rawMessage.extend( [ 0x00, 0x00, 0x00, 0x00, 0x4f, 0x20 ] )

        # WHEN
        message = ItchMessageFactory.createFromBytes( rawMessage )

        # THEN
        self.assertEqual(        'I', message.MessageType            )
        self.assertEqual(    3097732, message.NanoSeconds            )
        self.assertEqual(          0, message.PairedShares           )
        self.assertEqual(          0, message.ImbalanceShares        )
        self.assertEqual(        'O', message.ImbalanceDirection     )
        self.assertEqual(       "IP", message.Stock                  )
        self.assertEqual(          0, message.FarPrice               )
        self.assertEqual(          0, message.NearPrice              )
        self.assertEqual(          0, message.CurrentReferencePrice  )
        self.assertEqual(        'O', message.CrossType              )
        self.assertEqual(        ' ', message.PriceVariationIndicator )

    def test_create_CrossTrade(self):
        # GIVEN
        rawMessage = bytearray()
        rawMessage.extend( [ 0x00, 0x22, 0x51, 0x00, 0x02, 0x76, 0xa2, 0x00 ] )
        rawMessage.extend( [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x41 ] )
        rawMessage.extend( [ 0x42, 0x43, 0x44, 0x20, 0x20, 0x20, 0x20, 0x00 ] )
        rawMessage.extend( [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ] )
        rawMessage.extend( [ 0x00, 0x00, 0x05, 0x4f ] )

        # WHEN
        message = ItchMessageFactory.createFromBytes( rawMessage )

        # THEN
        self.assertEqual(        'Q', message.MessageType            )
        self.assertEqual(     161442, message.NanoSeconds            )
        self.assertEqual(          0, message.Shares                 )
        self.assertEqual(     "ABCD", message.Stock                  )
        self.assertEqual(          0, message.CrossPrice             )
        self.assertEqual(          5, message.MatchNum               )
        self.assertEqual(        'O', message.CrossType              )

    def test_create_OrderExecutedWithPrice(self):
        # GIVEN
        rawMessage = bytearray()
        rawMessage.extend( [ 0x00, 0x1e, 0x43, 0x01, 0x74, 0xa8, 0xca, 0x00 ] )
        rawMessage.extend( [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x31, 0x9b, 0x00 ] )
        rawMessage.extend( [ 0x00, 0x00, 0x64, 0x00, 0x00, 0x00, 0x00, 0x00 ] )
        rawMessage.extend( [ 0x00, 0x03, 0xb0, 0x4e, 0x00, 0x02, 0x9c, 0x5c ] )

        # WHEN
        message = ItchMessageFactory.createFromBytes( rawMessage )

        # THEN
        self.assertEqual(        'C', message.MessageType            )
        self.assertEqual(   24422602, message.NanoSeconds            )
        self.assertEqual(      12699, message.OrderRefNum            )
        self.assertEqual(        100, message.Shares                 )
        self.assertEqual(        944, message.MatchNum               )
        self.assertEqual(        'N', message.Printable              )
        self.assertEqual(      17.11, message.Price                  )

    def test_create_TradeNonCross(self):
        # GIVEN
        rawMessage = bytearray()
        rawMessage.extend( [ 0x00, 0x26, 0x50, 0x03, 0x10, 0x74, 0xb6, 0x00 ] )
        rawMessage.extend( [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x42 ] )
        rawMessage.extend( [ 0x00, 0x00, 0x00, 0x64, 0x4f, 0x43, 0x5a, 0x20 ] )
        rawMessage.extend( [ 0x20, 0x20, 0x20, 0x20, 0x00, 0x03, 0xbb, 0x78 ] )
        rawMessage.extend( [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x92 ] )

        # WHEN
        message = ItchMessageFactory.createFromBytes( rawMessage )

        # THEN
        self.assertEqual(        'P', message.MessageType            )
        self.assertEqual(   51410102, message.NanoSeconds            )
        self.assertEqual(          0, message.OrderRefNum            )
        self.assertEqual(        'B', message.Side                   )
        self.assertEqual(        100, message.Shares                 )
        self.assertEqual(      "OCZ", message.Stock                  )
        self.assertEqual(      24.46, message.Price                  )
        self.assertEqual(       1938, message.MatchNum               )





if __name__ == "__main__":
    unittest.main()

