import argparse
import get_data
import data_viz

def main():
    parser = argparse.ArgumentParser(
             description='from stdin use array to plot data: need col# and plot type',
             prog='input arg')

    parser.add_argument('--col_index', type=int, help='The column number')
    parser.add_argument('--out_file', type=str, help='filename for saving')
    parser.add_argument('--plot_type', type=str, help='histogram or boxplot or combo') 
    
    args = parser.parse_args()
    L = get_data.read_stdin_col(args.col_index)

    out_file_name = args.out_file
    if args.plot_type == 'boxplot':
        data_viz.boxplot(L,out_file_name,args.col_index)
    elif args.plot_type == 'hist':
        data_viz.histogram(L,out_file_name,args.col_index)
    elif args.plot_type == 'combo':
        data_viz.combo(L,out_file_name,args.col_index)
    else:
        print('input must be exactly: "boxplot", "hist", or "combo"')
    pass

if __name__ == '__main__':
    main()
