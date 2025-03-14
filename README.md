# DEPEN-FIND - NPM Dependency Validator

DEPEN-FIND is a tool designed to validate NPM dependencies and check their availability in the NPM registry. This tool is specifically built to identify potential vulnerabilities related to **Dependency Confusion Attacks** by ensuring that all dependencies listed in a `package.json` or `package-lock.json` file is missing in the official NPM registry.

## Features
- Fetches dependency lists from a **GitHub URL** or a **local file**.
- Checks whether each dependency exists in the **NPM registry**.
- Displays results in a structured table format.
- Helps prevent **Dependency Confusion Attacks** by identifying missing dependencies.

## Installation
Ensure you have Python installed on your system, then clone the project and install the required dependencies:

```sh
git clone https://github.com/0xAkarii/depen-find
```
```sh
cd depen-find
```
```sh
pip install -r requirements.txt
```

## Usage
Run the script and provide a **GitHub URL** or a **file path** to `package.json` or `package-lock.json`:

```sh
python depen_find.py
```

Example input:

- **Using a GitHub URL:**
  ```
  Enter the URL or file path of package.json or package-lock.json: https://github.com/user/repo/blob/main/package.json
  ```
- **Using a local file:**
  ```
  Enter the URL or file path of package.json or package-lock.json: /path/to/package.json
  ```

## Contribution
Contributions are welcome! Feel free to open an issue or submit a pull request to improve the tool.

## License
This project is licensed under the **MIT License**.

## Author
Created by **@0xAkarii** (ChatGPT helped me to fix some codes)

🔗 **LinkedIn:** [Alva Radian](https://www.linkedin.com/in/alva-radian)  
☕ **Support Me:** [Buy Me a Coffee](https://buymeacoffee.com/0xakarii)

