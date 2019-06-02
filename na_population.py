import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm._title ='Population of Countries in North America'
wm.add('North America',{'ca':34126000,'us':309349000,'mx':11342300})

wm.render_to_file('na_populations.svg')