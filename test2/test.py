import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles

@cocotb.test()
async def test(dut):

    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    dut.reset.value = 1
    await ClockCycles(dut.clk, 2)
    dut.reset.value = 0

    for i in range(10):
        await ClockCycles(dut.clk, 1)
        dut._log.info("count is %d, %d", i, dut.count.value)
        assert dut.count.value == i
