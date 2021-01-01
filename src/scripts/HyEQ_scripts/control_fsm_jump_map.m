function v  = control_fsm_jump_map(last_state, beacons_reading, emm_edges, thresh, control_socket)
    % Convert list of numbers into a list of strings
    last_state_str = arr_num2str(last_state);
    beacons_reading_str = arr_num2str(beacons_reading);
    emm_edges_str = arr_num2str(emm_edges);
    thresh_str = num2str(thresh);
    command = ['solve' last_state_str beacons_reading_str emm_edges_str thresh_str];
    command = join(command, ' ');
    % Second command
    fwrite(control_socket, command);
    % Receive solution
    bytes = fread(t, [1,t.BytesAvailable]);
    % Decode byets
    msg = char(bytes);
    % Turn into number array
    v = arr_str2num(msg);
end