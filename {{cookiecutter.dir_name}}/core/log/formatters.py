import json
import sys
from typing import Any

loglevel_mapping = {
    "ERROR": 50,
    "WARNING": 40,
    "INFO": 30,
    "DEBUG": 20,
    "TRACE": 10,
    "NOTSET": 0,
}

log_format = {
    "service_log": "{level} | {time:YYYY-MM-DD HH:mm:ss} | {extra[name]}"
    " | {extra[point]} | {message}"
}


def standard_web_sink_serializer(message: Any) -> None:
    record = message.record

    simplified = {
        "level": loglevel_mapping[record["level"].name],
        "timestamp": record["time"].timestamp(),
        "name": record["extra"]["name"],
        "point": record["extra"]["point"],
        "message": record["message"],
    }
    serialized = json.dumps(simplified, ensure_ascii=False)
    print(serialized, file=sys.stderr)  # noqa: T201
