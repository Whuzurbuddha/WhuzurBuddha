import subprocess

def show_cpu_info():
    command = 'lshw -C CPU'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    output = output.decode("utf-8")
    error = error.decode("utf-8")

    if output:
        return output
    else:
        return error
