import speedtest

def test_speed():
  try:
    st = speedtest.Speedtest()

    print('Testing download speed...')
    down_speed = st.download() / 1000000
    print(f'Download speed: {down_speed} Mbps')

    print('Testing upload speed...')
    up_speed = st.upload() / 1000000
    print(f'Upload speed: {up_speed} Mbps')

    return (down_speed, up_speed)

  except speedtest.SpeedtestException as e:
    print(e)
    # return (None, None)


test_speed()