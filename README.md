# More adjustable random functions

Generating adjustable random values,
from min to max with numbers to adjust.

For example, we have values from 1 to 10.

If number 2 and 3 will be in numbers to adjust with k=5,
final array will look like this:

```
[1,2,2,2,2,2,3,3,3,3,3,4,5,6,7,8,9,10]
```

and chance of random.choice for those values
will be increased 

# Examples

### Run basic functions 

```
from adjustable_random import (
    get_adjustable_random_list,
    get_adjustable_random_value
)

if __name__ == '__main__':

    adjustable_list: list[int] = get_adjustable_random_list(
        min_value=0,
        max_value=100,
        numbers_to_adjust=[
            10,15
        ]
    )
    adjustable_value: int = get_adjustable_random_value(
        min_value=0,
        max_value=100,
        numbers_to_adjust=[
            10,15
        ]
    )

    print(f"{adjustable_list=}")
    print(f"{adjustable_value=}")

```


### Run tests to see how it works


```
from adjustable_random import (
    init_random_values,
    run_graph_test
)

if __name__ == '__main__':
    values: list[int] = init_random_values()
    run_graph_test(values)

```