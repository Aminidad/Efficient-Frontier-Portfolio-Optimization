import csv
import pandas as pd


def file_format_fixer(nested_list):
    fixed_file = []
    for i in nested_list:
        fixed_file.append([int(i[1]), i[0], float(i[5])])
    return fixed_file


# --------- DONE
def date_selector(stock_list, start_date, end_date):
    new_list = []
    for item in stock_list:
        if item[0] != "<TICKER>" and end_date >= int(item[1]) >= start_date:
            new_list.append(item)
    return new_list


# --------- DONE
def close_price_checker(stock_list):
    fixed_list = [x for x, y in zip(stock_list, stock_list[1:]) if
                  not (float(x[5]) / float(y[5])) - 1 > 0.05 and
                  not (float(x[5]) / float(y[5])) - 1 < -0.05]
    # -------------------------------------------------------------
    # The loop automatically drops the first day value of the stock
    # Needs fix ?
    # -------------------------------------------------------------
    return fixed_list


# --------- DONE
def shared_dates(stock_list):
    def to_set(a_list):
        return {b for _, b, _, _, _, _, _, _, _, _, _, _ in a_list}

    intersection = to_set(stock_list[0])
    for a_set in (to_set(a_list) for a_list in stock_list[1:]):
        intersection = intersection & a_set

    flattened_lists = (item for a_list in stock_list for item in a_list)
    results = [item for item in flattened_lists if item[1] in intersection]

    return results


# --------- DONE
def get_table(selected, start_date, end_date, pd_friendly=True):
    final_list = []
    for fileName in selected:
        csv_file = open("data_csv//" + fileName + ".csv")
        csv_reader = csv.reader(csv_file)
        csv_list = [_ for _ in csv_reader]
        final_list_items = close_price_checker(date_selector(csv_list, start_date, end_date))
        final_list.append(final_list_items)
    if pd_friendly:
        return file_format_fixer(shared_dates(final_list))
    if not pd_friendly:
        return shared_dates(final_list)
