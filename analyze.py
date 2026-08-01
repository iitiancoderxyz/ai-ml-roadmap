import pandas as pd
def analyze_grades(filepath):
    df=pd.read_json(filepath, orient='index')
    print(df)
    for col in df.columns:
        avg=df[col].mean()
        print(f"Average grade of all students in {col} is {avg:.2f}")
