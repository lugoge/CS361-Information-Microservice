
import requests

class InformationClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_info(self, context):
        """Request help information from the microservice."""
        url = f"{self.base_url}/info/{context}"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                return response.json()

            elif response.status_code == 404:
                return {"error": "Context not found"}

            else:
                return {"error": f"Unexpected status code: {response.status_code}"}

        except requests.exceptions.ConnectionError:
            return {"error": "Unable to connect to microservice"}
        except Exception as e:
            return {"error": str(e)}

    def display_info(self, data):
        """Display formatted help information."""
        if "error" in data:
            print("\nERROR:", data["error"])
            return

        print("\n===================================")
        print(f" {data.get('title', 'No Title')}")
        print("===================================\n")

        if "purpose" in data:
            print("Purpose:")
            print(data["purpose"], "\n")

        if "steps" in data:
            print("Steps:")
            for i, step in enumerate(data["steps"], start=1):
                print(f"{i}. {step}")
            print()

        if "tips" in data:
            print("Tips:")
            for tip in data["tips"]:
                print(f"- {tip}")
            print()

        if "notes" in data:
            print("Notes:")
            print(data["notes"], "\n")


def main():
    client = InformationClient("http://localhost:5004")

    print("=== Information Microservice Test Client ===\n")

    while True:
        context = input("Enter context (or 'exit' to quit): ")

        if context.lower() == "exit":
            break

        data = client.get_info(context)
        client.display_info(data)


if __name__ == "__main__":
    main()
