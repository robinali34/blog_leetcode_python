---
layout: post
title: "2043. Simple Bank System"
date: 2025-10-20 13:50:00 -0700
categories: leetcode algorithm medium design data-structure
permalink: /2025/10/20/medium-2043-simple-bank-system/
---

# 2043. Simple Bank System

**Difficulty:** Medium  
**Category:** Design, Data Structure

## Problem Statement

You have been tasked with writing a program for a popular bank that will automate all its incoming transactions (transfer, deposit, and withdraw). The bank has `n` accounts numbered from `1` to `n`. The initial balance of each account is stored in a **0-indexed** integer array `balance`, with the `(i + 1)th` account having an initial balance of `balance[i]`.

Execute all the **valid** transactions. A transaction is **valid** if:

- The given account number(s) are between `1` and `n`, and
- The amount of money withdrawn or transferred from is less than or equal to the balance of the account.

Implement the `Bank` class:

- `Bank(long[] balance)` Initializes the object with the 0-indexed integer array `balance`.
- `boolean transfer(int account1, int account2, long money)` Transfers `money` dollars from the account numbered `account1` to the account numbered `account2`. Returns `true` if the transaction was successful, `false` otherwise.
- `boolean deposit(int account, long money)` Deposits `money` dollars to the account numbered `account`. Returns `true` if the transaction was successful, `false` otherwise.
- `boolean withdraw(int account, long money)` Withdraws `money` dollars from the account numbered `account`. Returns `true` if the transaction was successful, `false` otherwise.

## Examples

### Example 1:
```
Input
["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
[[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]

Output
[null, true, true, true, false, false]

Explanation
Bank bank = new Bank([10, 100, 20, 50, 30]);
bank.withdraw(3, 10);    // return true, account 3 has a balance of $20, so it is valid to withdraw $10.
                         // Account 3 has $20 - $10 = $10 after the transaction.
bank.transfer(5, 1, 20); // return true, account 5 has a balance of $30, so it is valid to transfer $20.
                         // Account 5 has $30 - $20 = $10 after the transaction.
                         // Account 1 has $10 + $20 = $30 after the transaction.
bank.deposit(5, 20);     // return true, it is valid to deposit $20 to account 5.
                         // Account 5 has $10 + $20 = $30 after the transaction.
bank.transfer(3, 4, 15); // return false, the current balance of account 3 is $10,
                         // so it is invalid to transfer $15 from it.
bank.withdraw(10, 50);   // return false, it is invalid because account 10 does not exist.
```

## Constraints

- `n == balance.length`
- `1 <= n, account, account1, account2 <= 10^5`
- `0 <= balance[i] <= 10^12`
- `1 <= money <= 10^12`
- At most `10^4` calls will be made to each function `transfer`, `deposit`, and `withdraw`.

## Approach

This is a **Data Structure Design** problem that simulates a simple bank system. The key requirements are:

1. **Account Validation:** Ensure account numbers are valid (1 to n)
2. **Balance Checking:** Ensure sufficient funds for withdrawals and transfers
3. **Atomic Operations:** Each transaction should be atomic (all-or-nothing)
4. **Efficient Operations:** All operations should be O(1) time complexity

### Algorithm:
1. **Store balances** in a vector/array for O(1) access
2. **Validate accounts** before any operation
3. **Check sufficient funds** before withdrawals and transfers
4. **Perform operations** atomically (check first, then modify)
5. **Return success/failure** based on validation results

## Solution

```python
class Bank:
    def __init__(self, balance: list[int]):
        self.balance = balance
    
    def isValid(self, account: int) -> bool:
        return 1 <= account <= len(self.balance)
    
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.isValid(account1) and self.isValid(account2) and self.balance[account1 - 1] >= money:
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        return False
    
    def deposit(self, account: int, money: int) -> bool:
        if self.isValid(account):
            self.balance[account - 1] += money
            return True
        return False
    
    def withdraw(self, account: int, money: int) -> bool:
        if self.isValid(account) and self.balance[account - 1] >= money:
            self.balance[account - 1] -= money
            return True
        return False

/**
 * Your Bank object will be instantiated and called as such:
 * Bank* obj = new Bank(balance);
 * bool param_1 = obj->transfer(account1,account2,money);
 * bool param_2 = obj->deposit(account,money);
 * bool param_3 = obj->withdraw(account,money);
 */
```

## Explanation

### Class Design:

**Private Members:**
- `vector<long long> balance`: Stores account balances (0-indexed)
- `bool isValid(int account)`: Helper function to validate account numbers

**Public Methods:**
1. **Constructor:** Initialize with given balance array
2. **transfer():** Move money between accounts
3. **deposit():** Add money to an account
4. **withdraw():** Remove money from an account

### Step-by-Step Process:

**Transfer Operation:**
1. **Validate both accounts** exist (1 to n)
2. **Check sufficient funds** in source account
3. **Perform atomic transfer** (subtract from source, add to destination)
4. **Return success/failure**

**Deposit Operation:**
1. **Validate account** exists
2. **Add money** to account balance
3. **Return success/failure**

**Withdraw Operation:**
1. **Validate account** exists
2. **Check sufficient funds** available
3. **Subtract money** from account balance
4. **Return success/failure**

### Example Walkthrough:
For `balance = [10, 100, 20, 50, 30]` (5 accounts):

- **withdraw(3, 10):** Account 3 has $20, withdraw $10 → Success, balance = $10
- **transfer(5, 1, 20):** Account 5 has $30, transfer $20 to account 1 → Success
- **deposit(5, 20):** Add $20 to account 5 → Success, balance = $30
- **transfer(3, 4, 15):** Account 3 has $10, insufficient for $15 → Failure
- **withdraw(10, 50):** Account 10 doesn't exist → Failure

## Complexity Analysis

**Time Complexity:** O(1) for all operations
- **Constructor:** O(n) where n is number of accounts
- **transfer():** O(1) - constant time validation and operations
- **deposit():** O(1) - constant time validation and operations
- **withdraw():** O(1) - constant time validation and operations

**Space Complexity:** O(n) where n is the number of accounts
- **Storage:** Vector to store account balances
- **Auxiliary:** O(1) for validation and operations

## Key Insights

1. **Account Indexing:** Accounts are 1-indexed but stored in 0-indexed array
2. **Validation First:** Always validate accounts before performing operations
3. **Atomic Operations:** Check conditions before modifying balances
4. **Efficient Design:** O(1) operations for all transactions
5. **Error Handling:** Return false for invalid operations instead of throwing exceptions

## Design Patterns

### Data Structure Design:
- **Encapsulation:** Private data members with public interface
- **Validation:** Centralized validation logic
- **Atomic Operations:** All-or-nothing transaction semantics

### Error Handling:
- **Graceful Degradation:** Return false instead of crashing
- **Input Validation:** Check all preconditions before operations
- **Consistent Interface:** All methods return boolean success status

## Alternative Approaches

### Using Map for Dynamic Accounts:
```python
class Bank:
    def __init__(self, balance: list[int]):
        self.balance = {}
        for i, bal in enumerate(balance):
            self.balance[i + 1] = bal
    
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 in self.balance and account2 in self.balance and self.balance[account1] >= money:
            self.balance[account1] -= money
            self.balance[account2] += money
            return True
        return False
    # ... other methods
```

### With Additional Features:
```python
class Bank:
    def __init__(self, balance: list[int]):
        self.balance = balance
        self.transactionLog = []
    
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.isValid(account1) and self.isValid(account2) and self.balance[account1 - 1] >= money:
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            self.transactionLog.append(f"Transfer: {account1} -> {account2} ${money}")
            return True
        return False
    # ... other methods
```

The vector-based approach is optimal for this problem due to its simplicity, efficiency, and direct array access patterns.
