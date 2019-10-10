import logging
import sys

logging.basicConfig(filename='logging.log',level=logging.DEBUG)

def before_all(context):
    context.logger = setup_custom_logger("Running Automated Acceptance Tests")
    context.logger.info("************************************************************************************************")
    context.logger.info("* Starting execution of Automation..".upper())
    context.logger.info("************************************************************************************************")
    context.logger.info("Before all execution configurations -- setting environment..")
    context.base_url = context.config.userdata.get('base_api_url')


def before_feature(context, feature):
    context.logger.info(f"Execution the before feature '{feature}' section")

def after_scenario(context, scenario):
    print("\n")
    context.logger.info("******************************************************************************")
    context.logger.info(f"* Test case '{scenario.name}' ---------------> '{scenario.status}'")
    context.logger.info("******************************************************************************\n\n\n\n")

def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler('logging.log', mode='w')
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger