from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
from modules.workflow import run_workflow
import traceback


def job_listener(event):
    if event.exception:
        print("\n❌ Job crashed!")
        print(traceback.format_exc())
    else:
        print("✅ Job executed successfully.")


def start_scheduler(topic: str):
    scheduler = BlockingScheduler()

    def scheduled_job():
        try:
            result = run_workflow(topic)
            if result:
                print("\nPost generated and saved successfully.\n")
            else:
                print("\nDuplicate detected. Skipped generation.\n")
        except Exception as e:
            print("\n🚨 Unexpected error in scheduled job:")
            print(str(e))

    scheduler.add_listener(job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

    scheduler.add_job(
        scheduled_job,
        trigger="interval",
        minutes=1
    )

    print("Scheduler started. Running every 1 minute...")
    scheduler.start()
