import subprocess

def show_gpu_info():
    command = 'lspci -v | grep -A7 -i "gpu"'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    
    if output:
        return output.decode("utf-8")
    else:
        return error.decode("utf-8")

