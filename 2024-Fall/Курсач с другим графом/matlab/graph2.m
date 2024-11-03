data = importdata('data.txt');
date = importdata('date.txt');
height = importdata('height.txt');

input_date = input('Введите дату(DD/MM/YYYY): ', 's');
input_date_dt = datetime(input_date, 'InputFormat', 'dd/MM/yyyy');
date_dt = datetime(date, 'InputFormat', 'dd/MM/yyyy HH/mm/ss'); % Исправлено на HH:mm:ss
test = hours(input_date_dt - date_dt) == 0 & minutes(input_date_dt - date_dt) == 0 & seconds(input_date_dt - date_dt) == 0;
idx = find(test, 1);
nums = data(idx:idx+287, 1:21);
[height_mesh, date_mesh] = meshgrid(height(1, 1:21), date(idx:idx+287));

% Получение размеров матрицы
[rows, cols] = size(date_mesh);

% Инициализация новой матрицы для хранения первых двух букв
date_epta = zeros(rows, cols);

% Перебор матрицы
for i = 1:rows
    for j = 1:cols
        part0 = date_mesh{i, j}(1:11);
        part1 = date_mesh{i, j}(12:13);
        part2 = date_mesh{i, j}(15:16);
        part3 = date_mesh{i, j}(18:19);
        date_timess = [part0, part1, ':', part2, ':', part3];
        % Преобразование строки в datetime
        date_time = datetime(date_timess, 'InputFormat', 'dd/MM/yyyy HH:mm:ss');
        
        % Преобразование datetime в числовой формат
        date_epta(i, j) = datenum(date_time);
    end
end


% date_epta = repmat(date_epta(:, 1), 1, 288);
% height_mesh = repmat(height_mesh(1, :), 288, 1);
% height_mesh = height_mesh';

nums2 = zeros(288, 288);
nums2(:, 1:21) = nums;
height_mesh2 = zeros(288, 288);
height_mesh2(:, 1:21) = height_mesh;
date_epta2 = zeros(288, 288);
date_epta2(:, 1:21) = date_epta;


figure;
contourf(date_epta, height_mesh, nums);
colormap(jet); % Установка цветовой карты
colorbar; % Добавление цветовой шкалы

% Настройка графика
ylabel('Height');
xlabel('Date');
title(date_mesh{i, j}(1:11));

chisto_chasici_matrixca = date_epta(1:12:end,1);
xticks(date_epta(1:12:end,1)); % Установка значений на оси X
xticklabels(datestr(chisto_chasici_matrixca, 'hh:MM')); % Форматирование меток на оси X
xtickangle(45);

yticks(0:50:max(height)); % Замените max(height) на максимальное значение высоты
