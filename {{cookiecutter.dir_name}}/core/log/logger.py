from loguru import logger

from core.settings import get_settings
from core.log.formatters import (
    log_format,
    loglevel_mapping,
    standard_web_sink_serializer,
)

logger.remove()
logger.add(
    sink=standard_web_sink_serializer,
    format=log_format["service_log"],
    level=loglevel_mapping[get_settings().LOG_LEVEL],
)


class Logger:
    name = "ANALYTICS_REPORTS"
    point: str

    def __init__(self, point: str) -> None:
        self.point = point

    def info(self, message: str) -> None:
        logger.bind(
            name=self.name, level=loglevel_mapping["INFO"], point=self.point
        ).info(message)

    def warning(self, message: str) -> None:
        logger.bind(
            name=self.name, level=loglevel_mapping["WARNING"], point=self.point
        ).warning(message)

    def error(self, message: str) -> None:
        logger.bind(
            name=self.name, level=loglevel_mapping["ERROR"], point=self.point
        ).error(message)
