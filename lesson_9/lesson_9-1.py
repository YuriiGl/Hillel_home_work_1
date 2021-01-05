import csv
import argparse

def check_arguments(arguments):
    arg_dict = {'BRAND':arguments.brand, 'COLOR': arguments.color,
                'MAKE_YEAR': arguments.year, 'FUEL': arguments.fuel,
                'N_REG_NEW': arguments.reg_num}
    arg_dict = {key: value for key,
                value in arg_dict.items() if value is not None}
    if arg_dict:
        return arg_dict
    else:
        raise SystemExit('There are no optional arguments')

def read_from_csv(filename):
    with open(filename, 'r', encoding="utf-8") as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=';')
        result = []
        for row in csv_reader:
            if ('BRAND' not in args_dict or row['BRAND'] == args_dict['BRAND']) and \
                ('COLOR' not in args_dict or row['COLOR'] == args_dict['COLOR']) and \
                ('MAKE_YEAR' not in args_dict or row['MAKE_YEAR'] == args_dict['MAKE_YEAR']) and \
                ('FUEL' not in args_dict or row['FUEL'] == args_dict['FUEL']):
                result.append(row)
    return write_in_csv(result)

def write_in_csv(res):
    filename = '-'.join(args_dict.values()) + '.csv'
    with open(filename, 'w', encoding="utf-8") as csvresult:
        headers = ['D_REG', 'BRAND', 'MODEL', 'MAKE_YEAR', 'COLOR','FUEL', 'NEW_REG_NEW']
        csv_writer = csv.DictWriter = csv.DictWriter(csvresult, fieldnames=headers, extrasaction='ignore')
        csv_writer.writeheader()
        csv_writer.writerows(res)
        print('Writed into ',filename)

parser = argparse.ArgumentParser(description='Transport Registry')
parser.add_argument('filename', help='Enter the filename in csv format')
parser.add_argument('--brand', help='Enter the model make')
parser.add_argument('--color', help='Enter the model color')
parser.add_argument('--year', help='Enter the model year')
parser.add_argument('--fuel', help='Enter the fuel type')
parser.add_argument('--reg_num', help='Enter the license plate')
arguments = parser.parse_args()
args_dict = check_arguments(arguments)
read_from_csv(arguments.filename)