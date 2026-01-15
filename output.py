import pandas as pd
from transformation import process_file

# processing the src files
acme_df = process_file("acme.txt", "ACME")
bettercare_df = process_file("bettercare.csv", "BETTERCARE")

# concatinating the output
final_df = pd.concat([acme_df, bettercare_df], ignore_index=True)

print(final_df)

# Saving the output to csv
final_df.to_csv("Merged_data_output.csv", index = False)