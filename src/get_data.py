import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("SPACETRACK_USERNAME")
PASSWORD = os.getenv("SPACETRACK_PASSWORD")

if not USERNAME or not PASSWORD:
    raise ValueError("Space-Track credentials not found")

ST_LOGIN_URL = "https://www.space-track.org/ajaxauth/login"
ST_QUERY_SATELLITES = "https://www.space-track.org/basicspacedata/query/class/satcat/OBJECT_TYPE/PAYLOAD/format/json"
CT_URL = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=csv"

OUTPUT = "../data/raw/satellites.csv"


def space_track_login(query_url):
    with requests.Session() as session:
        login_data = {"identity": USERNAME, "password": PASSWORD}
        response = session.post(ST_LOGIN_URL, data=login_data)

        if response.status_code != 200:
            raise RuntimeError(f"Login failed ({response.status_code})")

        data_response = session.get(query_url)

        if data_response.status_code != 200:
            raise RuntimeError(f"Data request failed ({data_response.status_code})")

        return data_response.json()


def extract_data():
    data_st = space_track_login(ST_QUERY_SATELLITES)
    df_st = pd.DataFrame(data_st)

    df_ct = pd.read_csv(CT_URL)

    return df_st, df_ct


def transform_data(df_st, df_ct):
    df_ct["ACTIVE"] = "Yes"

    df_st["NORAD_CAT_ID"] = df_st["NORAD_CAT_ID"].astype(int)
    df_ct["NORAD_CAT_ID"] = df_ct["NORAD_CAT_ID"].astype(int)

    df_merge = df_st.merge(df_ct[["NORAD_CAT_ID", "ACTIVE"]], on="NORAD_CAT_ID", how="left")

    df_merge["ACTIVE"] = df_merge["ACTIVE"].fillna("No")

    return df_merge


def load_data(df):
    df.to_csv(OUTPUT, index=False)


def main():
    df_st, df_ct = extract_data()
    df_merge = transform_data(df_st, df_ct)
    load_data(df_merge)


if __name__ == "__main__":
    main()