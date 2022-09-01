function [dataList] = Loading(file, namePath)
%Load data 

    dataList = {};

    for j=1:length(file)
        dataList{j} = importdata(strcat(namePath,file(j).name),';'); 
    end

end

