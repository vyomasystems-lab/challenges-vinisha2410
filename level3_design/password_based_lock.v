module password_based_lock(access,alarm,inp,reset,clk);
parameter [3:0]pass = 1234;
output access,alarm;						
input [13:0]inp;
input reset;
input clk;
parameter idle=3'b000, wait_pass=3'b001, access_state=3'b010, denied=3'b011;
reg[2:0] current_state, next_state;
reg access,condition,alarm;							
integer count;
  

  
initial 
begin
	count = 0;
	access = 0;					
	alarm = 0;  
    current_state=idle;
end
  always @(posedge clk or  posedge reset)
begin
  if(reset) 
    begin
     current_state<=idle;
    end
  else
    begin
     current_state<=next_state;
    end
end
 
    
  always @(*)
begin
  case(current_state)   
       idle: 
        begin
            alarm=0;
            count=0;
            access=0;
            next_state=wait_pass;
        end
       wait_pass:
        begin
            access<=0;
            if(inp==pass)
               next_state=access_state;
            else 
               next_state=denied;
              
        end
       access_state: 
        begin
            access<=1;
            alarm<=0;
            count<=0;
            next_state=wait_pass;
        end
       denied: 
        begin
            count=count+1;
            if(count<3)
               next_state=wait_pass;
          else if (count>=3)
               
            next_state=wait_pass;
        end
  endcase
end

endmodule