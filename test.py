import json
import requests
from tabulate import tabulate
from colorama import Fore, Style, init

# Initialize Colorama
init()

def print_banner():
    banner = f"""
{Fore.CYAN}██████╗ ███████╗██████╗ ███████╗███╗   ██╗    ███████╗██╗███╗   ██╗██████╗ {Style.RESET_ALL}
{Fore.CYAN}██╔══██╗██╔════╝██╔══██╗██╔════╝████╗  ██║    ██╔════╝██║████╗  ██║██╔══██╗{Style.RESET_ALL}
{Fore.CYAN}██║  ██║█████╗  ██████╔╝█████╗  ██╔██╗ ██║    █████╗  ██║██╔██╗ ██║██║  ██║{Style.RESET_ALL}
{Fore.CYAN}██║  ██║██╔══╝  ██╔═══╝ ██╔══╝  ██║╚██╗██║    ██╔══╝  ██║██║╚██╗██║██║  ██║{Style.RESET_ALL}
{Fore.CYAN}██████╔╝███████╗██║     ███████ ██║ ╚████║    ██║     ██║██║ ╚████║██████╔╝{Style.RESET_ALL}
{Fore.CYAN}╚═════╝ ╚══════╝╚═╝     ╚══════╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ {Style.RESET_ALL}

                {Fore.CYAN}DEPEN-FIND v1.0 - NPM Dependency Validator{Style.RESET_ALL} - {Fore.RED}by @0xAkarii{Style.RESET_ALL}
    """
    print(banner)

def fetch_json(input_source):
    if input_source.startswith("http"):
        try:
            print(f"📡 Fetching JSON from {input_source}...")
            raw_url = input_source.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
            response = requests.get(raw_url)
            if response.status_code == 200:
                print("✅ Successfully fetched JSON!")
                return response.text
            else:
                print("❌ Failed to fetch JSON! Ensure the URL is correct.")
        except Exception as e:
            print(f"❌ An error occurred: {e}")
    else:
        try:
            print(f"📂 Loading JSON from {input_source}...")
            with open(input_source, "r", encoding="utf-8") as file:
                return file.read()
        except Exception as e:
            print(f"❌ Error loading file: {e}")
    return None

def extract_dependencies(json_raw):
    try:
        data = json.loads(json_raw)
        return data.get("dependencies", {})
    except json.JSONDecodeError:
        print("⚠️ Invalid JSON input")
        return {}

def validate_npm_registry(dependencies):
    results = []
    print("🔍 Checking packages in the NPM registry...")
    
    for package_name in dependencies:
        url = f"https://registry.npmjs.org/{package_name}"
        print(f"🔄 Checking {package_name}...")
        response = requests.get(url)
        
        if response.status_code == 200:
            size = len(response.content)
            print(f"✅ {package_name} found ({size} bytes)")
            results.append([package_name, f"{Fore.GREEN}✅ AVAILABLE{Style.RESET_ALL}", f"{size} bytes"])
        else:
            print(f"❌ {package_name} not found in the NPM registry")
            results.append([package_name, f"{Fore.RED}❌ NOT FOUND{Style.RESET_ALL}", "-"])
    
    return tabulate(results, headers=["Package", "Status", "Size"], tablefmt="fancy_grid")

if __name__ == "__main__":
    print_banner()
    input_source = input("Enter the URL or file path of package.json or package-lock.json: ")
    json_raw = fetch_json(input_source)
    
    if json_raw:
        dependencies = extract_dependencies(json_raw)
        
        if dependencies:
            result = validate_npm_registry(dependencies)
            print(result)
        else:
            print("⚠️ No dependencies found.")
    else:
        print("⚠️ Failed to load JSON file. Check the entered source.")
