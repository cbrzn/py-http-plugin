from dataclasses import dataclass
from typing import Optional, Dict, Union, Any

from requests import request
from polywrap_plugin import PluginModule
from polywrap_core import Invoker


TEXT = "TEXT"
BINARY = "BINARY"
JSON = "JSON"

HttpResponseType = Union[TEXT, BINARY, JSON]

@dataclass(slots=True, kw_only=True)
class HttpRequest:
    headers: Optional[Dict[str, str]]
    url_params: Optional[Dict[str, str]]
    response_type: HttpResponseType
    body: Optional[str]

@dataclass(slots=True, kw_only=True)
class HttpResponse:
    status: int
    status_text: str
    headers: Optional[Dict[str, str]]
    body: Optional[str]

@dataclass(slots=True, kw_only=True)
class ArgsGet:
    url: str
    request: Optional[HttpRequest]

class HttpPlugin(PluginModule[None, str]):
    def get(self, args: ArgsGet, invoker: Invoker):
        config = {}
        if 'request' in args:
            config = self.parse_config(args['request'])
        
        req = request("get", args['url'])
        print(req)
        return HttpResponse(
            status=200,
            status_text="OK",
            headers=None,
            body=None
        )

    def post(self):
        pass

    def parse_config(self, config: HttpRequest):
        pass
