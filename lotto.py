from random import randint
from typing import Set

class Lotto():

  def draw(self) -> Set[int]:
    results: Set[int]
    results = set()

    while len(results) < 6:
      results.add(randint(1, 49))

    return results


  def check_result(self, ticket: Set[int], results: Set[int]) -> Set[int]:
    return (ticket&results)
