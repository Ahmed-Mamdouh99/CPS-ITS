function [arr_out] = arr_num2str(arr_in)
    arr_out = arrayfun(@(arr_in)num2str(arr_in),arr_in,'uni',0);
    arr_out = join(arr_out, ',');
end

