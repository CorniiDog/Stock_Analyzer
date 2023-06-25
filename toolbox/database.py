import os, pickle, unicodedata, re
import datetime

storage_folder = os.path.join(os.path.dirname(__file__), 'database')
if not os.path.exists(storage_folder):
    os.makedirs(storage_folder)


def set_storage_path(path):
    """
    Parameters
    ----------
    path : str
        The path to the folder where the database files will be stored

    Returns
    -------
    None
        This function does not return anything

    Notes
    -----
    This function is used to set the path to the folder where the database files will be stored

    References
    ----------
    No Links

    Examples
    --------
    set_storage_path('C:/Users/JohnDoe/Documents/MyDatabase')
    """
    global storage_folder
    if not os.path.exists(storage_folder):
        # throw error
        raise Exception(f"Path {path} does not exist")

    storage_folder = path


def slugify(value, allow_unicode=False):
    """
    Parameters
    ----------
    value : str
        The string to be slugified
    allow_unicode : bool
        Whether or not to allow unicode characters

    Returns
    -------
    str
        The slugified string

    Notes
    -----
    This function is used to slugify strings, which basically means to remove all special characters and replace them with dashes.
    This is useful for creating file names from strings.

    References
    ----------
    https://github.com/django/django/blob/master/django/utils/text.py

    Examples
    --------
    a = slugify('Hello World')
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')


def get(name: str):
    """
    Parameters
    ----------
    name : str
        The name of the file to be loaded

    Returns
    -------
    object or None
        The object loaded from the file, could be anything

    Notes
    -----
    This function is used to load objects from the database folder

    References
    ----------
    No Links

    Examples
    --------
    spreadsheet_data = get('spreadsheet_people')
    """
    if name.endswith('.pkl'):
        name = name[:-4]
    path = os.path.join(storage_folder, name + '.pkl')

    if not os.path.exists(path):
        return None

    with open(path, 'rb') as f:
        return pickle.load(f)


def get_modified_date(name: str):
    """
    Parameters
    ----------
    name : str
        The name of the file to be loaded

    Returns
    -------
    datetime.datetime or None
        The datetime object of the last modified date

    Notes
    -----
    This function is used to get the last modified date of a file in the database folder

    References
    ----------
    No Links

    Examples
    --------
    date = get_modified_date('spreadsheet_people')

    """

    if name.endswith('.pkl'):
        name = name[:-4]
    path = os.path.join(storage_folder, name + '.pkl')
    if not os.path.exists(path):
        return None
    return datetime.datetime.fromtimestamp(os.path.getmtime(path))



def save(name: str, data: any) -> None:
    """
    Parameters
    ----------
    name : str
        The name of the file to be saved
    data : any
        The data to be saved

    Returns
    -------
    None
        This function does not return anything

    Notes
    -----
    This function is used to save objects to the database folder

    References
    ----------
    No Links

    Examples
    --------
    spreadsheet_data = {"People": ["Bill", "Kent", "Steve"], "Ages": [20, 30, 40]}

    save('spreadsheet_people', spreadsheet_data)
    """
    if name.endswith('.pkl'):
        name = name[:-4]
    path = os.path.join(storage_folder, name + '.pkl')
    with open(path, 'wb') as f:
        pickle.dump(data, f)


def delete_database(name: str) -> object:
    """
    Parameters
    ----------
    name : str
        The name of the file to be deleted

    Returns
    -------
    object or None
        The object loaded from the file, could be anything

    Notes
    -----
    This function is used to delete objects from the database folder

    References
    ----------
    No Links

    Examples
    --------
    spreadsheet_data = {"People": ["Bill", "Kent", "Steve"], "Ages": [20, 30, 40]}

    save('spreadsheet_people', spreadsheet_data)

    delete_database('spreadsheet_people')
    """

    if name.endswith('.pkl'):
        name = name[:-4]

    contents = get(name)
    path = os.path.join(storage_folder, name + '.pkl')
    os.remove(path)
    return contents


def save_key(platform: str, key: str, override: bool = False) -> None:
    """
    Parameters
    ----------
    platform: str
        The name of the platform to be saved (e.g. 'google')
    key: str
        The key to be saved (e.g. '<google_api_key>')
    override: bool
        Whether or not to override the key if it already exists

    Returns
    -------
    None
        This function does not return anything

    Notes
    -----
    This function is used to save keys in a secure location

    References
    ----------
    https://www.nylas.com/blog/making-use-of-environment-variables-in-python/

    Examples
    --------
    save_key('google', '<google_api_key>')
    """

    user_dir = os.path.expanduser('~')
    keys_dir = os.path.join(user_dir, '.keys')
    if not os.path.exists(keys_dir):
        os.makedirs(keys_dir)

    platform = slugify(platform)
    platform_file = os.path.join(keys_dir, f"{platform}.key")


    if not override:
        if os.path.exists(platform_file):
            raise Exception(f"Key for {platform} already exists. Use override=True to override the key.")

    with open(platform_file, 'w') as f:
        f.write(key)



def load_key(platform: str) -> str:
    """
        Parameters
        ----------
        platform: str
            The key to be loaded (e.g. '<google_api_key>')

        Returns
        -------
        str or None
            This function returns the key if it exists, otherwise it returns None

        Notes
        -----
        This function is used to load keys from a secure location

        References
        ----------
        https://www.nylas.com/blog/making-use-of-environment-variables-in-python/

        Examples
        --------
        key = load_key('google')
        """

    user_dir = os.path.expanduser('~')
    keys_dir = os.path.join(user_dir, '.keys')
    if not os.path.exists(keys_dir):
        os.makedirs(keys_dir)

    platform = slugify(platform)
    platform_file = os.path.join(keys_dir, f"{platform}.key")

    if not os.path.exists(platform_file):
        return "None"

    with open(platform_file, 'r') as f:
        return f.read()

