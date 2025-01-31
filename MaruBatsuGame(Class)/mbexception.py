class MBException(Exception):
    def __init__(self, *args):
        self.val = args[0] if args is not None else ""

class OutOfBoundError(MBException):
    def __str__(self):
        return f"範囲外です : {self.val}"

class AlreadyExistError(MBException):
    def __str__(self):
        return f"既に埋まっています : {self.val}"
    
class FormatError(MBException):
    def __str__(self):
        return f" 数字１文字とアルファベット１文字にしてください : {self.val} "