clear;
close all;
clc;

%% Parameters

Ts = 0.03;
Fs = 1/Ts;

%% loading data

from = 46;
to = 48;

name = ["Reference signal", "Output", "Control1", "Control2"];

globalFiles = fromTo(from,to,'globalData/');
specificFiles = fromTo(from,to,'specificData/');

dataList_g = Loading(globalFiles, './globalData/');
dataList2 = Loading(specificFiles, './specificData/');



%% Plot data 


overlay(dataList_g, 1, Ts, Fs, 1, "Global Graph 1", from, to); 
overlay(dataList_g, 2, Ts, Fs, 2, "Global Graph 2", from, to);
overlay(dataList_g, 3, Ts, Fs, 3,"Global Graph 3", from, to);

overlay(dataList2, 5, Ts, Fs, 7,name(1), from, to);
overlay(dataList2, 6, Ts, Fs, 8, name(2), from, to);
overlay(dataList2, 57, Ts, Fs, 9, name(3), from , to);
overlay(dataList2, 58, Ts, Fs, 10, name(4), from, to);

% looking at velocity signal and position signal

overlay(dataList2, 22, Ts, Fs, 15, "Position signal", from, to);
overlay(dataList2, 23, Ts, Fs, 16, "Velocity signal", from, to);



