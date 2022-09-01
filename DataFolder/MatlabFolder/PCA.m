clc;
clear;
close all;
%% loading data 
from = 1;
to = 48;

data = fromTo(from,to,'specificData/'); % change the folder here 
dataList = Loading(data, './specificData/');

%% Take V27 signals from each cycles.

indexV27 = 2; % index of the signal used. 
matrix = [];

for j=1:length(dataList)
    column = dataList{1,j}.data(:, indexV27);
    if length(column) ~= 1550 % adding 0 to have the same length
        while length(column) ~= 1550
            column = [column; 0];
        end
    end
    matrix = [matrix column];
end


%% Put here from which type the data used come from.

type = [];

for i=1:10
    type = [type "type1"];
end

for i=1:23
    type = [type "type2"];
end

for i=1:12
    type = [type "type3"];
end

for i=1:3
    type = [type 'failure'];
end


%% PCA

matrix = matrix';

type = type';
matrixString = [matrix type]; 


% centering the data
Xavg = mean(matrix,2);
B = Xavg*ones(1,length(column));
matrix2 = matrix - B;

covMatrix = matrix2'*matrix2;

[U,S,V] = svd(covMatrix/sqrt(length(column)), 'econ');


x1 = [];
x2 = [];
x3 = [];
x4 = [];

y1 = [];
y2 = [];
y3 = [];
y4 = [];


figure(1), hold on

for i=1:size(matrix,1)
    k = V(:,1)'*matrix(i,:)';
    l = V(:,2)'*matrix(i,:)';
    m = V(:,3)'*matrix(i,:)';
    if(matrixString(i,1551) == "type1")
        plot(k,l, 'bo')
        x1 = [x1 k];
        y1 = [y1 l];
    elseif(matrixString(i,1551) == "type2")
        plot(k,l, 'bo')
        x2 = [x2 k];
        y2 = [y2 l];
    elseif(matrixString(i,1551) == "type3")
        plot(k,l, 'bo')
        x3 = [x3 k];
        y3 = [y3 l];
    else
        plot(k,l, 'rx')
        x4 = [x4 k];
        y4 = [y4 l];
    end
end
title('Clusters')
xlabel('PC1'), ylabel('PC2'),  
grid on


figure(2),
Y = [];
for i=1:48
    Y = [Y S(i,i)];
end

semilogy(1:48,Y, 'x')
title("Eigenvalues on a semilog plot")

%% classification

meanx_type1 = mean(x1);
meany_type1 = mean(y1);
meanx_type2 = mean(x2);
meany_type2 = mean(y2);
meanx_type3 = mean(x3);
meany_type3 = mean(y3);
meanx_type4 = mean(x4);
meany_type4 = mean(y4);

testedSignal = dataList{1,48}.data(:, indexV27);

if length(testedSignal) ~= 1550 % adding 0 to have the same length
    while length(testedSignal) ~= 1550
        testedSignal = [testedSignal; 0];
    end
end

x_test = V(:,1)'*testedSignal;
y_test = V(:,2)'*testedSignal;

% compute the distance 
d1 = pdist([x_test,y_test; meanx_type1, meany_type1],'euclidean');
d2 = pdist([x_test,y_test; meanx_type2, meany_type2],'euclidean');
d3 = pdist([x_test, y_test; meanx_type3, meany_type3],'euclidean');
d4 = pdist([x_test, y_test; meanx_type4, meany_type4],'euclidean');

minimum = min([d1,d2,d3,d4]);

if(minimum == d1)
    disp('The tested signal is from type1')   
elseif(minimum == d2)
    disp('The tested signal is from type2')   
elseif(minimum == d3)
    disp('The tested signal is from type3') 
else
    disp('The tested signal is a failure one') 
end

hold off


figure(3), 
plot(meanx_type1, meany_type1, 'rx'),
hold on,
plot(meanx_type2, meany_type2, 'rx'),
plot(meanx_type3, meany_type3, 'rx'),
plot(meanx_type4, meany_type4, 'rx'),
plot(x_test, y_test, 'bO')
plot([x_test meanx_type1], [y_test meany_type1])
plot([x_test meanx_type2], [y_test meany_type2])
plot([x_test meanx_type3], [y_test meany_type3])
plot([x_test meanx_type4], [y_test meany_type4])


title("Distance between the tested signal and the means")
xlabel("PC1"), ylabel("PC2")







