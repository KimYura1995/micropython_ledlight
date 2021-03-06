import uasyncio as asyncio
import machine
import neopixel
import settings


neo_pixel = neopixel.NeoPixel(machine.Pin(4), settings.SETTINGS['num_leds'])


class StaticMode:

    def __init__(self):
        self.set_settings()
        self.mode = 'static_mode'

    async def run(self):
        try:
            red = self.set_color(self.red_color)
            green = self.set_color(self.green_color)
            blue = self.set_color(self.blue_color)

            for led in range(self.num_leds):
                neo_pixel[led] = (red, green, blue)

            neo_pixel.write()
            self.change_settings()
            await asyncio.sleep_ms(10)
        except Exception:
            return

    def change_settings(self):
        self.set_settings()
        if settings.SETTINGS['current_mode'] is not self.mode:
            raise ValueError('Change Mode')

    def set_settings(self):
        self.num_leds = settings.SETTINGS['num_leds']
        self.led_status = settings.SETTINGS['led_status']
        self.led_brightness = settings.SETTINGS['led_brightness']
        self.red_color = settings.SETTINGS['mode']['static_mode']['red_color']
        self.green_color = settings.SETTINGS['mode']['static_mode']['green_color']
        self.blue_color = settings.SETTINGS['mode']['static_mode']['blue_color']

    def set_color(self, color):
        return int(color * self.led_brightness * self.led_status / 100)
