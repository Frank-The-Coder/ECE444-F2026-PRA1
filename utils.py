class utils:
    """Small number utilities for ECE444 PRA1 Activity 4."""

    @staticmethod
    def reversed(number):
        """Return the digits of an int reversed, as an int.

        123 -> 321, 120 -> 21 (leading zero dropped), -123 -> -321.
        Raises TypeError for anything that is not an int (bool is rejected
        too, because in Python bool is a subclass of int).
        """
        if isinstance(number, bool) or not isinstance(number, int):
            raise TypeError(f"reversed expects an int, got {type(number).__name__}")
        sign = -1 if number < 0 else 1
        return sign * int(str(abs(number))[::-1])

    @staticmethod
    def formatter(number):
        """Return an int in base 2 and base 8 as a (binary, octal) tuple of strings.

        10 -> ("0b1010", "0o12").
        Raises TypeError for anything that is not an int.
        """
        if isinstance(number, bool) or not isinstance(number, int):
            raise TypeError(f"formatter expects an int, got {type(number).__name__}")
        return bin(number), oct(number)
