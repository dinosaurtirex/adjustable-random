import random
from .exceptions import (
    AdjustException
)

import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def get_adjustable_random_list(
    *,
    min_value: int,
    max_value: int,
    numbers_to_adjust: list[int],
    k: int = 5
) -> int:
    """ Generating adjustable random values,
        from min to max with numbers to adjust.

        For example, we have values from 1 to 10.

        If number 2 and 3 will be in numbers to adjust with k=5,
        final array will look like this:

        [1,2,2,2,2,2,3,3,3,3,3,4,5,6,7,8,9,10]
        
        and chance of random.choice for those values
        will be increased 
    """
    max_adjustment_value: int = max(numbers_to_adjust)
    if max_adjustment_value > max_value:
        raise AdjustException(
            f"{max_adjustment_value=} > {max_value=}, {max_value=} should be < {max_adjustment_value=}"
        )

    numbers: list[int] = []
    for i in range(min_value, max_value):
        if i in numbers_to_adjust:
            for _ in range(k):
                numbers.append(i)
            continue 
        numbers.append(i)
    return numbers 


def get_adjustable_random_value(
    min_value: int,
    max_value: int,
    numbers_to_adjust: list[int],
    k: int = 5
):
    return random.choice(
        get_adjustable_random_list(
            min_value=min_value,
            max_value=max_value,
            numbers_to_adjust=numbers_to_adjust,
            k=k
        )
    )


def main() -> int:
    result: int = get_adjustable_random_list(
        min_value=0,
        max_value=15,
        numbers_to_adjust=[
            5,10,15
        ]
    )
    choice_result = random.choice(result)
    logger.debug(f"get_adjustable_random_list array: {result}")
    logger.debug(f"random choice result: {choice_result}")
    return 1


if __name__ == '__main__':
    from .tests import (
        init_random_values,
        run_graph_test
    )
    values: list[int] = init_random_values()
    run_graph_test(values)
