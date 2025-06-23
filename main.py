import re, io, math
import pandas as pd

# raw data

data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'

df = pd.read_csv(io.StringIO(data), sep=';', lineterminator='\n')

# Airline Code
def clean_airline(name: str) -> str:
    txt = re.sub(r"[^A-Za-z ]+", "", name) # keep letters & spaces only
    txt = re.sub(r"\s+", " ", txt).strip() # collapse multiple spaces
    return txt.title()                     # Title-case each word

df["Airline Code"] = df["Airline Code"].astype(str).apply(clean_airline)

# FlightCodes
# Make numeric, then fill the gaps with + 10 steps, convert to int
codes = pd.to_numeric(df["FlightCodes"], errors="coerce")
for i in range(len(codes)):
    if pd.isna(codes.iloc[i]):
        codes.iloc[i] = codes.iloc[i-1] + 10
df["FlightCodes"] = codes.astype(int)

# To_From
df[["From", "To"]] = (
    df["To_From"]
        .str.split("_", expand=True)
        .apply(lambda s: s.str.title())         # capital case
)
df.drop(columns=["To_From"], inplace=True)

# print output
print(df.to_string(index=False))