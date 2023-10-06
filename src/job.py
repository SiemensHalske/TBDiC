import json

from typing import Optional

class JobExtension:
    def __init__(self) -> None:
        pass


class Job(JobExtension):
    jobData_path: str = \
        "/home/Hendrik/Documents/Projects/TBDIC/src/jobData.json"
    jobData_list: list = []

    def __init__(self):
        self.file_list: list[str, str] = []
        self.hash_type: str = ""

    def loadJobData(self, file_path: Optional[str] = None) -> None:
        jobData_list = []
        with open(file_path, "r") as f:
            jobData_list = json.load(f)
        self.jobData_list = jobData_list

    def saveJobData(self, file_path: str) -> None:
        def _assembleJobData(self) -> None:
            self.jobData_list.append({
                "file_list": self.file_list,
                "hash_type": self.hash_type
            })
        with open(file_path, "w") as f:
            json.dump(self.jobData_list, f)


def run() -> None:
    job_handler = Job()
    job_handler.loadJobData(job_handler.jobData_path)
    job_handler.saveJobData(job_handler.jobData_path)
    


if __name__ == '__main__':
    print("This program is not meant to be run directly.")
    print("Please run the HashKeepr.py file instead.")
