`default_nettype none
`timescale 1ns/1ns
module test (
    input wire clk,
    input wire reset,
    output reg [7:0] count
    );

    initial begin
        $dumpfile ("test.vcd");
        $dumpvars (0, test);
    end

    always @(posedge clk) begin
        if(reset)
            count <= 0;
        else
            count <= count + 1'b1;
    end

endmodule
