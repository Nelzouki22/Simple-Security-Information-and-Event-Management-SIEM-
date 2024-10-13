import wmi

def get_event_logs(event_type=None, limit=100):
    # إنشاء كائن WMI للتفاعل مع Event Viewer
    c = wmi.WMI()
    logs = []

    print(f"Reading System Logs (event type: {event_type}, limit: {limit})...")

    # قراءة السجلات من سجل النظام (System Log)
    for log in c.Win32_NTLogEvent(Logfile='System'):
        # تصفية السجلات حسب نوع الحدث
        if event_type == 'Critical' and log.EventType == 1:
            log_info = f"Event ID: {log.EventCode}, Message: {log.Message}, Time: {log.TimeGenerated}"
            print(log_info)
            logs.append(log_info)
        elif event_type == 'Error' and log.EventType == 2:
            log_info = f"Event ID: {log.EventCode}, Message: {log.Message}, Time: {log.TimeGenerated}"
            print(log_info)
            logs.append(log_info)
        elif event_type is None:  # إذا لم يتم تحديد نوع الحدث، يمكننا حفظ جميع الأحداث
            log_info = f"Event ID: {log.EventCode}, Message: {log.Message}, Time: {log.TimeGenerated}"
            print(log_info)
            logs.append(log_info)

        if len(logs) >= limit:
            break  # وقف القراءة بعد الوصول إلى العدد المحدد

    return logs

def save_logs_to_file(logs, file_name='event_logs.txt'):
    # حفظ السجلات في ملف نصي
    with open(file_name, 'w') as file:
        for log in logs:
            file.write(log + "\n")
    print(f"Logs saved to {file_name}")

def main():
    # تحديد نوع الأحداث التي نريد قراءتها (Critical أو Error أو None)
    event_type = 'Critical'  # يمكنك تغييرها إلى 'Error' أو None

    # قراءة السجلات
    logs = get_event_logs(event_type=event_type)
    
    # حفظ السجلات في ملف نصي
    save_logs_to_file(logs)

# تشغيل البرنامج
if __name__ == '__main__':
    main()
