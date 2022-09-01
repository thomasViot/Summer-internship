function [T_reference,T_output,T_control1,T_control2] = changeDataSpecific(T_44, data)
%changeData tranforms data to get only what we need

T_reference = T_44.*data.data(:,1);
T_reference(T_reference == 0) = [];
T_reference(isnan(T_reference)) = [];

T_output = T_44.*data.data(:,2);
T_output(T_output == 0) = [];
T_output(isnan(T_output)) = [];

T_control1 = T_44.*data.data(:,54);
T_control1(T_control1 == 0) = [];
T_control1(isnan(T_control1)) = [];

T_control2 = T_44.*data.data(:,55);
T_control2(T_control2 == 0) = [];
T_control2(isnan(T_control2)) = [];
end

