# Test Case Examples

Use these test cases to help verify and debug your project.

---

## Budget Tracker Test Cases

### Test Case 1: Add Income

- Input:
  - Description: Freelance
  - Amount: 500
  - Category: Work
  - Is Income: yes
- Expected Output:
  - Income: Freelance | £500.00 | Category: Work
  - Balance: £500.00

### Test Case 2: Add Expense

- Input:
  - Description: Lunch
  - Amount: 15
  - Category: Food
  - Is Income: no
- Expected Output:
  - Expense: Lunch | £15.00 | Category: Food
  - Balance: £485.00

### Test Case 3: Multiple Transactions

- Add:
  - Income: Salary (£2000)
  - Expense: Rent (£800)
  - Expense: Internet (£50)
- Expected Output:
  - 3 transactions listed
  - Balance: £1150.00

### Test Case 4: Save and Reload

- Add transactions
- Exit and restart program
- Expected:
  - All transactions are restored correctly from file
  - Balance remains consistent

### Edge Case 1: Zero Amount

- Input:
  - Description: Test Zero
  - Amount: 0
  - Category: Misc
  - Is Income: yes
- Expected:
  - Should still show the transaction (optional: handle as invalid)

### Edge Case 2: Negative Amount

- Input:
  - Description: Mistake
  - Amount: -100
  - Category: Error
  - Is Income: yes
- Expected:
  - May cause incorrect balance
  - (Optional: validate and block negative numbers)

### Edge Case 3: Empty Description or Category

- Input:
  - Description: (empty)
  - Category: (empty)
- Expected:
  - Might show incomplete transaction
  - (Optional: ask user to retry)

---

## Contact Manager Test Cases

### Test Case 1: Add Contact

- Input:
  - Name: Alice
  - Phone: 123-456
  - Email: alice@mail.com
- Expected Output:
  - Alice | Phone: 123-456 | Email: alice@mail.com

### Test Case 2: Search Contact

- Search: "ali"
- Expected:
  - Finds Alice (case-insensitive)

### Test Case 3: Delete Contact

- Input: Alice
- Expected:
  - Alice removed from list

### Test Case 4: Save and Load

- Add multiple contacts, save, exit, reload
- Expected:
  - Contacts are restored from file

### Test Case 5: Multiple Entries

- Add:
  - Bob, 987-654, bob@mail.com
  - Charlie, 222-333, charlie@mail.com
- Expected:
  - All entries printed with correct formatting

### Edge Case 1: Duplicate Names

- Add 2 contacts named "Alex"
- Delete one
- Expected:
  - Both or only one may be deleted (depends on implementation)
  - (Optional: ask for confirmation or use phone/email to uniquely identify)

### Edge Case 2: Empty Fields

- Name, phone, or email left blank
- Expected:
  - Could cause formatting issues
  - (Optional: validate input before adding)

### Edge Case 3: Invalid Email Format

- Input: john@notanemail
- Expected:
  - Will still be accepted unless validated
  - (Optional: add email format checker)

### Edge Case 4: Long Names or Emails

- Input: Very long name or email string
- Expected:
  - Should still save and display, but formatting may break
