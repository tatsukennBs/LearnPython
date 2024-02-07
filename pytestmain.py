from pytestlib import SampleIot

def main():
    print("Stating")
    device_client = SampleIot.connectionDevices
    print(device_client)

if __name__ == "__main__":
    main()