# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def test_seq(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    
    dut.reset.value = 1
    await RisingEdge(dut.clk)   
    dut.reset.value = 0
    
    dut._log.info(f'initial   state={dut.current_state.value} ') 

    dut.inp.value = 1111
    #await RisingEdge(dut.clk)
    await Timer(20, units='us')
    dut._log.info(f'inp={int(dut.inp.value)}  access={dut.access.value} alarm={dut.alarm.value} count={dut.count.value}') 
    dut.inp.value = 1222
    #await RisingEdge(dut.clk)
    await Timer(20, units='us')
    dut.inp.value = 1333
    dut._log.info(f'inp={int(dut.inp.value)}   access={dut.access.value} alarm={dut.alarm.value} count={dut.count.value}')
    #await RisingEdge(dut.clk)
    await Timer(20, units='us')
    dut.inp.value = 1444
    dut._log.info(f'inp={int(dut.inp.value)}   access={dut.access.value} alarm={dut.alarm.value} count={dut.count.value}')
    await Timer(20, units='us')
    dut.inp.value = 1555
    dut._log.info(f'inp={int(dut.inp.value)}  access={dut.access.value} alarm={dut.alarm.value} count={dut.count.value}')

    assert dut.alarm.value==1, "alarm doesnt go high at count={count}".format(count=dut.count.value)
    

    

 
    