import requests, os

from bs4 import BeautifulSoup

# Configurables
DISPLAY_LENGTH     = 10
PROFILE_URL_PREFIX = 'https://my.pgp-hms.org/profile_public?hex='
GENOME_DIR_PATH    = 'resources/full_genome_data'


def main():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    valid_entries = []
    count         = 0

    for i in range(int(6190/DISPLAY_LENGTH)):
        print(f"{count} files validated ({int(count/6190)}%)")
        r = requests.get(
            url     = f'https://my.pgp-hms.org/users?sEcho=2&iColumns=8&sColumns=&iDisplayStart={i*10}&iDisplayLength={DISPLAY_LENGTH}&mDataProp_0=pgp_id&mDataProp_1=hex&mDataProp_2=enrolled&mDataProp_3=received_sample_materials&mDataProp_4=has_ccrs&mDataProp_5=has_relatives_enrolled&mDataProp_6=has_whole_genome_data&mDataProp_7=has_other_genetic_data&sSearch=&bRegex=false&sSearch_0=&bRegex_0=false&bSearchable_0=true&sSearch_1=&bRegex_1=false&bSearchable_1=true&sSearch_2=&bRegex_2=false&bSearchable_2=true&sSearch_3=&bRegex_3=false&bSearchable_3=true&sSearch_4=&bRegex_4=false&bSearchable_4=true&sSearch_5=&bRegex_5=false&bSearchable_5=true&sSearch_6=&bRegex_6=false&bSearchable_6=true&sSearch_7=&bRegex_7=false&bSearchable_7=true&iSortingCols=1&iSortCol_0=0&sSortDir_0=asc&bSortable_0=true&bSortable_1=true&bSortable_2=true&bSortable_3=true&bSortable_4=true&bSortable_5=true&bSortable_6=true&bSortable_7=true&_=1739673986470',
            headers = headers
            )
        
        data          = r.json().get("aaData")
        valid_entries.append(get_valid_entries(data))
        count += DISPLAY_LENGTH

    for ct, id in enumerate(valid_entries):
        download_data(id)
        print(f"{ct}/{len(valid_entries)} files downloaded ({int(ct/len(valid_entries))}%)")

# Data entries validated by having 1 or more complete genomes
def get_valid_entries(data: list) -> list:
    valid_entry_ids = []

    for entry in data:
        if entry['has_whole_genome_data'] != 0:
            valid_entry_ids.append(entry['hex'])

    return valid_entry_ids


def download_data(id: str) -> None:
    r = requests.get(PROFILE_URL_PREFIX + id)
    soup = BeautifulSoup(r.text)

    hyperlinks = soup.find_all('a', href=True)
    for link in hyperlinks:
        if 'genome_download' in link.get('href'):
            os.system(f'wget "{link.get("href")}" -P "{GENOME_DIR_PATH}"')


if __name__ == '__main__':
    main()