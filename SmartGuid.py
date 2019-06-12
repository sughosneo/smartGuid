from threading import Lock
import time
import datetime
from datetime import datetime

class SmartGuid:

    __lock = None
    __instance = None

    @classmethod
    def instance(cls):

        if cls.__instance == None:
            cls.__instance = SmartGuid()
        return cls.__instance

    def __init__(self):

        self.__lock = Lock()

        if self.__instance !=None:
            raise ValueError("Already an object exist!")

    def getGuid(self,prefix:str,suffix:str) -> str:

        self.__lock.acquire()

        try:

            if prefix and suffix is None:
                return "{}-{}".format(prefix,str(self.__getTimeStampValue()))
            elif suffix and prefix is None:
                return "{}-{}".format(str(self.__getTimeStampValue()),suffix)
            elif prefix and suffix:
                return "{}-{}-{}".format(prefix,str(self.__getTimeStampValue()), suffix)
            else:
                return str(self.__getTimeStampValue())

        except Exception as error:
            raise Exception("Not able to generate guid !")
        finally:
            self.__lock.release()

    def __getTimeStampValue(self):

        # dateTimeNow = datetime.now()
        # return datetime.timestamp(dateTimeNow)

        return time.time_ns()

