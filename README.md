# github_automation

The GitHubManager class allows you to automate basic GitHub tasks, like creating a pull request. This was written for the ConnectAutomation project. See the ConnectAutomation Docker container repo [here](https://github.com/linaro-marketing/connect_automation_container).

## Getting Started

Clone this repo and cd into the directory you've cloned it to. Setup a Python virtualenv using:

```bash
$ virtualenv -p python3 venv
$ source venv/bin/activate
```

Install the requirements:

```bash
$ pip install -r requirements.txt
```

Currently `pip` doesn't support freezing a module that has been installed from a GitHub repo. So if using the Linaro Vault, you will have to manually install the vault_auth module using:

```bash
$ pip install git+https://github.com/linaro-its/vault_auth.git
```

Modify the examples/test.py with your parameters:

```python3
ghm = GitHubManager(
            "https://github.com/linaro/connect", path_to_working_directory, app_directory, full_path_to_ssh_key, auth_token, github_reviewers)
```

Now run the example with:

```bash
python examples/test.py
```

For a more detailed example please the implementation in the ConnectAutomation container: [ConnectAutomation](https://github.com/linaro-marketing/connect_automation_container/blob/master/app/main.py).
