function [v] = control_fsm_jump_set(last_state, beacons_reading, edges, thresh)

report = 0;

reduced = zeros(length(beacons_reading));

for i = 1:length(edges)
    [~, end_node] = edges(i);
    if last_state(i) == 0
        reduced(end_node) = 1;
    end
end

for i = 1:length(edges)
     [~, end_node] = edges(i);
     % Emission level is below threshold. Should re-enable edge
     if thresh > beacons_reading(end_node) && last_state(i) == 0
         report = 1;
         break;
     end
     % Emission level is bigger than or equal to threshold and access to
     % node is not reduced.
     if thresh <= beacons_reading(end_node) && reduced(end_node) == 0
         report = 1;
         break;
     end
end

v = report;

end

