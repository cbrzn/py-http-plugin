import pytest

from polywrap_client import PolywrapClient, PolywrapClientConfig
from polywrap_uri_resolvers import StaticResolver
from polywrap_core import Uri, InvokerOptions, UriWrapper
from polywrap_plugin import PluginWrapper

from http_plugin import HttpPlugin, HttpResponse

@pytest.mark.asyncio
async def test_http_plugin():
    uri = Uri("ens/http-plugin.polywrap.eth")

    plugin = HttpPlugin(None)
    wrapper = PluginWrapper(plugin, {})

    uri_wrapper = UriWrapper(uri=uri, wrapper=wrapper)

    resolver = StaticResolver.from_list([ uri_wrapper ]).unwrap()

    config = PolywrapClientConfig(resolver=resolver)
    client = PolywrapClient(config=config)

    args = {
        "url": "https://reqbin.com/echo"
    }

    options = InvokerOptions(
        uri=uri, 
        method="get", 
        args=args, 
        encode_result=False
    )
    result = (await client.invoke(options)).unwrap()
    print(result)