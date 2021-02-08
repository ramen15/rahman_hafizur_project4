while True:
    print(input.rotation(Rotation.ROLL))
    if input.rotation(Rotation.ROLL) < 0:
        light.set_all(light.rgb(255,0,0))
        music.siren.play_until_done()
    else:
        light.clear()
        music.stop_all_sounds()