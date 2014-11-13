import os

for dirname, dirnames, filenames in os.walk('.'):
    #remove students who did not submit a resume
    if not os.listdir(dirname):
        os.rmdir(dirname)
    # print path to all filenames.
    for filename in filenames:
        fileName, fileExtension = os.path.splitext(filename)
        #ignore python files obviously
        if fileExtension == ".py" :
            continue
        #remove bad files created by jotform
        if ("./" + filename == dirname + fileExtension) :
            os.remove(os.path.join(dirname, filename))
        else:
            #reset all resume names
            os.rename(os.path.join(dirname, filename), os.path.join(dirname, "resume" + fileExtension))

    # Don't want to rename any git files now do we?
    if '.git' in dirnames:
        # don't go into any .git directories.
        dirnames.remove('.git')
