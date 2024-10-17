
data = importdata('data.txt');
date = importdata('date.txt');
height = importdata('height.txt');

try
    input_date = input('Введите дату(DD/MM/YYYY HH:MM:SS): ', 's');
    input_date_dt = datetime(input_date, 'InputFormat', 'dd/MM/yyyy HH:mm:ss');
    date_dt = datetime(date, 'InputFormat', 'dd/MM/yyyy HH/mm/ss');

    test = hours(input_date_dt - date_dt) == 0 & minutes(input_date_dt - date_dt) == 0 & seconds(input_date_dt - date_dt) == 0;
    idx = find(test, 1);

    if idx ~= 0
        nums = data(idx:idx, 1:21);

        plot(nums, height, 'DisplayName', 'Фактическая');
        hold on;

        y = [1000, 0];
        x = [nums(1,1)-20, nums(1,1)];

        plot(x, y, 'DisplayName', 'Теоритическая');
        lgd = legend;
        lgd.FontSize = 14;
        lgd.Title.String = input_date;
    else
        disp('Неверно введена дата!');
    end
catch ERROR
    disp("Неправильный формат даты. Пожалуйста введите дату в формате 00/00/00 00:00:00")
end