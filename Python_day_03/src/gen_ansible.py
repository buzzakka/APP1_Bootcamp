import yaml
from yaml.loader import SafeLoader

with open("../materials/todo.yml", "r") as file:
    data = yaml.load(file, Loader=SafeLoader)
    install_packages = data["server"]["install_packages"]
    exploit_files = data["server"]["exploit_files"]
    bad_guys = ",".join(data["bad_guys"])
    to_yaml = [
        {
            "name": "Playbook",
            "hosts": "all",
            "become": "yes",
            "tasks": [
                {
                    "name": "Install Python3 and Nginx",
                    "ansible.builtin.apt": {"name": install_packages}
                },
                {
                    "name": "Copy files consumer.py and producer.py",
                    "ansible.builtin.copy": {"src": "{{ item }}", "dest": "{{ item }}"},
                    "loop": exploit_files
                },
                {
                    "name": "Run files",
                    "ansible.builtin.script": {
                        "script": f"{exploit_files[1]} -e {bad_guys}",
                        "interpreter": "python3"
                    }
                }
            ]
        }
    ]
    with open("deploy.yml", "w") as f:
        yaml.dump(to_yaml, f, sort_keys=False)
