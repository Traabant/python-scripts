import matplotlib.pyplot as plt
import numpy as np
import datetime


def main():
    with open("d:\\new.csv", encoding='UTF-8') as csv_file:
        lines_from_file = csv_file.readlines()
        # print(lines_from_file)
    run_id = 0

    loader_state_list_disabled = []
    loader_state_list_enabled = []

    for line in lines_from_file:

        current_info = {
            'loaderstate': "",
            'starttime': ""
        }
        loader_loc = line.find("LoaderState")
        if loader_loc != -1:
            current_info['loaderstate'] = line[loader_loc+12:loader_loc+13]
            if current_info['loaderstate'] == "-":
                current_info['loaderstate'] = line[loader_loc + 12:loader_loc + 14]

        starttime_loc = line.find("StartTime")
        if starttime_loc != -1:
            current_info['starttime'] = line[starttime_loc+10:starttime_loc+18]
            current_info['starttime'] = datetime.datetime.strptime(current_info['starttime'], '%H:%M:%S')
        run_id += 1

        if current_info['loaderstate'] == "1":
            loader_state_list_enabled.append(current_info)
        elif current_info['loaderstate'] == "-1":
            loader_state_list_disabled.append(current_info)

    # fig = plt.figure()
    # line = fig.add_subplot(1, 1, 1)
    # line.plot

    pass

    # loader_file = open("d:\\loader.csv", 'w', encoding='UTF-8')
    # loader_file.write(line_to_write)
    # loader_file.close()


if __name__ == '__main__':
    main()
