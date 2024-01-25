import os
import gdown
import zipfile

def download_and_unzip(database_name):
    if database_name == 'D1':
        file_id = '1Dn5jv8PNX-NHKdkGJ9velyG_4AI--Cz9'
    elif database_name == 'D2':
        file_id = '16VDeLf5lXPz7qkhhddziXXJmjQ2Nyp22'
    else:
        raise RuntimeError("Database name is incorrect. It should be D1 or D2.")

    destination = '../data/'
    zip_path = os.path.join(destination, database_name + ".zip")
    output_folder = os.path.join(destination, database_name)

    if not os.path.exists(destination):
        os.makedirs(destination)

    # Check if the zip file is already downloaded
    if not os.path.exists(zip_path):
        gdown.download(f'https://drive.google.com/uc?id={file_id}', zip_path, quiet=False)

    # Check if the destination folder is already unzipped
    if not os.path.exists(output_folder):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(destination)
