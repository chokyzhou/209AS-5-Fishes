import re

class Convert:
    def __init__(self) -> None:
        pass

    def coo2str(x:int, y:int) -> str:
        return "(" + str(x) + "," + str(y) + ")"
    
    def str2coo(s:str) -> tuple:
        nums = re.findall(r"\d+", str)
        return (nums[0],nums[1])