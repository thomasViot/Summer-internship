function [output] = fromTo(from,to,namePath)
%fromTo Specifies which data to load.
    output = [];
    for i = from:to
        output = [output dir(strcat(namePath,'data',num2str(i),'.txt'))]; % select all txt files in the folder
    end
end

