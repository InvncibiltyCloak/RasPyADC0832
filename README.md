# RasPyADC0832
An extremely simple library to interact with an ADC0832 IC from a Raspberry Pi. It is able to work with both available channels. Does not support differential mode.

## Dependencies
This library depends on the RPi.GPIO library. This comes installed by default on Raspbian. Otherwise you can use `pip install RPi.GPIO` to install it.

## Quick Start
First, import the ADC0832 class from this library.
```
from ADC0832 import ADC0832
```

Next, create an AD0832 instance.
```
adc = ADC0832()
```

Call `read_channel` as needed.
```
value1 = adc.read_channel(0)
value2 = adc.read_channel(1)
```

When finished, clean up.
```
adc.cleanup()
```

## Pin Configuration
There arent many options in this library, because it is such a simple device. By default the CLK pin is on P1 header pin #16, both DATA_IN and DATA_OUT are connected to pin #22, and CSEL is connected to pin #18. These can be changed with keyword arguments to the ADC0832 constructor:
```
adc = ADC0832(clk_pin = 16, data_pin = 22, csel_pin = 18)
```
