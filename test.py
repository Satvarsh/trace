import time

H.init("xdn3kmle", {
  tracingOrigins: ['localhost', 'example.myapp.com/backend'],
  networkRecording: {
    enabled: true,
    recordHeadersAndBody: true,
  },
});

def wait_five_minutes():
    print("Starting 5 minute wait...")
    time.sleep(300)  # 300 seconds = 5 minutes
    print("5 minutes have passed!")

# Call the function
if __name__ == "__main__":
    wait_five_minutes()