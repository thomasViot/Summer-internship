clc;
clear;
close all;
%% Parameters 

Fs = 33.3;            % Sampling frequency                    
Ts = 1/Fs;             % Sampling period       

%% Load data 

data1 = importdata('./specificData/data1.txt',';');
T_44_1 = data1.data(:,72); 
[T_reference_1,T_output_1,T_control1_1,T_control2_1] = changeDataSpecific(T_44_1,data1);

T_output_1 = T_output_1 - mean(T_output_1);
T_control1_1 = T_control1_1 - mean(T_control1_1);
T_control2_1 = T_control2_1 - mean(T_control2_1);

data2 = importdata("./specificData/data2.txt",';');
T_44_2 = data2.data(:,72);
[T_reference_2,T_output_2,T_control1_2,T_control2_2] = changeDataSpecific(T_44_2,data2);

T_output_2 = T_output_2 - mean(T_output_2);
T_control1_2 = T_control1_2 - mean(T_control1_2);
T_control2_2 = T_control2_2 - mean(T_control2_2);

%% Shrucked signal

samples = 34; % sample where to start to study 

T_output_1 = T_output_1(samples:end,1);
T_control1_1 = T_control1_1(samples:end);
T_control2_1 = T_control2_1(samples:end);

T_output_2 = T_output_2(samples:end);
T_control1_2 = T_control1_2(samples:end);
T_control2_2 = T_control2_2(samples:end);

%% detrend data

dataX = iddata(T_output_1, [T_control1_1, T_control2_1 ],Ts); %(output, inputs)
dataX = detrend(dataX); % pre-process

dataX2 = iddata(T_output_2, [T_control1_2, T_control2_2 ],Ts); %(output, inputs)
dataX2 = detrend(dataX2); % pre-process

%% ARX/ARXMAX MODELS

% ARX 

for i = 32:32
    na = i;
    for j=1:1
        nb = j*ones(2,1)'; 
        nk = zeros(2,1)'; 
        model = arx(dataX,[na nb nk]);
        figure(i),
        compare(dataX2, model);
        title('ARX')
    end

end


% ARMAX 

for i = 40:40
    nax = i;
    for j= 1:1
        nbx = j*ones(2,1)';
        for k = 1:1
            ncx =  k;
            nkx = zeros(2,1)'; 
            modelx = armax(dataX, [nax nbx ncx nkx] );
            figure(i),
            compare(dataX2, modelx);
            title("ARMAX")
        end
    end
end

figure,
pzmap(modelx);


%% plots

figure,
t = 0:Ts:length(T_output_1)/Fs-Ts;
figure(73),
plot(t, T_output_1)
title("output time domain shrucked")
xlabel("Time in s")
ylabel("Amplitude")
