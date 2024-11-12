from dulwich import porcelain
import sys

if sys.argv[1] == "update":
	porcelain.pull(".", remote_location="https://github.com/Enviction/LiberIPad.git")
else:
 porcelain.clone("https://github.com/Enviction/LiberIPad.git", ".")