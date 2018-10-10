import os
def rename():
    file_name = "urls.txt"
    if os.path.exists(file_name):
        with open(file_name, "a") as f:
            content = f.read()
            content = content.split("\n")
            for tmp in content:
                if tmp.startswith("*"):
                    tmp = tmp.replace("*","")
                    tmp = tmp.split("***")
                    name = tmp[1]
                    newname = tmp[0]+".flv"
                    if os.path.exists(name):
                        os.rename(name,newname)


if __name__ == "__main__":
    rename()
