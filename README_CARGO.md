# Cargo Loading Optimization

## Overview
This project solves the **Cargo Loading Optimization** problem. The objective is to assign multiple cargos to a specific set of tanks in a way that maximizes the total loaded cargo volume while adhering to strict operational constraints.

## Problem Statement
Given a set of **cargos** (each with a total cubic volume) and a set of **tanks** (each with a fixed capacity), the program determines the optimal allocation strategy.

### Constraints
*   **Cargo Splitting is Allowed:** A single cargo can be divided and stored across multiple tanks.
*   **One Cargo Per Tank:** A specific tank can only hold one type of cargo (no mixing).
*   **Capacity Limits:** A tank cannot hold more cargo than its defined capacity.

## Approach: The Greedy Strategy
To solve this efficiently, a **Greedy Algorithm** is employed. This approach works optimally because cargo splitting is allowed, meaning there is no benefit to leaving tank capacity unused if cargo is available.

### Steps:
1.  **Sort Cargos:** Arrange all cargos in descending order of volume.
2.  **Sort Tanks:** Arrange all tanks in descending order of capacity.
3.  **Allocate:** Iteratively assign the largest available tanks to the largest remaining cargos.
4.  **Fill:** Load as much as possible into the current tank without violating constraints.

## ⚙️ Key Logic
The core allocation logic is defined by the following formula:

```python
load = min(remaining_cargo_volume, tank_capacity)
```

### This logic ensures:

1. ✅ No Overflow: The load never exceeds the tank's capacity.
2. ✅ No Over-allocation: We never load more cargo than exists.

3. ✅ Natural Splitting: If remaining_cargo_volume > tank_capacity, the cargo is naturally split, filling the current tank completely while the remainder waits for the next available tank.

### 📊 Complexity Analysis
Metric	Complexity	Reason
Time Complexity	O(N log N)	Dominated by the sorting of cargos and tanks.
Space Complexity	O(N)	Required to store the input lists and allocation results.

### 📤 Output
The program generates a detailed report containing:
Allocation Map: Which cargo is assigned to which tank and the specific volume loaded.
Total Volume: The aggregate volume of all loaded cargo.

### 📝 Summary
This solution provides a high-performance, logic-driven method to maximize cargo loading. By leveraging sorting and greedy allocation, it ensures all constraints are respected while optimizing storage utility.