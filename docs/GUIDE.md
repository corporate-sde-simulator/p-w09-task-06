# Learning Guide - unknown

> **Welcome to Product-Track Week 9, Task 6!**
> This is a **learning task**. This guide teaches you the unknown concepts you need . Take your time and read carefully.

---

## What You Need To Do (Summary)

1. **Read** `TICKET.md` to understand the task
2. **Read** this guide to learn the unknown syntax you'll need
3. **Find the root cause** by investigating the error logs and tracing the code execution
4. **Fix the bugs** using what you learned
5. **Run the tests** to verify your fix: `npm test`
6. **Add new tests** in the `tests/` folder to prove your fix works

---

## JavaScript (Node.js) Quick Reference

### Variables and Types
```javascript
const name = "Alice";           // constant - can't be reassigned
let count = 42;                 // variable - can be reassigned
const items = [1, 2, 3];       // array
const config = {key: "value"};  // object
const isActive = true;          // boolean
// DON'T use 'var' - it has scoping issues
```

### Functions
```javascript
// Regular function
function greet(name, greeting = "Hello") {
    return ${greeting}, !;    // Template literal (backticks)
}

// Arrow function (shorter syntax, same thing)
const greet = (name) => Hello, !;

// Calling:
const result = greet("Alice");
```

### Classes
```javascript
class Calculator {
    constructor() {                     // Constructor
        this.history = [];              // 'this' = current object
    }

    add(a, b) {                         // Method
        const result = a + b;
        this.history.push(result);
        return result;
    }

    getHistory() {
        return [...this.history];       // Return a copy
    }
}

// Using it:
const calc = new Calculator();
calc.add(2, 3);
console.log(calc.getHistory());        // [5]

// Exporting (so other files can use it):
module.exports = Calculator;

// Importing:
const Calculator = require('./Calculator');
```

### Objects (Key-Value Storage)
```javascript
const user = {name: "Alice", age: 25};
user.name;                              // Access: "Alice"
user["name"];                           // Also works
user.email = "alice@test.com";          // Add/update
"name" in user;                         // Check key exists: true
const {name, age} = user;              // Destructuring
```

### Arrays
```javascript
const items = [1, 2, 3];
items.push(4);                          // Add to end
items.pop();                            // Remove last
items.length;                           // Length: 3
items.map(x => x * 2);                 // Transform: [2, 4, 6]
items.filter(x => x > 1);             // Filter: [2, 3]
items.forEach(item => console.log(item));  // Loop
```

### Error Handling
```javascript
try {
    const result = riskyOperation();
} catch (error) {
    console.error(Error: );
} finally {
    cleanup();
}
```

### Common Patterns You'll See
```javascript
// Null/undefined checks
if (!value) { return "Empty"; }             // falsy check
if (value === null) { return "Null"; }      // strict null check
if (value === undefined) { return "Undef"; } // strict undefined

// == vs === (IMPORTANT!)
"5" == 5      // true  (loose - converts types)
"5" === 5     // false (strict - checks type too)
// ALWAYS use === in real code

// Ternary operator
const status = isActive ? "active" : "inactive";

// Optional chaining
const city = user?.address?.city;  // undefined if any part is null
```

### How to Run Tests
```bash
# From the task folder:
npx jest tests/ --verbose

# Or if Jest is installed:
npm test
```

### How to Add a Test
```javascript
// In the test file:
test('should do something specific', () => {
    const obj = new MyClass();
    const result = obj.method(inputData);
    expect(result).not.toBeNull();        // Not null
    expect(result).toBe(expectedValue);   // Exact match
    expect(result.length).toBeGreaterThan(0);  // Comparison
});
```

---

## Project Structure

| File | Purpose |
|------|---------|
| `TICKET.md` | Your task assignment - **read this first!** |
| `src/docker-compose.yml` | Main source code - **has bugs to fix** |
| `src/Dockerfile` | Supporting code - **may also have bugs** |
| `tests/test_docker.py` | Test file - **add your tests here** |
| `docs/DESIGN.md` | Architecture decisions (background reading) |
| `docs/GUIDE.md` | This learning guide |
| `.context/` | Meeting notes and PR comments (background context) |

---

## The Incident (Why you are here)


---

## Step-by-Step Workflow

1. Open a terminal and navigate to this task folder
2. Read `TICKET.md` completely
3. Explore the `src/` files and investigate the execution flow
4. **Fix the root cause** of the incident
5. Run the tests:
   ```bash
   npm test
   ```
6. If tests pass, you're done with the fix
7. **Bonus:** Add a new test to `tests/` that specifically tests the bug you fixed

---

## Common Mistakes to Avoid

- Don't change the function signatures (method names, parameters) - only fix the logic inside
- Make sure all existing tests still pass after your changes
- If you're stuck, re-read the `TICKET.md` requirements section carefully
