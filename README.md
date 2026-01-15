# Healthcare_Eligibility_Pipeline

This project builds a configuration-driven data pipeline that ingests healthcare eligibility files from multiple partners. Since each partner sends data in a different format, the pipeline standardizes all incoming data into a single, unified structure that can be easily used by downstream systems.

## Project Structure

```text
Healthcare_Eligibility_Pipeline/
│
├── acme.txt                  # Acme Health source file
├── bettercare.csv            # Better Care source file
├── config.py                 # Partner configuration definitions
├── transformation.py         # Core ingestion & transformation logic
├── output.py                 # Pipeline entry point
├── Merged_data_output.csv    # Final unified output
└── README.md                 # Project documentation

```md
## To Run the Pipeline
Make sure Python 3 and the pandas library are installed.
Place the partner input files (acme.txt, bettercare.csv) in the project directory.
Run the pipeline using the command below:
python output.py
The pipeline will generate a unified output file named Merged_data_output.csv.

##Adding a New Partner
Add a new entry to PARTNER_CONFIG inside config.py.
Define the following for the new partner:
File delimiter
Column mappings
Date format
Partner code
Place the new input file in the project directory.
Call process_file() with the new partner key.
No changes to the transformation or orchestration code are required.


Or make
