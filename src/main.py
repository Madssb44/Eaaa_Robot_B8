## main file for controlling the car
import web
import gc 


def init():
    while True:
        try:
            import webrepl_setup
        
        finally:
            web.stop_server
            web.disconnect_wifi
            print('test done')






init()
