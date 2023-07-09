import subprocess

def show_audio_info():
    command = 'lspci -v | grep -A7 -i "audio"'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if output:
        return output.decode("utf-8")
    else: 
        return error.decode("utf-8")
    