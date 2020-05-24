from cx_Freeze import setup, Executable

executables = [Executable('Curr_tepm_in_any_city_of_the_world.py')]

includes = ['requests', 'time']

options = {
    'build_exe': {
        'include_msvcr': True,
        'includes': includes,
    }
}

setup(name='Curr_tepm',
      version='0.0.1',
      description='Current tepm in any city of the world!',
      executables=executables,
      options=options)