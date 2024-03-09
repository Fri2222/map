import subprocess
script_path = r"D:\pythonProject\map\main.py"
# script_path = r"D:\pythonProject\map\main_text.py"
def run_python_script(script_path):
    try:
        subprocess.run(['python', script_path], check=True)
        print("Python脚本执行成功！")
    except subprocess.CalledProcessError as e:
        print(f"Error: Python脚本执行失败 - {e}")

if __name__ == "__main__":
    run_python_script(script_path)
