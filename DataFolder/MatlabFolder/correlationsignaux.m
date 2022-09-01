clc;
clear;
close all;

%% Parameters and loading
Ts = 0.03;


data1 = importdata('./specificData/data1.txt',';');
T_44_1 = data1.data(:,72); 
[T_reference_1,T_output_1,T_control1_1,T_control2_1] = changeDataSpecific(T_44_1,data1);


%% Testing cross correlation

corr1 = xcorr(T_output_1, T_control1_1, 'normalized');
corr2 = xcorr(T_output_1,T_control2_1, 'normalized');


figure,
plot(corr1) %open
title("correlation between output and control1 (open)")
figure,
plot(corr2) % close
title("correlation between output and control2 (close)")


figure,
plot(T_output_1)
hold on,
plot(T_control1_1/30 +100)
title('output and control1 (open)')
hold off,

figure,
plot(T_output_1)
hold on,
plot(T_control2_1/30 +100)
title('output and control2 (close)')
hold off,


figure,
plot(T_output_1)
hold on,
plot(T_control1_1/30 +100)
plot(T_control2_1/30 +100)
title('output, control1 and control2')

