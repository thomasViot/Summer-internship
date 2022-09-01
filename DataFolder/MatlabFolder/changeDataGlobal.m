function [T_output_V27,T_output_V32,T_output_V6] = changeDataGlobal(T_44, data)
%changeData tranforms data to get only what we need

T_output_V27 = T_44.*data.data(:,2);
T_output_V27(T_output_V27 == 0) = [];
T_output_V27(isnan(T_output_V27)) = [];

T_output_V32 = T_44.*data.data(:,6);
T_output_V32(T_output_V32 == 0) = [];
T_output_V32(isnan(T_output_V32)) = [];

T_output_V6 = T_44.*data.data(:,18);
T_output_V6(T_output_V6 == 0) = [];
T_output_V6(isnan(T_output_V6)) = [];

end

