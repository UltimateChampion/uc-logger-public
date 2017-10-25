import sys
import datetime

class UCLogger:

	class FileWriter:
		def __init__(self, _fileName):
			self.fileName = _fileName

		def write(self, _writeString):
			with open(self.fileName, 'a') as theFile:
				theFile.write(_writeString)

	class OutputWriter:
		def __init__(self, _outputType, _fileName = None):
			self.outputType = _outputType
			self.fileName = _fileName
			self.infoWriter = FileWriter(self.fileName) if self.outputType in ["file"] else sys.stdout
			self.errorWriter = FileWriter(self.fileName) if self.outputType in ["file"] else sys.stderr

		def writeInfo(self, _info):
			self.infoWriter.write(_info)

		def writeError(self, _error):
			self.errorWriter.write(_error)

	def __init__(self, _outputType, _fileName = None):
		self.outputType = _outputType
		self.fileName = _fileName
		self.outputWriter = UCLogger.OutputWriter(self.outputType, self.fileName)

	def logInfo(self, _infoString):
		currentTime = datetime.datetime.now()
		logLine = "UC Logger INFO (Time : {}):{}\n".format(currentTime, _infoString)
		self.outputWriter.writeInfo(logLine)

	def logError(self, _infoString):
		currentTime = datetime.datetime.now()
		logLine = "UC Logger ERROR (Time : {}):{}\n".format(currentTime, _infoString)
		self.outputWriter.writeError(logLine)

class UCLogging:
	sharedLogger = None

	def __init__(self, _outputType, _fileName = None):
		if not self.sharedLogger:
			self.sharedLogger = UCLogger(_outputType, _fileName)

	def logger(self):
		return self.sharedLogger

def main():
	UCLogging("out").logger().logInfo("Hello!")
	UCLogging("").logger().logInfo("World!")

if __name__ == "__main__":
	main()