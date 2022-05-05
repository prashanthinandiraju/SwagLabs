import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(level=logging.DEBUG,
                            filename="C:\\Users\\User\\Documents\\pythonProject\\SwagLabs\\Logs\\SwagLabs.log",
                            filemode="a",
                            format='%(asctime)s - %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S:%p',
                            force="True")

        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger