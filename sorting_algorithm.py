from typing import List, Tuple
from math import log2

# -------- Bubble Sort --------
def bubble_sort_count(a: List[int]) -> Tuple[List[int], int, int]:
    arr = a[:]
    n = len(arr)
    comps = moves = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comps += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                moves += 3
                swapped = True
        if not swapped:
            break
    return arr, comps, moves

# -------- Merge Sort --------
def merge_sort_count(a: List[int]) -> Tuple[List[int], int, int]:
    arr = a[:]
    comps = moves = 0
    def merge(L: List[int], R: List[int]) -> List[int]:
        nonlocal comps, moves
        i = j = 0
        out: List[int] = []
        while i < len(L) and j < len(R):
            comps += 1
            if L[i] <= R[j]:
                out.append(L[i]); i += 1
            else:
                out.append(R[j]); j += 1
            moves += 1
        if i < len(L):
            out.extend(L[i:]); moves += len(L) - i
        if j < len(R):
            out.extend(R[j:]); moves += len(R) - j
        return out
    def sort(x: List[int]) -> List[int]:
        if len(x) <= 1: return x
        m = len(x) // 2
        return merge(sort(x[:m]), sort(x[m:]))
    out = sort(arr)
    return out, comps, moves

# -------- Quick Sort --------
def quick_sort_count(a: List[int]) -> Tuple[List[int], int, int]:
    arr = a[:]
    comps = moves = 0
    def sort(lo: int, hi: int):
        nonlocal comps, moves
        if lo >= hi: return
        mid = (lo + hi) // 2         # middle pivot for determinism
        arr[hi], arr[mid] = arr[mid], arr[hi]; moves += 2
        pivot = arr[hi]
        i = lo
        for j in range(lo, hi):
            comps += 1
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]; moves += 2
                i += 1
        arr[i], arr[hi] = arr[hi], arr[i]; moves += 2
        sort(lo, i - 1); sort(i + 1, hi)
    sort(0, len(arr) - 1)
    return arr, comps, moves

# -------- main --------
def main():
    staticlist = [64, 256, 128, 512, 32]   # static list

    print("\n=== Sorting Complexity (staticlist List) ===")
    print(f"Array: {staticlist}\n")
    header = f"{'Algorithm':<8}  {'comparisons':>12}  {'moves':>10}"
    print(header)
    print("-" * len(header))

    out, c, m = bubble_sort_count(staticlist); print(f"{'Bubble':<8}  {c:12d}  {m:10d}")
    out, c, m = merge_sort_count(staticlist);  print(f"{'Merge':<8}   {c:11d}  {m:10d}")
    out, c, m = quick_sort_count(staticlist);  print(f"{'Quick':<8}   {c:11d}  {m:10d}")


def bigo_check():
    sizes = [32, 64, 128, 256, 512]
    print("\n=== Big-O style scaling (comparison ratios) ===")
    print(f"{'n':>5}  {'Bubble c/n^2':>14}  {'Merge c/(nlogn)':>16}  {'Quick c/(nlogn)':>16}")
    for n in sizes:
        data = list(range(1, n+1))  # deterministic [1..n]
        _, cb, _ = bubble_sort_count(data)
        _, cm, _ = merge_sort_count(data)
        _, cq, _ = quick_sort_count(data)
        print(f"{n:5d}  {cb/(n*n):14.4f}  {cm/(n*log2(n)):16.4f}  {cq/(n*log2(n)):16.4f}")


if __name__ == '__main__':
    main()
    bigo_check()