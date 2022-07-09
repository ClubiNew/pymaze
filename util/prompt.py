from argparse import ArgumentError
from typing import Optional

def get_int(
    prompt: str,
    min: Optional[int] = None,
    max: Optional[int] = None,
    odd: bool = False,
    even: bool = False,
) -> int:
    if odd and even:
        raise Exception("A number cannot be both even and odd. To allow either, set both arguments to false.")

    while True:
        try:
            n = int(input(f"{prompt}: "))

            if min != None and n < min:
                print(f"Please input a value ≥{min}.")
                continue
            elif max != None and n > max:
                print(f"Please input a value ≤{max}.")
                continue
            elif odd and n % 2 == 0:
                print("Please enter an odd number.")
                continue
            elif even and n % 2 == 1:
                print("Please enter an even number.")
                continue

            return n
        except:
            print("Please enter a whole number.")

def get_decision(prompt: str) -> bool:
    decision = input(f"{prompt} (y/n): ").lower()

    while decision not in ['y', 'n']:
        print("Please choose 'y' or 'n'.")
        decision = input(f"{prompt} (y/n): ").lower()

    return decision == 'y'

def get_selection(options: list[str], prompt: str) -> int:
    for idx, choice in enumerate(options):
        print(f"{idx + 1}. {choice}")

    print()
    return get_int(prompt, 1, len(options)) - 1
