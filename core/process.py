import psutil  # 실행중인 프로세스 및 시스템 활용 라이브러리


process_names = [
    "Philips_HL7_ManagementSystem.exe",
    "Mediana_HL7_ManagementSystem.exe",
    "Mindray_HL7_ManagementSystem.exe",
    "Code.exe",
]
for proc in psutil.process_iter():
    try:
        # 프로세스 이름, PID값 가져오기
        processName = proc.name()

        try:
            if process_names.index(processName) != -1:
                exist = True
        except Exception:
            pass

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):  # 예외처리
        pass
