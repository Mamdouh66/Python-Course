File = str(input("File name: ")).strip().lower()
if File.find(".") == -1:
    File += "."
split_character = "."
suffix = File.rsplit(split_character, 1)[1]
match suffix:
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "gif":
        print("image/gif")
    case "pdf" | "zip":
        print("application/"+suffix)
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")
