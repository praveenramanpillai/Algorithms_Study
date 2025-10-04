import time
import random
from collections import deque
from typing import Any, List, Dict


# =================== DATA STRUCTURE ====================================

class Queue:
    def __init__(self):
        self._items: deque[Any] = deque()
    def add(self, item: Any):
        self._items.append(item)  # Enqueue
    def remove(self) -> Any:
        return self._items.popleft()  # Dequeue (FIFO)


class Stack:
    def __init__(self):
        self._items: deque[Any] = deque()
    def add(self, item: Any):
        self._items.append(item)  # Push
    def remove(self) -> Any:
        return self._items.pop()  # Pop (LIFO)


# ==================== COMPARISON LOGIC ==========================

TEST_SIZES = [10000, 100000, 1000000, 10000000]
NUM_TRIALS = 3

def run_comparison() -> List[Dict[str, Any]]:
    results: List[Dict[str, Any]] = []

    print("--- Queue vs. Stack Performance Comparison ---")

    for N in TEST_SIZES:
        # Create N random integers for the test size (N).
        test_data = [random.randint(1, 1_000_000) for _ in range(N)]
        current_N_results = {'N': N}

        for structure_name, StructureClass in [("Queue", Queue), ("Stack", Stack)]:
            total_add_time: float = 0.0
            total_remove_time: float = 0.0

            for _ in range(NUM_TRIALS):
                # --- ADD (Enqueue/Push) ---
                ds = StructureClass()
                start_time = time.perf_counter()
                for item in test_data:
                    ds.add(item)
                end_time = time.perf_counter()
                total_add_time += (end_time - start_time)

                # --- REMOVE (Dequeue/Pop) ---
                start_time = time.perf_counter()
                for _ in range(N):
                    ds.remove()
                end_time = time.perf_counter()
                total_remove_time += (end_time - start_time)

            # Store average times
            avg_add_time = total_add_time / NUM_TRIALS
            avg_remove_time = total_remove_time / NUM_TRIALS

            current_N_results[f'{structure_name}_Avg_Add_sec'] = avg_add_time
            current_N_results[f'{structure_name}_Avg_Remove_sec'] = avg_remove_time

        results.append(current_N_results)
        print(f"Completed tests for N = {N:,}")

    return results


# ========================== DISPLAY RESULTS ===============================

def display_comparison_data(data: List[Dict[str, Any]]):
    print("\nQUEUE (FIFO) vs. STACK (LIFO) - EMPIRICAL PERFORMANCE DATA (in seconds):")
    header_format = "{:<12} | {:<17} | {:<17} | {:<17} | {:<17}"
    row_format = "{:<12} | {:<17f} | {:<17f} | {:<17f} | {:<17f}"

    print(header_format.format("Operations", "Queue_Avg_Add", "Queue_Avg_Remove", "Stack_Avg_Add",
                               "Stack_Avg_Remove"))
    print("-" * 95)

    for row in data:
        print(row_format.format(
            row['N'],
            row['Queue_Avg_Add_sec'],
            row['Queue_Avg_Remove_sec'],
            row['Stack_Avg_Add_sec'],
            row['Stack_Avg_Remove_sec']
        ))
    print("=" * 95)


if __name__ == "__main__":
    comparison_data = run_comparison()
    display_comparison_data(comparison_data)