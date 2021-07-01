"""Convert Census Tract excel spreadsheet to csv file."""

import xlrd
import csv
import os
import glob


def retrive_excel_file(filename=None):
    """Search for and retrieve excel file."""
    try:
        if filename is not None:
            print("Locating excel file {}...".format(filename))
            excel_file = input_folder + filename
        else:
            print("Locating most recent excel file in this directory...")
            files = glob.glob(input_folder + "/*.xls")
            excel_file = max(files)
        print("File located {}".format(excel_file))
        return excel_file
    except Exception as error:
        print("Could not retrieve file. {}".format(error))

    


def convert_to_csv():
    """Take excel file and turn each sheet into a csv file."""

    print("Processing...")
    with xlrd.open_workbook(excel_file) as excel_workbook:
        for sheet_name in excel_workbook.sheet_names():
            excel_worksheet = excel_workbook.sheet_by_name(sheet_name)
            csv_filename = "est14us.csv" #"census" + sheet_name + ".csv"
            # csv_filename.replace("-", "_")
            csv_file = '../data/cleaned_csv/' + csv_filename
            with open(csv_file, 'w') as open_csv:
                write_to_csv = csv.writer(open_csv, quoting=csv.QUOTE_ALL)
                for rows in range(excel_worksheet.nrows):
                    write_to_csv.writerow(excel_worksheet.row_values(rows))
    print("A csv file was generated. Check input folder for results.")

# def main():

if __name__ == "__main__":
    # os.chdir("..")
    input_folder = "../data/"
    excel_file = retrive_excel_file(filename="est14us.xls")
    convert_to_csv()
