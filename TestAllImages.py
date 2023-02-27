import glob
import subprocess
imagePathArray= []
path= "D:/Food_Detection_Project/darknetTest"
imagePathArray= glob.glob(path+"/images/*.jpg")
print(imagePathArray)

#subprocess.call("D:/darknet-master/darknet.exe detector test "+ path+"/yolo.data "+ path+"/yolo.cfg "+ path +"/yolo.weights" )
print("D:/darknet-master/darknet.exe detector test "+ path+"/yolo.data "+ path+"/yolo.cfg "+ path +"/yolo.weights")

