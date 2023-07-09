import subprocess

def show_cpu_info():
    command = 'lscpu'
    process  =  subprocess.Popen(command, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    output, error = process.communicate()

    if output:
        return output.decode("utf-8")
    else:
        return error.decode("utf-8")
