# Level1_design1: MUX Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.v

![](https://i.imgur.com/miWGA1o.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux module) which has 5-bit select line *sel* and thirty one 2-bit inputs *inp0*, *inp1*.. till *inp30*. Depending on *sel* value, one of the 31 inputs get selected which is then driven to the output *out*.

The out list is created to store in case any bugs are found in design. The inp list is created to store thirty one 2-bit value. The stored values in the list is then assigned to the input port. 

```
dut.inp0.value=inp[0]
dut.inp1.value=inp[1]
.
.
dut.inp30.value=inp[30]

```
The *sel* input is assigned all possible values using for loop and the design is tasted.

The assert statement is used for comparing the multiplexer's output to the expected value and it is given inside try block. If there is an assertion error,error statement inside except block is printed and value is appended to out list.

The assert statement outside the for loop checks if there's any bugs appended to 'out'. If len(out) is not equal to zero, the whole test fails.
The following error is seen:
```
assert dut.sum.value == A+B, "Adder result is incorrect: {A} + {B} != {SUM}, expected value={EXP}".format(
                     AssertionError: Adder result is incorrect: 7 + 5 != 2, expected value=12
```
## Test Scenario 
- Test Inputs: inp12=1 sel=12
- Expected Output: out=01
- Observed Output in the DUT dut.out.value=00

- Test Inputs: inp30=1 sel=30
- Expected Output: out=01
- Observed Output in the DUT dut.out.value=00

- Test Inputs: inp12=2 sel=12
- Expected Output: out=02
- Observed Output in the DUT dut.out.value=00

- Test Inputs: inp30=2 sel=30
- Expected Output: out=02
- Observed Output in the DUT dut.out.value=00

- Test Inputs: inp12=3 sel=12
- Expected Output: out=01
- Observed Output in the DUT dut.out.value=00

- Test Inputs: inp30=3 sel=30
- Expected Output: out=3
- Observed Output in the DUT dut.out.value=00

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
5'b01011: out = inp11;
5'b01101: out = inp12;   ====> BUG
5'b01101: out = inp13;

5'b11100: out = inp28;
5'b11101: out = inp29;
default: out = 0;         ====> BUG (No case statement for 30th select line)

```
For the mux design, the case statement must be 5'b01100: out = inp12; 
An additional case statement 5'b11110: out = inp30; must be included.

## Design Fix
Updating the design and re-running the test makes the test pass.

![](https://i.imgur.com/5XbL1ZH.png)

The updated design is checked in as adder_fix.v

## Verification Strategy

## Is the verification complete ?
