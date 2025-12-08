import pandas as pd

def export_orders_to_excel(dataframe, output_file):

#Export the order data to an Excel file with separate sheets for each DC.
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        # Group data by DistributionCenter and write each to a separate sheet
        for dc, group in dataframe.groupby('DistributionCenter'):
            group[['OrderID', 'DistributionCenter','StatusCode', 'OrderDate']].to_excel(writer, sheet_name=dc, index=False)
    print(f"Processed file saved as {output_file}")
