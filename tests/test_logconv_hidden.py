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



####################################################################

@cocotb.test()
async def test_encryption_corner_21(dut):
    dut.fp16_in.value = 0x0000
    await Timer(5, unit="ns")
    assert dut.log_out_q5_10.value == 32768




#@cocotb.test()
#async def test_encryption_corner_20(dut):
#    dut.fp16_in.value = 0x6C2A
#    await Timer(5, unit="ns")
#    assert dut.log_out_q5_10.value == 13354

@cocotb.test()
async def test_encryption_corner_19(dut):
    dut.fp16_in.value = 0x52F4
    await Timer(5, unit="ns")
    assert dut.log_out_q5_10.value == 5876


@cocotb.test()
async def test_encryption_corner_18(dut):
    dut.fp16_in.value = 0x4A6D
    await Timer(5, unit="ns")
    assert dut.log_out_q5_10.value == 3693


#@cocotb.test()
#async def test_encryption_corner_17(dut):
#    dut.fp16_in.value = 0x63FF
#    await Timer(5, unit="ns")
#    assert dut.log_out_q5_10.value == 11263


#@cocotb.test()
#async def test_encryption_corner_16(dut):
#    dut.fp16_in.value = 0x5BFF
#    await Timer(5, unit="ns")
#    assert dut.log_out_q5_10.value == 9215


@cocotb.test()
async def test_encryption_corner_15(dut):
    dut.fp16_in.value = 0x3C01
    await Timer(5, unit="ns")
    assert dut.log_out_q5_10.value == 1



@cocotb.test()
async def test_encryption_corner_14(dut):
    dut.fp16_in.value = 0x3C00
    await Timer(5, unit="ns")
    assert dut.log_out_q5_10.value == 0


@cocotb.test()
async def test_encryption_corner_13(dut):
    dut.fp16_in.value = 0x3BFF
    await Timer(5, unit="ns")
    assert dut.log_out_q5_10.value == 65535

@cocotb.test()
async def test_encryption_corner_12(dut):
    dut.fp16_in.value = 0x3405
    await Timer(5, unit="ns")
    assert dut.log_out_q5_10.value == 63493

@cocotb.test()
async def test_encryption_corner_11(dut):
    dut.fp16_in.value = 0x3801
    await Timer(5, unit="ns")
    assert dut.log_out_q5_10.value == 64513


@cocotb.test()
async def test_encryption_corner_10(dut):
    dut.fp16_in.value = 0x3C01
    await Timer(5, unit="ns")
    assert dut.log_out_q5_10.value == 1

@cocotb.test()
async def test_encryption_corner_9(dut):
    dut.fp16_in.value = 0x47E1
    await Timer(5, unit="ns")
    assert dut.log_out_q5_10.value == 3041





@cocotb.test()
async def test_encryption_corner_8(dut):
    dut.fp16_in.value = 0x45B2
    await Timer(5, unit="ns")
    assert dut.log_out_q5_10.value == 2482



@cocotb.test()
async def test_encryption_corner_7(dut):
    dut.fp16_in.value = 0x426A
    await Timer(5, unit="ns")
    assert dut.log_out_q5_10.value == 1642


#@cocotb.test()
#async def test_encryption_corner_6(dut):
#    dut.fp16_in.value = 0x41D3
#    await Timer(5, unit="ns")
#    assert dut.log_out_q5_10.value == 1235


#@cocotb.test()
#async def test_encryption_corner_5(dut):
#    dut.fp16_in.value = 0x4127
#    await Timer(5, unit="ns")
#    assert dut.log_out_q5_10.value == 1063


@cocotb.test()
async def test_encryption_corner_4(dut):
    dut.fp16_in.value = 0x43FF
    await Timer(5, unit="ns")
    assert dut.log_out_q5_10.value == 2047

@cocotb.test()
async def test_encryption_corner_3(dut):
    dut.fp16_in.value = 0x4001
    await Timer(5, unit="ns")
    assert dut.log_out_q5_10.value == 1025


@cocotb.test()
async def test_encryption_corner_2(dut):
    """Large exponent"""
    dut.fp16_in.value = 0x7800
    await Timer(5, unit="ns")
    assert dut.log_out_q5_10.value == 15360


#@cocotb.test()
#async def test_encryption_corner_1(dut):
#    """Smallest normalized value"""
#    dut.fp16_in.value = 0x0400
#    await Timer(5, unit="ns")
#    assert dut.log_out_q5_10.value == 54272








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
