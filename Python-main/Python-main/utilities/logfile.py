import logging

class LogGen:
    @staticmethod
    def loggen():
     logging.basicConfig(filename=".\\Lamdatest\\logs\\result.log,",
                                 format='%(asctime)s: %(levelname)s: %(message)s:',
                            datefmt='%m/%d/%y %I:%M:%S %p')
     log=logging.getLogger()
     log.setLevel(logging.INFO)
     return log