# Level3_design: Password based lock system
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![](https://github.com/vyomasystems-lab/challenges-vinisha2410/blob/master/images/Gitpod%20id.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test which takes inp,reset,clk as inputs 

The values are assigned to the input port using 
```
dut.inp.value = 1111
```

The assert statement is used for comparing the dut.alarm.value to the expected output .

The following error is seen:
![](https://github.com/vyomasystems-lab/challenges-vinisha2410/blob/master/images/Screenshot%20(1057).png)

```
assert dut.alarm.value==1, "alarm doesnt go high at count={count}".format(count=dut.count.value)
                     AssertionError: alarm doesnt go high at count=3
```
## Test Scenario 
- Test Inputs: 

dut.inp.value = 1111

dut.inp.value = 1222

dut.inp.value = 1333

dut.inp.value = 1444
- Expected Output: alarm=1
- Observed Output: dut.alarm.value=0

Output mismatches for the above inputs proving that there is a design bug

## Verification Strategy


## Is the verification complete ?


