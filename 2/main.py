from secant import Secant
from cosecant import Cosecant
from cotangent import Cotangent
import math


def main():
    sec = Secant(math.pi / 4)
    print(f"Secant Value: {sec.value()}")
    print(f"Secant Derivative: {sec.derivative().value()}")
    print(sec)
    print()

    cosec = Cosecant(math.pi / 4)
    print(f"Cosecant Value: {cosec.value()}")
    print(f"Cosecant Derivative: {cosec.derivative().value()}")
    print(cosec)
    print()

    cot = Cotangent(math.pi / 4)
    print(f"Cotangent Value: {cot.value()}")
    print(f"Cotangent Derivative: {cot.derivative().value()}")
    print(cot)


if __name__ == "__main__":
    main()
