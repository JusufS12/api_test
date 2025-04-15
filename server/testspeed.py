import speedtest

def test_speed():
  
  down_speed = 0
  up_speed = 0
  
  try:
    st = speedtest.Speedtest()
    st.get_servers()
    st.get_best_server()
    print('Testing download speed...')
    st.download()
    print('Testing upload speed...')
    st.upload()
    res = st.results.dict()

    down_speed = round(res['download'] / 1000000, 2)
    print(f'Download speed: {down_speed} Mbps')

    up_speed = round(res['upload'] / 1000000, 2)
    print(f'Upload speed: {up_speed} Mbps')

  except speedtest.SpeedtestException as e:
    print(e)
  
  return down_speed, up_speed


test_speed()