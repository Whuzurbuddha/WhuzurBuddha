import subprocess

def show_gpu_info():
    command = 'lspci -v | grep -A7  -i "VGA"'
    main_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = main_process.communicate()
    output = output.decode("utf-8")
    error = error.decode("utf-8")

    if output:
        return output
    else:
        return error

