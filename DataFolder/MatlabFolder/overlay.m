function[] = overlay(dataList, index, Ts, Fs, titleGraph, name, from, to)
%overlay permits to overlay graphs
%   titleGraph is the figure number, index is the row that you want to
%   display, Ts is the sample time, Fs is the frequency sample,
%   dataList is a struct with data.
    
    test = 1;
    figure(titleGraph),
    for j = 1:length(dataList)
        t = 0:Ts:length(dataList{1,j}.data(:,index))/Fs-Ts;
        hold on,
        plot(t,dataList{1,j}.data(:, index));
        
        space = {' '};
        title(strcat(name, space, "From", space, string(from), space, "To", space , string(to))),
        xlabel('Time'),
        ylabel('Amplitude')
           
        if test == 1
            legend('data1')
        end
        
        if j == length(dataList)
            hold off
        end
        test = 2;
    end
    
end

