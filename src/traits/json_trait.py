from dataclasses import dataclass, asdict
import json


@dataclass(frozen=True)
class JsonTrait:
    def to_json(self, *, indent=2) -> str:
        return json.dumps(asdict(self), indent=indent)
