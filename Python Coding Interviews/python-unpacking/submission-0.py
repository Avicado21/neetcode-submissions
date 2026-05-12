from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    num1, num2, num3 = triplet
    val = num1+num2+num3
    return val


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    h,w,l = box_dimensions
    val = h*w*l
    return val
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
