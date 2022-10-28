from pref_read_votes_2 import csv_file_reader, get_table_counts
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
matplotlib.use('TkAgg')

def create_graph(table):
    columns = table.pop(0)[1:]
    print(columns)
    rows = []
    data = []
    for row in table:
        rows.append(row.pop(0))
        data.append(row)
    print(rows)
    for x in data:
        print(x)

    plt.figure(figsize=(10, 10))
    # y ticks
    values = np.arange(0,150,25)
    print(values)
    value_increment = 1

    colors = plt.cm.BuPu(np.linspace(0, 1, len(rows)))
    n_rows = len(data)
    for c in colors:
        for i in range(0, len(c)):
            c[i] = random.random()
        print(c)


    index = np.arange(len(columns))+0.3
    print(index)

    bar_width = 0.4

    y_offset = np.zeros(len(columns))
    print(y_offset)

    cell_text = []
    for row in range(n_rows):
        plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
        y_offset = y_offset + data[row]
        cell_text.append([x for x in data[row]])

    # Reverse colors and text labels to display the last value at the top.
    #colors = colors[::-1]
    #cell_text.reverse()

    # Add a table at the bottom of the axes
    the_table = plt.table(cellText=cell_text,
                          rowLabels=rows,
                          rowColours=colors,
                          colLabels=columns,
                          loc='bottom')
    # Adjust layout to make room for the table:
    plt.subplots_adjust(left=0.2, bottom=0.4)
    the_table.scale(1, 2)

    plt.ylabel("Loss in ${0}'s".format(value_increment))
    plt.yticks(values * value_increment, ['%d' % val for val in values])
    plt.xticks([])
    plt.title('Loss by Disaster')

    plt.savefig('pyplot-table-tighten-figsize.png',
                # bbox_inches='tight',
                #edgecolor=fig.get_edgecolor(),
               # facecolor=fig.get_facecolor(),
                dpi=150
                )
    fig = plt.gcf()
    plt.savefig('pyplot-table-original.png',
                bbox_inches='tight',
                dpi=150
                )

    plt.show()

    return None


if __name__ == "__main__":
    read_file = "set_150_votes_8_candidates_biased.csv"
    collected_votes, bin_base = csv_file_reader(read_file)
    table = get_table_counts(collected_votes)
    create_graph(table)
