import subprocess

def show_gpu_info():
    command = 'lshw -C display'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if output:
        return output.decode("utf-8")
    else:
        return error.decode("utf-8")

