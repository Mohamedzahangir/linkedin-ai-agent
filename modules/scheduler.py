from apscheduler.schedulers.blocking import BlockingScheduler
from modules.workflow import run_workflow


def start_scheduler(topic: str):
    scheduler = BlockingScheduler()

    scheduler.add_job(
        lambda: run_workflow(topic),
        trigger="interval",
        minutes=1
    )

    print("Scheduler started. Running every 1 minute...")
    scheduler.start()
