from connections import TCPConnection
from connections.serial import SerialConnection
from protocol import ProtocolDecoder  

with SerialConnection('COM5') as conn:
    decoder = ProtocolDecoder(conn)
    while True:
        print(decoder.get_S1S())
        print(decoder.get_GDA())
        print(decoder.set_reference_position(450, -80))
        print(decoder.enable_stabilization())
        print("\r")

    #for decoded in decoder.get_SLS(5,1):
    #    print(decoded)
    #decoder.get_SLS(5,1)
    # decoder.debug_message_stream()