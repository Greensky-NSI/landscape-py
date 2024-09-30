from utils.types import color_type


def assert_color(col: color_type, *, allow_floats: bool = False):
    return isinstance(col, tuple) and (len(col) == 3 or len(col) == 4) and all((isinstance(i, int) or (isinstance(i, float) and allow_floats)) for i in col)

def assert_color_mode(mode: str):
    return mode in ["maximum", "modulo"]

def assert_size_factor(test_size):
    return (isinstance(test_size, float) or isinstance(test_size, int)) and test_size > 0