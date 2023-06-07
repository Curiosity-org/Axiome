import os
import yaml

def get_config(
        category: str,
        key: str,
        type = str,
        default=None,
    ):
    """Return the configuration variable contained in the optionnal category
    with the specified key and type.
    This function first check in the configuration file `config.yaml`, then
    in the environment variable and fallback to the specified default value.

    You can set the bridge up in two ways:

    With environment variables: `CATEGORY_KEY='your value'`
    With configuration file (`config.yaml`):
    ```
    category:
      key: 'value'
    ```
    """
    if os.path.exists('config.yaml'):
        with open('config.yaml', encoding='utf-8') as configuration_file:
            config = yaml.load(configuration_file, yaml.Loader)
    else:
        config = {}

    env_variable_name = category.upper() + '_' + key.upper()

    if category.lower() in config:
        if key.lower() in config[category.lower()]:
            return type(config[category.lower()][key.lower()])
    elif env_variable_name in os.environ:
        return type(os.environ[env_variable_name])
    else:
        return default
