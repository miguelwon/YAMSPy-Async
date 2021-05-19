import sys
import time
import serial

from yamspy import MSPy

serial_port = "/dev/ttyACM0"

with MSPy(device=serial_port, logfilename='MSPy.log', logfilemode='a', loglevel='DEBUG') as board:
    test_mocap = [0, 20, 30, 40, 0]
    data = board.convert(test_mocap, 16)

    try:
        while True:
            if board.send_RAW_msg(MSPy.MSPCodes['MSP_MOCAP'], data):
                dataHandler = board.receive_msg()
                codestr = MSPy.MSPCodes2Str.get(dataHandler['code'])
                if codestr:
                    print('Received >>> {}'.format(codestr))
                    board.process_recv_data(dataHandler)
                elif dataHandler['packet_error'] == 1:
                    print('Received >>> ERROR!')
            time.sleep(.1)
            print(f"Debug content: {board.SENSOR_DATA['debug']}") # debug should be set to MOCAP for this script to work...
            if board.send_RAW_msg(MSPy.MSPCodes['MSP_DEBUG'], data=[]):
                dataHandler = board.receive_msg()
                codestr = MSPy.MSPCodes2Str.get(dataHandler['code'])
                if codestr:
                    print('Received >>> {}'.format(codestr))
                    board.process_recv_data(dataHandler)
                    print(f"Debug content: {board.SENSOR_DATA['debug']}")
                elif dataHandler['packet_error'] == 1:
                    print('Received >>> ERROR!')
            test_mocap[0] = test_mocap[0]+1 # it will reject the message if this values is not incremented
            data = board.convert(test_mocap, 16)

    except KeyboardInterrupt:
        print("Keyboard Interrupt received!")
    finally:
        print("Board is rebooting...")
        if board.reboot():
            try:
                dataHandler = board.receive_msg()
                board.process_recv_data(dataHandler)
            except serial.SerialException:
                print("Serial error... it's rebooting :)")