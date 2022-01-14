import time
from smbus2 import SMBus

bus = SMBus(1)
bmp_addr = 0x76

# setup config register

bus.write_byte_data(bmp_addr, 0xf5, (5 << 5))
bus.write_byte_data(bmp_addr, 0xf4, ((5 << 5) | (3 << 0)))

# global values
data = 0
package = {'Data': [], 'Temperature': [], 'Pressure': []}

# calculation of preasure and temperature
dig_T1 = bus.read_word_data(bmp_addr, 0x88)
dig_T2 = bus.read_word_data(bmp_addr, 0x8A)
dig_T3 = bus.read_word_data(bmp_addr, 0x8C)

if dig_T2 > 32767:
    dig_T2 -= 65536
if dig_T3 > 32767:
    dig_T3 -= 65536

dig_P1 = bus.read_word_data(bmp_addr, 0x8E)
dig_P2 = bus.read_word_data(bmp_addr, 0x90)
dig_P3 = bus.read_word_data(bmp_addr, 0x92)
dig_P4 = bus.read_word_data(bmp_addr, 0x94)
dig_P5 = bus.read_word_data(bmp_addr, 0x96)
dig_P6 = bus.read_word_data(bmp_addr, 0x98)
dig_P7 = bus.read_word_data(bmp_addr, 0x9A)
dig_P8 = bus.read_word_data(bmp_addr, 0x9C)
dig_P9 = bus.read_word_data(bmp_addr, 0x9E)

if (dig_P2 > 32767):
    dig_P2 -= 65536
if (dig_P3 > 32767):
    dig_P3 -= 65536
if (dig_P4 > 32767):
    dig_P4 -= 65536
if (dig_P5 > 32767):
    dig_P5 -= 65536
if (dig_P6 > 32767):
    dig_P6 -= 65536
if (dig_P7 > 32767):
    dig_P7 -= 65536
if (dig_P8 > 32767):
    dig_P8 -= 65536
if (dig_P9 > 32767):
    dig_P9 -= 65536


def temperature():
    d1 = bus.read_byte_data(bmp_addr, 0xfa)
    d2 = bus.read_byte_data(bmp_addr, 0xfb)
    d3 = bus.read_byte_data(bmp_addr, 0xfc)

    adc_T = ((d1 << 16) | (d2 << 8) | d3) >> 4

    var1 = (((adc_T >> 3) - (dig_T1 << 1)) * dig_T2) >> 11
    var2 = (((((adc_T >> 4) - dig_T1) * ((adc_T >> 4) - dig_T1)) >> 12) * dig_T3) >> 14
    t_fine = var1 + var2
    T = (t_fine * 5 + 128) >> 8
    T = T / 100

    print("Temperature: " + str(T))
    temp_data = [t_fine, T]

    return temp_data


def pressure(t_fine):
    p1 = bus.read_byte_data(bmp_addr, 0xf7)
    p2 = bus.read_byte_data(bmp_addr, 0xf8)
    p3 = bus.read_byte_data(bmp_addr, 0xf9)

    adc_P = ((p1 << 16) | (p2 << 8) | p3) >> 4

    var1 = (t_fine / 2.0) - 64000.0
    var2 = (var1 * var1 * dig_P6 / 32768.0)
    var2 = var2 + var1 * dig_P5 * 2.0
    var2 = (var2 / 4.0) + dig_P4 * 65536.0
    var1 = dig_P3 * var1 * var1 / 524288.0 + dig_P2 * var1 / 524288.0
    var1 = (1.0 + var1 / 32768.0) * dig_P1
    if var1 == 0:
        return 0
    p = 1048576.0 - adc_P
    print(adc_P)
    p = (p - (var2 / 4096.0)) * 6250.0 / var1
    print(p)
    var1 = dig_P9 * p * p / 2147483648.0
    var2 = p * dig_P8 / 32768.0
    p = p + (var1 + var2 + dig_P7) / 16
    print(t_fine)
    print("Pressure: " + str(p))

    return p


def package(T, P, data):
    package['Data'].append(data)
    package['Temperature'].append(T)
    package['Pressure'].append(P)
    print(package)
    return package


while True:
    temp_data = temperature()
    P = pressure(temp_data[0])
    package(temp_data[1], P, data)
    data = data + 1
    time.sleep(1)
