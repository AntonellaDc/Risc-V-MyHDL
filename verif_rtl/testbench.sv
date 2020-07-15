// Testbench ALU RISCV
// make compile
// make view

module testbench;
   
   parameter NB_INPUT =  32;
   parameter NB_OUTPUT =  32;
   parameter NB_SELECTOR = 4;

   reg [NB_INPUT-1:0]    input_a,input_b;
   reg [NB_SELECTOR-1:0] selector;
   wire [NB_OUTPUT-1:0]  output_alu;

   // MyHDL Sentences
   initial 
     begin
        $from_myhdl(input_a,input_b,selector);
        $to_myhdl(output_alu);
     end

   initial
     begin
        $dumpfile("cosim.vcd");
        $dumpvars();
     end
   
   riscv_alu
     alu
     (
      .alu_op_i ( selector ),

      .alu_a_i ( input_a ),
      .alu_b_i ( input_b ),

      .alu_p_o ( output_alu )
      );

endmodule
