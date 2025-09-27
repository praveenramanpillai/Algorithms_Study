
from dataclasses import dataclass
from typing import Callable, List, Tuple, Any, Dict
import random
import time
from datetime import datetime, timedelta


@dataclass
class Claim:
    claim_id: int
    patient_id: int
    amount_cents: int
    service_date_ts: int

def claim_key(c: Claim) -> Tuple[Any, ...]:
    return (c.service_date_ts, c.amount_cents, c.claim_id)


# Data generation of Random Medical Claims
# -----------------------
def gen_claims(n: int, seed: int = 42) -> List[Claim]:
    rng = random.Random(seed)
    base = datetime(2024, 1, 1)
    claims = []
    for i in range(n):
        dt = base + timedelta(days=rng.randint(0, 365))
        service_ts = int(dt.timestamp())
        amount_cents = rng.randint(100, 100000)
        patient_id = rng.randint(1000000, 9999999)
        claims.append(Claim(
            claim_id=i + 1,
            patient_id=patient_id,
            amount_cents=amount_cents,
            service_date_ts=service_ts
        ))
    rng.shuffle(claims)
    return claims


# -------Bubble Sort--------------
def bubble_sort(arr: List[Claim], key: Callable[[Claim], Tuple[Any, ...]]) -> Dict[str, float]:
    a = arr[:]
    n = len(a)
    comparisons = swaps = 0

    t0 = time.perf_counter()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if key(a[j]) > key(a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    t1 = time.perf_counter()
    return {"time_sec": t1 - t0, "comparisons": comparisons, "swaps": swaps, "n": n}


# -------Merge Sort-----------
def merge_sort(arr: List[Claim], key: Callable[[Claim], Tuple[Any, ...]]) -> Dict[str, float]:
    a = arr[:]
    comparisons = moves = 0

    def merge(left: List[Claim], right: List[Claim]) -> List[Claim]:
        nonlocal comparisons, moves
        i = j = 0
        out: List[Claim] = []
        while i < len(left) and j < len(right):
            comparisons += 1
            if key(left[i]) <= key(right[j]):
                out.append(left[i]); i += 1
            else:
                out.append(right[j]); j += 1
            moves += 1
        out.extend(left[i:]); out.extend(right[j:])
        moves += len(left) - i + len(right) - j
        return out

    def msort(xs: List[Claim]) -> List[Claim]:
        if len(xs) <= 1:
            return xs
        mid = len(xs) // 2
        return merge(msort(xs[:mid]), msort(xs[mid:]))

    t0 = time.perf_counter()
    _ = msort(a)
    t1 = time.perf_counter()

    return {"time_sec": t1 - t0, "comparisons": comparisons, "moves": moves, "n": len(a)}


# ---------Compare--------------
def compare():
    for n in (100, 500, 2000):
        claims = gen_claims(n)
        bub = bubble_sort(claims, claim_key)
        bub["algorithm"] = "Bubble"
        mer = merge_sort(claims, claim_key)
        mer["algorithm"] = "Merge"
        print(f"=== N={n} ===")
        for r in (bub, mer):
            print(r)

if __name__ == "__main__":
    compare()
