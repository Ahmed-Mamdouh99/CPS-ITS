function [t] = start_control(host, port, edges)

% Create command
command = ['python python_scripts/sub_process/control.py' ' --ip ' host ' --port ' int2str(port) ' &'];
% Start server
system(command);

% Start a socket
t = tcpip(host, port);
fopen(t);
% Send the edges structure

edges_str = arr_2d_num2str(edges);
fwrite(t, [ 'set-edges ' edges_str{1}]);

end