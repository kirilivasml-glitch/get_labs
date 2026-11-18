import time
import smbus


class MCP3021:
    def __init__(self, dynamic_range, verbose=False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose

    def deinit(self):
        self.bus.close()

    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)

        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF

        number = (upper_data_byte << 6) | (lower_data_byte >> 2)

        if self.verbose:
            print(
                f"Принятые данные: {data}, "
                f"Старший байт: {upper_data_byte:02x}, "
                f"Младший байт: {lower_data_byte:02x}, "
                f"Число: {number}"
            )

        return number

    def get_voltage(self):
        number = self.get_number()
        voltage = number * self.dynamic_range / 1023

        if self.verbose:
            print(f"Напряжение: {voltage:.4f} В")

        return voltage


if __name__ == "__main__":
    adc = None

    try:
        adc = MCP3021(dynamic_range=5.0, verbose=True)

        while True:
            voltage = adc.get_voltage()
            print(f"Измеренное напряжение: {voltage:.4f} В")
            time.sleep(1)

    finally:
        if adc is not None:
            adc.deinit()