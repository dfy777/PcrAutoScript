#-*- coding: UTF-8-*-
class UnfindSimulatorException(Exception):
    def __init__(self, ErrorInfo):
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo

class UnfindAdbException(Exception):
    def __init__(self, ErrorInfo):
        self.errorinfo = ErrorInfo
    
    def __str__(self):
        return self.errorinfo

class ConnectException(Exception):
    def __init__(self, ErrorInfo):
        self.errorinfo = ErrorInfo
    
    def __str__(self):
        return self.errorinfo