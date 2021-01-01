function [arr_out] = arr_2d_num2str(arr_in)
arr_out = {};
for i = 1:length(arr_in)
  arr_out{i} = [ num2str(arr_in(i,1)) ',' num2str(arr_in(i,2)) ];
end
  arr_out = join(arr_out, ' ');
end

