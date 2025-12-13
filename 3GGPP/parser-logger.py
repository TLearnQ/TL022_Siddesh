import os
import glob
import yaml
import json
import logging

class APIResponseError(Exception):
    pass

logging.basicConfig(
    filename='3gpps.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def analyze_apis():

    files = glob.glob("NETWORKING/Cloud-and-Devops-Associate/3GGPP/3gpp/*.yaml")[:5]
    summary = []

    stats = {
        "total_endpoints": 0,
        "methods": {},
        "auth_types": set(),
        "codes": {},
        "missing_responses": 0  
    }

    endpoints_with_responses = (
    stats["total_endpoints"] - stats["missing_responses"]
    )
    
    coverage_percentage = (
        (endpoints_with_responses / stats["total_endpoints"]) * 100
        if stats["total_endpoints"] else 0
    )

    stats["coverage_percentage"] = round(coverage_percentage, 2)

    for file_path in files:
        try:
            with open(file_path, 'r') as f:
                data = yaml.safe_load(f)

           
            info = data.get("info", {})
            title = info.get("title")
            description = info.get("description")
            version = info.get("version")

            
            if 'components' in data and 'securitySchemes' in data['components']:
                for scheme in data['components']['securitySchemes']:
                    stats["auth_types"].add(scheme)

            
            for path, methods in data.get('paths', {}).items():
                for method, details in methods.items():
                    if method.lower() not in ['get', 'post', 'put', 'delete', 'patch']:
                        continue

                    stats["total_endpoints"] += 1
                    stats["methods"][method.upper()] = stats["methods"].get(method.upper(), 0) + 1

                    responses = details.get('responses', {})
                    if not responses:
                        stats["missing_responses"] += 1

                    for code in responses:
                        stats["codes"][code] = stats["codes"].get(code, 0) + 1

                    summary.append({
                        "file": os.path.basename(file_path),
                        "api_title": title,
                        "api_version": version,
                        "api_description": description,
                        "endpoint": path,
                        "method": method.upper(),
                        "tags": details.get("tags", []),
                        "response_codes": list(responses.keys())
                    })

            logging.info(f"Successfully parsed {file_path}")

        except Exception as e:
            logging.error(f"Failed to parse {file_path}: {str(e)}")
            # raise APIResponseError(f"Critical failure on {file_path}")


    with open("summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    report = f"""
***** API SUMMARY REPORT ******
total Endpoints: {stats['total_endpoints']}
methods Used: {stats['methods']}
response codes lists: {stats['codes']}
auth Methods: {list(stats['auth_types'])}
endpoints missing response: {stats['missing_responses']}
coverage_percentage:{stats['coverage_percentage']}
"""

    print(report)
    with open("README.txt", "w") as f:
        f.write(report)

if __name__ == "__main__":
    analyze_apis()

