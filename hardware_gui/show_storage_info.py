import subprocess

def show_storage_info():
    command = 'hwinfo --storage-ctrl'
    process = subprocess.Popen(command, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    output, error = process.communicate()
    output = output.decode("utf-8")
    error = error.decode("utf-8")

    if output:
        return output
    else:
        return error
