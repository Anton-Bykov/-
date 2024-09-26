"""import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 21, 20, 16]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec2bin(x):
    return [int(bit) for bit in bin(x)[2:].zfill(8)]

try:
    period_str = input("Введите период треугольного сигнала: ")
    try:
        period = float(period_str)
    except ValueError:
        print("Ошибка: Введите числовое значение для периода.")
        exit()

    while True:  
        for value in range(256):
            binary = dec2bin(value)
            GPIO.output(dac, binary)
            time.sleep(period / 512)
            print(f"Значение: {value}, Напряжение: {value*3.3/255:.2f} В")

        for value in range(255, -1, -1):
            binary = dec2bin(value)
            GPIO.output(dac, binary)
            time.sleep(period / 512)
            print(f"Значение: {value}, Напряжение: {value*3.3/255:.2f} В")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()"""

"""import RPi.GPIO as GPIO
import time

pwm_pin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT)

pwm = GPIO.PWM(pwm_pin, 1000) 

pwm.start(0)

try:
    while True:
        duty_cycle_str = input("Введите коэффициент заполнения (0-100): ")
        try:
            duty_cycle = float(duty_cycle_str)
        except ValueError:
            print("Ошибка: Введите числовое значение.")
            continue

        if duty_cycle < 0 or duty_cycle > 100:
            print("Ошибка: Введите число в диапазоне от 0 до 100.")
            continue

        pwm.ChangeDutyCycle(duty_cycle)
        
        voltage = duty_cycle / 100 * 3.3  # Предполагая 3.3 В на Raspberry Pi
        print(f"Предполагаемое напряжение: {voltage:.2f} В")

finally:
    # Очистка настроек GPIO
    pwm.stop()
    GPIO.cleanup()"""

"""import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 21, 20, 16]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec2bin(x):
    return [int(bit) for bit in bin(x)[2:].zfill(8)]

try:
    period_str = input("Введите период треугольного сигнала: ")
    try:
        period = float(period_str)
    except ValueError:
        print("Ошибка: Введите числовое значение для периода.")
        exit()

    while True:  
        for value in range(256):
            binary = dec2bin(value)
            GPIO.output(dac, binary)
            time.sleep(period / 512)
            print(f"Значение: {value}, Напряжение: {value*3.3/255:.2f} В")

        for value in range(255, -1, -1):
            binary = dec2bin(value)
            GPIO.output(dac, binary)
            time.sleep(period / 512)
            print(f"Значение: {value}, Напряжение: {value*3.3/255:.2f} В")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()"""
