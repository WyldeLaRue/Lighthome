import subprocess

def send_outlet_signal(new_state, outlet_id):
    frequency_table = {
        "on":  {'1': 87347,
                '2': 87491,
                '3': 87811,
                '4': 89347,
                '5': 95491
        },
        "off": {'1': 87356,
                '2': 87500,
                '3': 87820,
                '4': 89356,
                '5': 95500
        }
    }
    frequency = frequency_table[new_state.lower()][str(outlet_id)]
    shell_cmd = 'codesend %d -l 200' % frequency
    subprocess.call(shell_cmd, shell=True)
