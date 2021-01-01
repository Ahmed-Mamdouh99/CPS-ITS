function [arr_out] = arr_str2num(str_in)
    split_arr = split(str_in, ',');
    arr_out = arrayfun(@(a)str2double(a),split_arr);
end

