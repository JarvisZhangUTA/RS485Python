class Config:
    EN_485 = 4
    BAUD_RATE = 19200

    SERIAL_CYC = 1
    SERIAL_WAIT = 1

    DOWN_QUEUE_NAME = 'command_queue'
    UP_QUEUE_NAME = 'result_queue'

    SOCKET_HOST = 'ws://206.189.166.192:8080'