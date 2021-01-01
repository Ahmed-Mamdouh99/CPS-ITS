clear % Clear current workspace

% Hybrid blocks parameters
T = 10; % Continuous horizon
J = 100; % Discrete horizon

x0ADC = [0 0]; % ADC initial state
Ts = 0.1; % ADC sampling rate

x0NET = [0 0]; % Network initial state
Tnmax = 1; % Network min time for event
Tnmin = 0.5; % Network max time for event

x0PLANT = [0 0 0]; % Plant initial state
minU = 0;
maxX = 10;
maxU = 10;

% Set hybrid equation rule
rule =  1;

% Create model
[status, ~] = system('python python_scripts/create_model1.py');
if status == 0
    % Define network model
    load('data/MODEL1.mat') % The file should contian structural information
else
    error('Could not create model data.');
end

% Start control sub process
[control_socket] = start_control('localhost', 5000, EDGES);

% Simulation parameters
emm_decay = .5; % The decay rate of emmission at a node
emm_threshold = 500; % Emmission threshold for nodes
