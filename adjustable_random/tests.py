import random as rand 
from collections import Counter 
import matplotlib.pyplot as plt 
from .main import get_adjustable_random_list


def init_random_values(
    k: int=1000
) -> list[int]: 
    """ generating k results for get_adjustable_random_list()
        function 
    """
    results = []
    for _ in range(k):
        results.append(
            rand.choice(
                get_adjustable_random_list(
                    min_value=0,
                    max_value=100,
                    numbers_to_adjust=[
                        10,15,20
                    ]
                )
            )
        )
    return results 


def run_graph_test(
    values: list[int]
) -> int:
    """ visualisng plot with inited random values via 
        get_adjustable_random_list()
    """

    collection = Counter(values)

    plt.figure(figsize = (10, 5))
    plt.bar(
        list(collection.keys()), 
        list(collection.values()), 
        color ='maroon',
        width = 0.4
    )

    plt.xlabel("Numbers")
    plt.ylabel("Choiced by random")
    plt.title("Adjustable random test case")
    plt.show()

    return 1