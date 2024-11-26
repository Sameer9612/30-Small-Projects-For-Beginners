import speedtest

wifi = speedtest.Speedtest()
wifi.get_best_server()

download_speed = wifi.download() / 1_000_000  # Convert to Mbps
upload_speed = wifi.upload() / 1_000_000  # Convert to Mbps

print(f"WiFi Download Speed: {download_speed:.2f} Mbps")
print(f"WiFi Upload Speed: {upload_speed:.2f} Mbps")
