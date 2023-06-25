[Back to DOCS.md](DOCS.md)

Import Statement: `from toolbox import database`

Alternative Import Statement: `from toolbox.database import *`

# >  function set_storage_path #

### [def set_storage_path(path):](./../toolbox/database.py#L9) 

Note

```python
    This function is used to set the path to the folder where the database files will be stored
```

Param

```python
ters
    ----------
    path : str
        The path to the folder where the database files will be stored
```

Return

```python
    None
        This function does not return anything
```

Example

```python
    set_storage_path('C:/Users/JohnDoe/Documents/MyDatabase')
```

Reference

```python
    No Links
```

# >  function slugify #

### [def slugify(value, allow_unicode=False):](./../toolbox/database.py#L41) 

Note

```python
    This function is used to slugify strings, which basically means to remove all special characters and replace them with dashes.
    This is useful for creating file names from strings.
```

Param

```python
ters
    ----------
    value : str
        The string to be slugified
    allow_unicode : bool
        Whether or not to allow unicode characters
```

Return

```python
    str
        The slugified string
```

Example

```python
    a = slugify('Hello World')
```

Reference

```python
    https://github.com/django/django/blob/master/django/utils/text.py
```

# >  function get #

### [def get(name: str):](./../toolbox/database.py#L77) 

Note

```python
    This function is used to load objects from the database folder
```

Param

```python
ters
    ----------
    name : str
        The name of the file to be loaded
```

Return

```python
    object or None
        The object loaded from the file, could be anything
```

Example

```python
    spreadsheet_data = get('spreadsheet_people')
```

Reference

```python
    No Links
```

# >  function get_modified_date #

### [def get_modified_date(name: str):](./../toolbox/database.py#L112) 

Note

```python
    This function is used to get the last modified date of a file in the database folder
```

Param

```python
ters
    ----------
    name : str
        The name of the file to be loaded
```

Return

```python
    datetime.datetime or None
        The datetime object of the last modified date
```

Example

```python
    date = get_modified_date('spreadsheet_people')
```

Reference

```python
    No Links
```

# >  function save #

### [def save(name: str, data: any) -> None:](./../toolbox/database.py#L147) 

Note

```python
    This function is used to save objects to the database folder
```

Param

```python
ters
    ----------
    name : str
        The name of the file to be saved
    data : any
        The data to be saved
```

Return

```python
    None
        This function does not return anything
```

Example

```python
    spreadsheet_data = {"People": ["Bill", "Kent", "Steve"], "Ages": [20, 30, 40]}

    save('spreadsheet_people', spreadsheet_data)
```

Reference

```python
    No Links
```

# >  function delete_database #

### [def delete_database(name: str) -> object:](./../toolbox/database.py#L182) 

Note

```python
    This function is used to delete objects from the database folder
```

Param

```python
ters
    ----------
    name : str
        The name of the file to be deleted
```

Return

```python
    object or None
        The object loaded from the file, could be anything
```

Example

```python
    spreadsheet_data = {"People": ["Bill", "Kent", "Steve"], "Ages": [20, 30, 40]}

    save('spreadsheet_people', spreadsheet_data)

    delete_database('spreadsheet_people')
```

Reference

```python
    No Links
```

# >  function save_key #

### [def save_key(platform: str, key: str, override: bool = False) -> None:](./../toolbox/database.py#L220) 

Note

```python
    This function is used to save keys in a secure location
```

Param

```python
ters
    ----------
    platform: str
        The name of the platform to be saved (e.g. 'google')
    key: str
        The key to be saved (e.g. '<google_api_key>')
    override: bool
        Whether or not to override the key if it already exists
```

Return

```python
    None
        This function does not return anything
```

Example

```python
    save_key('google', '<google_api_key>')
```

Reference

```python
    https://www.nylas.com/blog/making-use-of-environment-variables-in-python/
```

# >  function load_key #

### [def load_key(platform: str) -> str:](./../toolbox/database.py#L267) 

Note

```python
        This function is used to load keys from a secure location
```

Param

```python
ters
        ----------
        platform: str
            The key to be loaded (e.g. '<google_api_key>')
```

Return

```python
        str or None
            This function returns the key if it exists, otherwise it returns None
```

Example

```python
        key = load_key('google')
```

Reference

```python
        https://www.nylas.com/blog/making-use-of-environment-variables-in-python/
```

