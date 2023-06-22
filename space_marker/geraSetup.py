#pip install cx_freeze
import cx_Freeze
executables =[
    cx_Freeze.Executable(script="space_marker.py", icon="assets/space.ico")
]
cx_Freeze.setup(    
    name = "Space Machine Power",
    options={
        "build_exe":{
            "packages":["pygame","os","time","random","pickle"],
            "include_files":["assets/bg.jpg",
                            "assets/space.png",
                            "assets/Space_Machine_Power.mp3"]
        }
    }, executables = executables
)

#py geraSetup.py build
#py geraSetup.py bdist_msi