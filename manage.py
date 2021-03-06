# -*- coding: utf-8 -*-

import asyncio
from signal import signal, SIGINT

import uvloop

from wechat.app import create_app

import os,sys
parent = os.path.dirname(os.path.realpath(__file__))
sys.path.append('root/MITIE/mitielib')

app = create_app()


def run():
    asyncio.set_event_loop(uvloop.new_event_loop())
    server = app.create_server(host="0.0.0.0", port=80)
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(server)
    signal(SIGINT, lambda s, f: loop.stop())
    try:
        loop.run_forever()
    except:
        loop.stop()


if __name__ == '__main__':
    run()