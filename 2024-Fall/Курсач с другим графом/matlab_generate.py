def open_data():
    with open("data.txt", "r") as file:
        lines = file.readlines()
        data = tuple(line.replace(",", ".").split("\t")[1:] for line in lines)
        date = tuple(line.replace(":", "/").split("\t")[0] + "\n" for line in lines)
    file.close()

    return lines, data, date


def write_data(all_data: tuple, exception: str, file_path: str, data_idx: int):
    if data_idx != 0:
        data = all_data[data_idx]
        dt = []

        for elem in data:
            if exception not in elem:
                if data_idx == 1:
                    dt.append(",".join(elem))
                elif data_idx == 2:
                    dt.append(elem)

        with open(file_path, "w") as file:
            file.writelines(dt)
        file.close()
    else:
        data = all_data[data_idx]

        with open(file_path, "w") as file:
            file.writelines(data[0].replace("\t", ",")[10:-20])
        file.close()


def create_mlb_txt():
    data = open_data()
    write_data(data, "OutsideTemperature\n", "Matlab/data.txt", 1)
    write_data(data, "data time\n", "Matlab/date.txt", 2)
    write_data(data, "", "Matlab/height.txt", 0)
