import speedtest

def test_network_speed():
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    results = st.results.dict()

    download_speed = results['download'] / 1024 / 1024  # Convert to Mbps
    upload_speed = results['upload'] / 1024 / 1024      # Convert to Mbps
    ping = results['ping']

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")

def main():
    print("Testing network speed...")
    test_network_speed()

if __name__ == "__main__":
    main()
