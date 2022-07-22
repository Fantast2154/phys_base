class Application:
    def __init__(self):
        self.send_massage('App is running')
    
    def send_massage(self, msg):
        input_message = str(msg)
        class_info = str(Application.__name__)
        print(f'{class_info}: {input_message}')
        