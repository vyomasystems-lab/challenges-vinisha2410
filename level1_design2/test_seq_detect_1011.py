# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    cocotb.log.info('#### CTB: Develop your test here! ######')

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f'inp={dut.inp_bit.value}  state={dut.current_state.value} out={dut.seq_seen.value}') 
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut._log.info(f'inp={dut.inp_bit.value}  state={dut.current_state.value} out={dut.seq_seen.value}') 
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut._log.info(f'inp={dut.inp_bit.value}  state={dut.current_state.value} out={dut.seq_seen.value}') 
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut._log.info(f'inp={dut.inp_bit.value}  state={dut.current_state.value} out={dut.seq_seen.value} ') 
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut._log.info(f'inp={dut.inp_bit.value}  state={dut.current_state.value} out={dut.seq_seen.value}') 
    errors=[]
    try:
            assert dut.seq_seen.value == 1, "error"
    except:
            errors.append(dut.seq_seen.value)
            dut._log.info(f'ERROR at input={dut.inp_bit.value} state={dut.current_state.value} out={dut.seq_seen.value} expected_output={1}')
            dut._log.info(f'BUG_1: Output is not seen after one clock cycle instead it is seen at same clock cycle')
              

    dut.reset.value = 1
    await FallingEdge(dut.clk) 
    dut._log.info(f' state={dut.current_state.value} inp={dut.inp_bit.value} out={dut.seq_seen.value} ') 
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    dut._log.info(f' state={dut.current_state.value} inp={dut.inp_bit.value} out={dut.seq_seen.value}')
    cocotb.log.info('#### CTB: Develop your test here! ######')

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f'inp={dut.inp_bit.value} state={dut.current_state.value} out={dut.seq_seen.value}')
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f'inp={dut.inp_bit.value} state={dut.current_state.value}  out={dut.seq_seen.value}')
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut._log.info(f'inp={dut.inp_bit.value} state={dut.current_state.value} out={dut.seq_seen.value} ')
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut._log.info(f'inp={dut.inp_bit.value} state={dut.current_state.value} out={dut.seq_seen.value} ')
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut._log.info(f'inp={dut.inp_bit.value} state={dut.current_state.value} out={dut.seq_seen.value} ')
   
    try:
            assert dut.seq_seen.value == 1, "error"
    except:
            errors.append(dut.seq_seen.value)
            dut._log.info(f'ERROR at input={dut.inp_bit.value} state={dut.current_state.value} out={dut.seq_seen.value} expected_output={1}')
            dut._log.info(f'BUG_2: Sequence is not at all detected even in same clock cycle. Bug in state transition')
            
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut.reset.value = 1
    await FallingEdge(dut.clk) 
    dut._log.info(f' state={dut.current_state.value} inp={dut.inp_bit.value} ') 
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    dut._log.info(f' state={dut.current_state.value} inp={dut.inp_bit.value} ')
    cocotb.log.info('#### CTB: Develop your test here! ######')

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f'inp={dut.inp_bit.value} state={dut.current_state.value} out={dut.seq_seen.value} ')
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info(f'inp={dut.inp_bit.value} state={dut.current_state.value} out={dut.seq_seen.value} ')
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut._log.info(f'inp={dut.inp_bit.value} state={dut.current_state.value} out={dut.seq_seen.value}')
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut._log.info(f'inp={dut.inp_bit.value} state={dut.current_state.value} out={dut.seq_seen.value}')
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut._log.info(f'inp={dut.inp_bit.value} state={dut.current_state.value} out={dut.seq_seen.value} ')
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut._log.info(f'inp={dut.inp_bit.value} state={dut.current_state.value} out={dut.seq_seen.value}')
   
    try:
            assert dut.seq_seen.value == 1, "error"
    except:
            errors.append(dut.seq_seen.value)
            dut._log.info(f'ERROR at input={dut.inp_bit.value} state={dut.current_state.value} out={dut.seq_seen.value} expected_output={1}')
            dut._log.info(f'BUG_3 Sequence is not at all detected even in same clock cycle. Bug in state transition')
            
    

    
