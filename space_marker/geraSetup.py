#pip install cx_freeze
import cx_Freeze
executables =[
    cx_Freeze.Executable(script="space_marker.py", icon="space.ico")
]
cx_Freeze.setup(    
    name = "Space Machine Power",
    options={
        "build_exe":{
            "packages":["pygame","os","time","random","pickle"],
            "include_files":["bg.jpg",
                            "space.png",
                            "Space_Machine_Power.mp3"]
        }
    }, executables = executables
)

#py geraSetup.py build
#py geraSetup.py bdist_msi