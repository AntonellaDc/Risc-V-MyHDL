from myhdl import *

# ############### #
# ALU Operations  #
# ############### #
class ALUOp:
    ALU_NONE              = int('0000',2)
    ALU_SHIFTL            = int('0001',2)
    ALU_SHIFTR            = int('0010',2)
    ALU_SHIFTR_ARITH      = int('0011',2)
    ALU_ADD               = int('0100',2)
    ALU_SUB               = int('0110',2)
    ALU_AND               = int('0111',2)
    ALU_OR                = int('1000',2)
    ALU_XOR               = int('1001',2)
    ALU_LESS_THAN         = int('1010',2)
    ALU_LESS_THAN_SIGNED  = int('1011',2)

# ###################### #
#  Modelo ALU riscv      #
# ###################### #


class ALUPortIO:
    def __init__(self):
        self.alu_a_i   = Signal(modbv(0)[32:])
        self.alu_b_i   = Signal(modbv(0)[32:])
        self.alu_op_i  = Signal(modbv(0)[4:])
        self.alu_p_o   = Signal(modbv(0)[32:])
        
@block
def riscv_alu ( io_iface ):

    sub_res_w = Signal(modbv(0)[32:])
    
    @always_comb
    def logic():

        # Desplazamiento a la izquierda
        if   ( io_iface.alu_op_i == ALUOp.ALU_SHIFTL ):
            io_iface.alu_p_o.next = io_iface.alu_a_i << io_iface.alu_b_i[5:0]
        # Desplazamiento a la derecha
        elif  (io_iface.alu_op_i == ALUOp.ALU_SHIFTR):
            io_iface.alu_p_o.next = io_iface.alu_a_i >> io_iface.alu_b_i[5:0]
        elif  (io_iface.alu_op_i == ALUOp.ALU_SHIFTR_ARITH):
            io_iface.alu_p_o.next = io_iface.alu_a_i.signed() >> io_iface.alu_b_i[5:0]
        # Suma
        elif ( io_iface.alu_op_i == ALUOp.ALU_ADD ):
            io_iface.alu_p_o.next = io_iface.alu_a_i + io_iface.alu_b_i
        # Resta
        elif ( io_iface.alu_op_i == ALUOp.ALU_SUB ):
            io_iface.alu_p_o.next = io_iface.alu_a_i - io_iface.alu_b_i
        # And
        elif ( io_iface.alu_op_i == ALUOp.ALU_AND ):
            io_iface.alu_p_o.next = (io_iface.alu_a_i & io_iface.alu_b_i)
        # Or
        elif ( io_iface.alu_op_i == ALUOp.ALU_OR ):
            io_iface.alu_p_o.next = (io_iface.alu_a_i | io_iface.alu_b_i)
        # XOR
        elif ( io_iface.alu_op_i == ALUOp.ALU_XOR ):
            io_iface.alu_p_o.next = (io_iface.alu_a_i ^ io_iface.alu_b_i)
        # Comparaciones
        elif ( io_iface.alu_op_i == ALUOp.ALU_LESS_THAN ):
            io_iface.alu_p_o.next  = concat(modbv(0)[31:], io_iface.alu_a_i < io_iface.alu_b_i )
        elif ( io_iface.alu_op_i == ALUOp.ALU_LESS_THAN_SIGNED ):
            io_iface.alu_p_o.next  = concat(modbv(0)[31:], io_iface.alu_a_i.signed() < io_iface.alu_b_i.signed())
        else:
            io_iface.alu_p_o.next = io_iface.alu_a_i

    return logic

        
                
        
