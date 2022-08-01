# Level1_design2: Sequence Detector Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.


![]([https://i.imgur.com/miWGA1o.png](https://github.com/vyomasystems-lab/challenges-vinisha2410/blob/master/images/Gitpod%20id.png))

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under
Test which takes in inp_bit, reset and clk as input

The errors list is created to store values in case any bugs are found in design.The values are assigned to the input port using 
```
dut.reset.value = 1
dut.inp_bit.value = 1
```

The assert statement is used for comparing the sequence_detector's output to the expected value and it is given inside 'try' block. If there is an assertion error, statement inside 'except' block is printed and value is appended to errors list.

The final assert statement outside the checks if there's any bugs appended to 'errors' list
. If len(errors) is not equal to zero, the whole test fails.

The following error is seen:
![](https://github.com/vyomasystems-lab/challenges-vinisha2410/blob/master/images/seq_failed_test.png)
![](https://github.com/vyomasystems-lab/challenges-vinisha2410/blob/master/images/seq_failed_test%20(2).png)
```
assert len(errors) == 0, "test fails"
                     AssertionError: test fails
```
## Test Scenario **(Important)**
- Test Inputs: 

dut.inp_bit.value = 1

dut.inp_bit.value = 1

dut.inp_bit.value = 0

dut.inp_bit.value = 1

dut.inp_bit.value = 1

dut.inp_bit.value = 0
- Expected Output: seq_seen=1
- Observed Output in the DUT dut.seq_seen.value=0
<br/>

- Test Inputs: 
 
dut.inp_bit.value = 1

dut.inp_bit.value = 0

dut.inp_bit.value = 1

dut.inp_bit.value = 0

dut.inp_bit.value = 1

dut.inp_bit.value = 1

dut.inp_bit.value = 0

- Expected Output: seq_seen=1
- Observed Output in the DUT dut.seq_seen.value=0
<br/>

- Test Inputs: 

dut.inp_bit.value = 1

dut.inp_bit.value = 0

dut.inp_bit.value = 1

dut.inp_bit.value = 1

dut.inp_bit.value = 0

dut.inp_bit.value = 1

dut.inp_bit.value = 1

- Expected Output: seq_seen=1
- Observed Output in the DUT dut.seq_seen.value=0
<br/>


Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;   ====> BUG1
        else
          next_state = SEQ_10;
      end
      
SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;   ====> BUG2
      end
      
SEQ_1011:
      begin
        next_state = IDLE;     ====> BUG3
      end
 
```
In SEQ_1 case, the next_state under if block should be SEQ_1
In SEQ_101 case, the next_state under else block should be SEQ_10
In SEQ_1011 case, if inp_bit=1, next_state= SEQ_1 else next_state= SEQ_10

## Design Fix
Updating the design and re-running the test makes the test pass.

![]([https://i.imgur.com/5XbL1ZH.png](https://github.com/vyomasystems-lab/challenges-vinisha2410/blob/master/images/seq_passed_test.png))

The updated design is provided in corrected_design folder

## Verification Strategy
In case of sequnce detector, state transitions are important to note. Therefore the current state has to be monitored. For overlapping sequence detector, non-sequence can be start of another sequence. 1011 sequence is provided after a non-sequence as input and states are monitored. 

## Is the verification complete ?
Yes, possible combination of input has been given to note the state transitions. The design has 3 bugs in total.
