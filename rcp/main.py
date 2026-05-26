import asyncio
from keke import ktrace
from kivy.core.window import Window
from kivy.base import EventLoop
from kivy.logger import Logger
from kivy.factory import Factory
log = Logger.getChild(__name__)

Factory.register('ScreenHeader', module='rcp.components.widgets.screen_header')

Window.show_cursor = False

if __name__ == "__main__":
    from rcp.app import MainApp
    # Monkeypatch to add more trace events
    EventLoop.idle = ktrace()(EventLoop.idle)
    try:
        asyncio.run(MainApp().async_run())
    except KeyboardInterrupt:
        log.info("Exiting Application")
