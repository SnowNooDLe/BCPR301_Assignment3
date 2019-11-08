class Writer(object):

    def __init__(self, filename):
        self.file = open(filename, "w")

    def writeToFile(self, job, arg = None):
        # If arg is none, means will only display what they are doing.
        if (arg != None):
        # as some values would be passed int, so converting them to string to be stored in txt
            if (type(arg) != str):
                arg = str(arg)
            # Writing output to text file with new line
            self.file.write(job)
            self.file.write(": ")
            self.file.write(arg)
            self.file.write("\n")
        else:
            # Writing output to text file with new line
            self.file.write(job)
            self.file.write("\n")
