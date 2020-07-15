import sys
sys.path
sys.path.append('../sim/')
from riscv_alu import riscv_alu
from riscv_alu import ALUOp
from riscv_alu import ALUPortIO
import random
from myhdl import *

@block
def _testbench():
    """
    Testbech para ALU
    """
    clk = Signal(False)
    rst = Signal(True)
    aluIO = ALUPortIO()
    dut = riscv_alu(io_iface=aluIO)

    halfperiod = delay(5)

    @always(halfperiod)
    def clk_drive():
        clk.next = not clk

    @instance
    def stimulus():
        yield delay(5)
        rst.next = 0

        # Execute 1000 tests.
        for j in range(1000):
            aluIO.alu_a_i.next = random.randrange(0, 2**32)
            aluIO.alu_b_i.next = random.randrange(0, 2**32)
            a = aluIO.alu_a_i
            b = aluIO.alu_b_i

            # Test each function
            for i in range(1,16):
                aluIO.alu_op_i.next = i
                yield delay(1)
                shamt = aluIO.alu_b_i[5:0]

                if i == ALUOp.ALU_ADD:
                    assert aluIO.alu_p_o == modbv(a + b)[32:], "Error ADD"
                elif i == ALUOp.ALU_SHIFTL:
                    assert aluIO.alu_p_o == modbv(a << shamt)[32:], "Error SLL"
                elif i == ALUOp.ALU_XOR:
                    assert aluIO.alu_p_o == a ^ b, "Error XOR"
                elif i == ALUOp.ALU_SHIFTR:
                    assert aluIO.alu_p_o == a >> shamt, "Error SRL"
                elif i == ALUOp.ALU_OR:
                    assert aluIO.alu_p_o == a | b, "Error OR"
                elif i == ALUOp.ALU_AND:
                    assert aluIO.alu_p_o == a & b, "Error AND"
                elif i == ALUOp.ALU_SUB:
                    assert aluIO.alu_p_o == modbv(a - b)[32:], "Error SUB"
                elif i == ALUOp.ALU_SHIFTR_ARITH:
                    assert aluIO.alu_p_o == modbv(a.signed() >> shamt)[32:], "Error SRA"
                elif i == ALUOp.ALU_LESS_THAN_SIGNED:
                    assert aluIO.alu_p_o == modbv(a.signed() < b.signed())[32:], "Error SLT"
                elif i == ALUOp.ALU_LESS_THAN:
                    assert aluIO.alu_p_o == modbv(abs(a) < b)[32:], "Error SLTU"
                elif i==ALUOp.ALU_NONE:
                    assert aluIO.alu_p_o == a, "Error UNDEFINED OP"

        raise StopSimulation

    return instances()


if __name__ == "__main__":
    testbench = _testbench()
    testbench.config_sim(trace=True)
    testbench.run_sim(2000)
