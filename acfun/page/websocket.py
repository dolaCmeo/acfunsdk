# coding=utf-8
import time
import random
import websocket, ssl
import base64
from acfun.source import routes, apis, websocket_links, header
from acfun.protos import AcProtos

__author__ = 'dolacmeo'

# https://github.com/wpscott/AcFunDanmaku/blob/master/AcFunDanmu/README.md
# https://github.com/wpscott/AcFunDanmaku/blob/master/AcFunDanmu/data.md
# https://github.com/orzogc/acfundanmu/blob/master/proto.go
# https://developers.google.com/protocol-buffers/docs/pythontutorial
# https://websocket-client.readthedocs.io/en/latest/getting_started.html

# https://protogen.marcgravell.com/decode


class AcWsConfig:
    did = None
    userId = None
    ssecurity = None
    sessKey = None
    visitor_st = None
    api_st = None
    api_at = None
    appId = 0
    instanceId = 0

    def __init__(self, acer):
        self.acer = acer
        self._get_token()

    def _get_did(self):
        live_page_req = self.acer.client.get(routes['live_index'])
        assert live_page_req.status_code // 100 == 2
        self.did = live_page_req.cookies.get('_did')

    def _get_token(self):
        self._get_did()
        if self.acer.is_logined:
            api_req = self.acer.client.post(apis['token'], data={"sid": "acfun.midground.api"})
            api_data = api_req.json()
            assert api_data.get('result') == 0
            self.ssecurity = api_data.get("ssecurity", '')
            self.api_st = api_data.get("acfun.midground.api_st", '').encode()
            self.api_at = api_data.get("acfun.midground.api.at", '').encode()
        else:
            api_req = self.acer.client.post(apis['token_visitor'], data={"sid": "acfun.api.visitor"})
            api_data = api_req.json()
            assert api_data.get('result') == 0
            self.ssecurity = api_data.get("acSecurity", '')
            self.visitor_st = api_data.get("acfun.api.visitor_st", '').encode()
        self.userId = api_data.get("userId")


class AcWebSocket:
    ws_link = None
    config = None

    def __init__(self, acer):
        self.acer = acer
        websocket.enableTrace(True)
        self.ws_link = random.choice(websocket_links)
        self.config = AcWsConfig(self.acer)
        self.ws = websocket.WebSocketApp(
            url=self.ws_link,
            on_open=self.register,
            on_message=self.message,
            on_error=self.error,
            on_close=self.close,
            # on_ping=self.keep_alive_request,
            on_pong=self.keep_alive_response,
        )
        self.protos = AcProtos(self.config)
        self.ws.run_forever(
            # sslopt={"cert_reqs": ssl.CERT_NONE},
            ping_interval=30, ping_timeout=10,
            skip_utf8_validation=True,
            origin="live.acfun.cn",
        )
        pass

    def register(self, ws):
        basic_register = self.protos.Basic_Register_Request()
        print("send: ", base64.standard_b64encode(basic_register))
        self.ws.send(basic_register)
        self.protos.seqId += 1

    def message(self, ws, message):
        print("recv: ", base64.standard_b64encode(message))
        self.protos.decode(message)

    # def keep_alive_request(self, ws, message):
    #     pass

    def keep_alive_response(self, ws, message):
        # print("pone: ", base64.standard_b64encode(message))
        keep_alive = self.protos.Keep_Alive_Request()
        print("ping: ", base64.standard_b64encode(keep_alive))
        self.ws.send(keep_alive)
        # self.protos.decode(message)

    def close(self, ws):
        pass

    def error(self, ws):
        # print("error", e)
        pass