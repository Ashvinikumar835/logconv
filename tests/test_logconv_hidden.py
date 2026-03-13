import os
from pathlib import Path

import cocotb
from cocotb.triggers import Timer
from cocotb_tools.runner import get_runner

@cocotb.test()
async def test_encryption_1(dut):
    """Test log conversion with fp16 value of 0x4000 (2)"""
    print("fp16tolog conversion")
    dut.fp16_in.value = 0x4000
    await Timer(5, unit="ns")  
   
    dut._log.info("fp16_in = %d,   log_out_q5_10= %x",
                  dut.fp16_in.value, dut.log_out_q5_10.value)
    assert dut.log_out_q5_10.value == 1024, "log conversion is not correct"  


@cocotb.test()
async def test_encryption_2(dut):
    """Test log conversion with fp16 value of 0x4200 (3)"""
    print("fp16tolog conversion")
    dut.fp16_in.value = 0x4200
    await Timer(5, unit="ns")  
   
    dut._log.info("fp16_in = %d,   log_out_q5_10= %x",
                  dut.fp16_in.value, dut.log_out_q5_10.value)
    assert dut.log_out_q5_10.value == 1536, "log conversion is not correct"

@cocotb.test()
async def test_encryption_3(dut):
    """Test log conversion with fp16 value of 0x4400 (3)"""
    print("fp16tolog conversion")
    dut.fp16_in.value = 0x4400
    await Timer(5, unit="ns")  
   
    dut._log.info("fp16_in = %d,   log_out_q5_10= %x",
                  dut.fp16_in.value, dut.log_out_q5_10.value)
    assert dut.log_out_q5_10.value == 2048, "log conversion is not correct"

@cocotb.test()
async def test_encryption_4(dut):
    """Test log conversion with fp16 value of 0x5600 (3)"""
    print("fp16tolog conversion")
    dut.fp16_in.value = 0x5600
    await Timer(5, unit="ns")  
   
    dut._log.info("fp16_in = %d,   log_out_q5_10= %x",
                  dut.fp16_in.value, dut.log_out_q5_10.value)
    assert dut.log_out_q5_10.value == 6656, "log conversion is not correct"

   
####tc5

@cocotb.test()
async def test_encryption_5(dut):
    """Test log conversion with fp16 value of 0x3E00 (1.5)"""
    print("fp16tolog conversion")

    dut.fp16_in.value = 0x3E00
    await Timer(5, unit="ns")

    dut._log.info("fp16_in = %d, log_out_q5_10 = %x",
                  dut.fp16_in.value, dut.log_out_q5_10.value)

    assert dut.log_out_q5_10.value == 512, "log conversion incorrect"


###TC6
@cocotb.test()
async def test_encryption_6(dut):
    """Test log conversion with fp16 value of 0x3800 (0.5)"""
    print("fp16tolog conversion")

    dut.fp16_in.value = 0x3800
    await Timer(5, unit="ns")

    dut._log.info("fp16_in = %d, log_out_q5_10 = %x",
                  dut.fp16_in.value, dut.log_out_q5_10.value)

    assert dut.log_out_q5_10.value == 64512, "log conversion incorrect"

###TC7

@cocotb.test()
async def test_encryption_7(dut):
    """Test log conversion with fp16 value of 0x4100 (~2.25)"""
    print("fp16tolog conversion")

    dut.fp16_in.value = 0x4100
    await Timer(5, unit="ns")

    dut._log.info("fp16_in = %d, log_out_q5_10 = %x",
                  dut.fp16_in.value, dut.log_out_q5_10.value)

    assert dut.log_out_q5_10.value == 1280, "log conversion incorrect"
   
###TC8
@cocotb.test()
async def test_encryption_8(dut):
    """Test log conversion with fp16 value of 0x4600"""
    print("fp16tolog conversion")

    dut.fp16_in.value = 0x4600
    await Timer(5, unit="ns")

    dut._log.info("fp16_in = %d, log_out_q5_10 = %x",
                  dut.fp16_in.value, dut.log_out_q5_10.value)

    assert dut.log_out_q5_10.value == 2560, "log conversion incorrect"

###TC9
@cocotb.test()
async def test_encryption_9(dut):
    """Test log conversion with fp16 value of 0"""
    print("fp16tolog conversion")

    dut.fp16_in.value = 0x0000
    await Timer(5, unit="ns")

    dut._log.info("fp16_in = %d, log_out_q5_10 = %x",
                  dut.fp16_in.value, dut.log_out_q5_10.value)

    assert dut.log_out_q5_10.value == 32768, "log conversion incorrect"



# CRITICAL: Pytest wrapper function
def test_logconv_runner():
    import os
    from pathlib import Path
    from cocotb_tools.runner import get_runner
    """Pytest wrapper to run cocotb tests"""
    sim = os.getenv("SIM", "icarus")
    proj_path = Path(__file__).resolve().parent.parent
    #logconv RTL source files( need all module)
    sources = [
        proj_path / "golden/logconv.v",
       proj_path /"golden/bk_adder16bit.v",
    ]
    
    runner = get_runner(sim)
    runner.build(
        sources=sources,
        hdl_toplevel="logconv",
        always=True,
    )
    
    runner.test(
        hdl_toplevel="logconv",
        test_module="test_logconv_hidden"
    )
